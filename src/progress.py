import sys


class ProgressBar:
    def __init__(self, total, counters, bar_width=30, fill_char="█", empty_char="░"):
        self.total = total
        self.bar_width = bar_width
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.counts = {name: 0 for name in counters}

    def update(self, counter, amount=1):
        self.counts[counter] = self.counts.get(counter, 0) + amount
        self._render()

    def _render(self):
        done = sum(self.counts.values())
        filled = int(self.bar_width * done / self.total) if self.total else self.bar_width
        bar = self.fill_char * filled + self.empty_char * (self.bar_width - filled)
        stats = "  ".join(f"{name}: {count}" for name, count in self.counts.items())
        sys.stdout.write(f"\r  {bar} {done}/{self.total}  {stats}")
        sys.stdout.flush()

    def finish(self):
        print()
