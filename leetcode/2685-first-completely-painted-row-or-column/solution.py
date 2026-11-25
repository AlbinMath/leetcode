class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        pos = [None] * (m * n + 1)
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)

        row_cnt = [0] * m
        col_cnt = [0] * n

        for idx, v in enumerate(arr):
            r, c = pos[v]
            row_cnt[r] += 1
            col_cnt[c] += 1
            if row_cnt[r] == n or col_cnt[c] == m:
                return idx

        return -1
