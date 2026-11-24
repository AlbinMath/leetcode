from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = sum(l * l for _, _, l in squares)
        half = total / 2

        def below(y: float) -> float:
            s = 0.0
            for _, yi, l in squares:
                h = y - yi
                if h > 0:
                    s += l * (h if h < l else l)
            return s

        lo, hi = 0.0, float(max(yi + l for _, yi, l in squares))
        for _ in range(100):
            mid = (lo + hi) / 2
            if below(mid) >= half:
                hi = mid
            else:
                lo = mid
        return hi
