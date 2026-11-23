from itertools import permutations

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(x: str, y: str) -> str:
            if y in x:
                return x
            if x in y:
                return y
            for k in range(min(len(x), len(y)), 0, -1):
                if x[-k:] == y[:k]:
                    return x + y[k:]
            return x + y

        best = None
        for p in permutations((a, b, c)):
            s = merge(merge(p[0], p[1]), p[2])
            if best is None or (len(s), s) < (len(best), best):
                best = s
        return best
