class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0       # index of the current page
        self.last = 0      # index of the last valid page in history

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur < len(self.history):
            self.history[self.cur] = url   # overwrite stale forward entry
        else:
            self.history.append(url)
        self.last = self.cur               # everything after is discarded

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.last, self.cur + steps)
        return self.history[self.cur]
