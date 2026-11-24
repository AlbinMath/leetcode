class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stk = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stk) < self.maxSize:
            self.stk.append(x)

    def pop(self) -> int:
        if not self.stk:
            return -1
        i = len(self.stk) - 1
        res = self.stk.pop() + self.inc[i]
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        self.inc[i] = 0
        return res

    def increment(self, k: int, val: int) -> None:
        idx = min(k, len(self.stk)) - 1
        if idx >= 0:
            self.inc[idx] += val
