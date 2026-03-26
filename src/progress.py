import sys
import time

_G = "\033[32m"   # green
_Y = "\033[33m"   # yellow
_R = "\033[0m"    # reset

_THROTTLE = 0.25
_SPINNER  = ("◐", "◓", "◑", "◒")


def _enable_ansi():
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7
            )
        except Exception:
            pass


def _fmt(secs):
    secs = int(secs)
    h, rem = divmod(secs, 3600)
    m, s   = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


# ── ProgressBar ───────────────────────────────────────────────────────────────

class ProgressBar:
    """Simple two-line bar used when no Pipeline is active."""

    def __init__(self, total, counters, bar_width=40):
        _enable_ansi()
        self.total   = total
        self.bar_width = bar_width
        self.counts  = {name: 0 for name in counters}
        self._start  = time.monotonic()
        self._status = ""
        self._prev   = 0
        self._tlast  = 0.0

    def status(self, text):
        self._status = text
        self._draw(force=True)

    def update(self, counter, amount=1):
        self.counts[counter] = self.counts.get(counter, 0) + amount
        self._draw()

    def finish(self):
        self._draw(force=True)
        sys.stdout.write("\n")
        sys.stdout.flush()
        self._prev = 0

    def _draw(self, force=False):
        now = time.monotonic()
        if not force and (now - self._tlast) < _THROTTLE:
            return
        self._tlast = now

        lines = []
        if self._status:
            lines.append(f"  {_Y}►{_R}  {self._status}")

        done    = sum(self.counts.values())
        elapsed = now - self._start
        filled  = int(self.bar_width * done / self.total) if self.total else self.bar_width
        bar     = f"{_G}{'█' * filled}{_R}{'░' * (self.bar_width - filled)}"

        if done > 0 and self.total > done:
            eta  = elapsed / done * (self.total - done)
            tstr = f"{_fmt(elapsed)} | ~{_fmt(eta)} Remaining"
        else:
            tstr = _fmt(elapsed)

        stats = "  ".join(f"{n}: {c}" for n, c in self.counts.items())
        lines.append(f"  {bar} {tstr}  {stats}")

        # Build the full redraw as one write so the terminal renders it atomically.
        buf = "\033[1A\033[2K" * self._prev + "\r" if self._prev else ""
        buf += "\n".join(lines) + "\n"
        sys.stdout.write(buf)
        sys.stdout.flush()
        self._prev = len(lines)


# ── Pipeline ──────────────────────────────────────────────────────────────────

class Pipeline:
    """
    Full-pipeline display: a step list with spinner/checkmarks and a shared bar.

    Steps are pre-declared; each moves through pending → running → done.
    Calling begin() on a new step resets the bar for that step.

    Usage:
        pipe = Pipeline(["Processing pairs", "Training GoCP", ...])

        # inside each phase:
        pipe.begin("Training GoCP", total=10, counters=["Folds"])
        pipe.status("Fold 1/10: Training...")
        pipe.update("Folds")
        pipe.finish()

        # after all steps:
        pipe.complete()   # clear the display
        print(summary)    # print final summary
    """

    def __init__(self, steps):
        _enable_ansi()
        self._order  = list(steps)
        self._state  = {s: ("pending", None, None) for s in steps}
        self._cur    = None
        self._status = ""
        self._total  = 1
        self._counts = {}
        self._bstart = None
        self._spin   = 0
        self._prev   = 0
        self._tlast  = 0.0

    # ── Public API ────────────────────────────────────────────────────────────

    def begin(self, step, total, counters):
        """Start a step and reset the progress bar."""
        if step in self._state:
            self._state[step] = ("running", time.monotonic(), None)
        self._cur    = step
        self._total  = total
        self._counts = {c: 0 for c in counters}
        self._bstart = time.monotonic()
        self._status = ""
        self._draw(force=True)

    def status(self, text):
        """Update the sub-step text shown above the bar."""
        self._status = text
        self._draw(force=True)

    def update(self, counter, amount=1):
        """Increment a bar counter."""
        self._counts[counter] = self._counts.get(counter, 0) + amount
        self._draw()

    def ping(self):
        """Advance the spinner without changing counts — use during long setup loops."""
        self._draw()

    def finish(self):
        """Mark the current step as complete."""
        if self._cur and self._cur in self._state:
            _, t0, _ = self._state[self._cur]
            self._state[self._cur] = ("done", t0, time.monotonic())
        self._cur    = None
        self._status = ""
        self._draw(force=True)

    def complete(self):
        """Clear the pipeline display before printing the final summary."""
        if self._prev:
            sys.stdout.write("\033[1A\033[2K" * self._prev + "\r")
            self._prev = 0
        sys.stdout.flush()

    # ── Rendering ─────────────────────────────────────────────────────────────

    def _draw(self, force=False):
        now = time.monotonic()
        if not force and (now - self._tlast) < _THROTTLE:
            return
        self._tlast = now
        self._spin  = (self._spin + 1) % 4

        lines = []

        for name in self._order:
            st, t0, t1 = self._state[name]
            if st == "done":
                lines.append(f"[ {_G}✓{_R} ] {name:<32}  [{_fmt(t1 - t0)}]")
            elif st == "running":
                lines.append(f"[ {_Y}{_SPINNER[self._spin]}{_R} ] {name}")
            else:
                lines.append(f"[   ] {name}")

        lines.append("")

        if self._status:
            lines.append(f"  {self._status}")

        done    = sum(self._counts.values())
        elapsed = (now - self._bstart) if self._bstart else 0
        filled  = int(40 * done / self._total) if self._total else 40
        bar     = f"{_G}{'█' * filled}{_R}{'░' * (40 - filled)}"

        if done > 0 and self._total > done:
            eta  = elapsed / done * (self._total - done)
            tstr = f"{_fmt(elapsed)} | ~{_fmt(eta)} Remaining"
        else:
            tstr = _fmt(elapsed)

        lines.append(f"  {bar} {tstr}")

        # Build the full redraw as one write so the terminal renders it atomically.
        buf = "\033[1A\033[2K" * self._prev + "\r" if self._prev else ""
        buf += "\n".join(lines) + "\n"
        sys.stdout.write(buf)
        sys.stdout.flush()
        self._prev = len(lines)
