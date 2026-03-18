import sys


class ProgressBar:
    def __init__(self, total, counters, bar_width=30, fill_char="█", empty_char="░"):
        self.total = total
        self.bar_width = bar_width
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.counts = {name: 0 for name in counters}
        self._status = ""
        self._has_status = False

    def update(self, counter, amount=1):
        self.counts[counter] = self.counts.get(counter, 0) + amount
        self._render()

    def status(self, text):
        self._status = text
        self._has_status = True
        self._render()

    def _render(self):
        done = sum(self.counts.values())
        filled = int(self.bar_width * done / self.total) if self.total else self.bar_width
        bar = self.fill_char * filled + self.empty_char * (self.bar_width - filled)
        stats = "  ".join(f"{name}: {count}" for name, count in self.counts.items())
        # Move to start, clear line, write bar
        line = f"  {bar} {done}/{self.total}  {stats}"
        if self._has_status:
            # Clear both lines: move up if we previously wrote a status line
            sys.stdout.write(f"\r\033[K{line}\n\033[K    {self._status}\033[A")
        else:
            sys.stdout.write(f"\r\033[K{line}")
        sys.stdout.flush()

    def finish(self):
        if self._has_status:
            # Clear the status line below, then move to next line
            sys.stdout.write(f"\n\033[K")
        print()
