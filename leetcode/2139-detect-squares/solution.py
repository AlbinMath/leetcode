from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.cnt = defaultdict(int)             # (x, y) -> times added
        self.by_y = defaultdict(lambda: defaultdict(int))  # y -> {x: count}

    def add(self, point):
        x, y = point
        self.cnt[(x, y)] += 1
        self.by_y[y][x] += 1

    def count(self, point) -> int:
        qx, qy = point
        res = 0
        for x, c in self.by_y[qy].items():
            if x == qx:
                continue
            d = x - qx
            for ny in (qy + d, qy - d):
                res += c * self.cnt[(qx, ny)] * self.cnt[(x, ny)]
        return res
