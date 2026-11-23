class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def between(x, lo, hi):
            return min(lo, hi) < x < max(lo, hi)

        # Rook (a, b) -> queen (e, f)
        if a == e and not (c == a and between(d, b, f)):
            return 1
        if b == f and not (d == b and between(c, a, e)):
            return 1

        # Bishop (c, d) -> queen (e, f)
        if abs(c - e) == abs(d - f):
            # Rook blocks if it is on the same diagonal, strictly between
            if not (abs(a - c) == abs(b - d)
                    and abs(a - e) == abs(b - f)
                    and between(a, c, e)):
                return 1

        return 2
