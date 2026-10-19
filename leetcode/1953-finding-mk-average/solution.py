from collections import deque

class MKAverage:
    N = 100000

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.q = deque()
        self.cnt = [0] * (self.N + 1)
        self.sm = [0] * (self.N + 1)

    def _update(self, v: int, dc: int) -> None:
        ds = dc * v
        i = v
        while i <= self.N:
            self.cnt[i] += dc
            self.sm[i] += ds
            i += i & -i

    def _smallest_sum(self, j: int) -> int:
        # sum of the j smallest elements currently in the window
        pos = c = s = 0
        step = 1 << 16                      # highest power of two <= N
        while step:
            nxt = pos + step
            if nxt <= self.N and c + self.cnt[nxt] < j:
                pos = nxt
                c += self.cnt[nxt]
                s += self.sm[nxt]
            step >>= 1
        # remaining (j - c) elements all have value pos + 1
        return s + (j - c) * (pos + 1)

    def addElement(self, num: int) -> None:
        self.q.append(num)
        self._update(num, 1)
        if len(self.q) > self.m:
            self._update(self.q.popleft(), -1)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        total = self._smallest_sum(self.m - self.k) - self._smallest_sum(self.k)
        return total // (self.m - 2 * self.k)
