class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg = 0
        min_abs = float('inf')

        for row in matrix:
            for v in row:
                if v < 0:
                    neg += 1
                a = abs(v)
                total += a
                min_abs = min(min_abs, a)

        return total if neg % 2 == 0 else total - 2 * min_abs
