class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(m):
            if i > 0:
                for j in range(n):
                    if matrix[i][j]:
                        matrix[i][j] += matrix[i - 1][j]

            row = sorted(matrix[i], reverse=True)
            for k, h in enumerate(row, 1):
                res = max(res, h * k)

        return res
