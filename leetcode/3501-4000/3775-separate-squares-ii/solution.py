from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = sorted({x for x, _, l in squares} | {x + l for x, _, l in squares})
        idx = {v: i for i, v in enumerate(xs)}
        m = len(xs) - 1  # number of elementary segments
        cnt = [0] * (4 * m)
        ln = [0] * (4 * m)

        def update(node, lo, hi, a, b, v):
            if a >= hi or b <= lo:
                return
            if a <= lo and hi <= b:
                cnt[node] += v
            else:
                mid = (lo + hi) // 2
                update(node * 2, lo, mid, a, b, v)
                update(node * 2 + 1, mid, hi, a, b, v)
            if cnt[node] > 0:
                ln[node] = xs[hi] - xs[lo]
            elif hi - lo == 1:
                ln[node] = 0
            else:
                ln[node] = ln[node * 2] + ln[node * 2 + 1]

        events = []
        for x, y, l in squares:
            a, b = idx[x], idx[x + l]
            events.append((y, 1, a, b))
            events.append((y + l, -1, a, b))
        events.sort()

        # pass 1: total area, recording strips
        strips = []  # (y_start, width, height)
        total = 0
        prev_y = events[0][0]
        for y, v, a, b in events:
            if y > prev_y:
                w = ln[1]
                total += w * (y - prev_y)
                strips.append((prev_y, w, y - prev_y))
                prev_y = y
            update(1, 0, m, a, b, v)

        # pass 2: find the crossing strip (compare 2*acc with total to stay exact)
        acc = 0
        for y0, w, h in strips:
            if w > 0 and 2 * (acc + w * h) >= total:
                return y0 + (total / 2 - acc) / w
            acc += w * h
        return float(prev_y)
