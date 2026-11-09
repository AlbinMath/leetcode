from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                h[j] = h[j] + 1 if mat[i][j] else 0

            cnt = [0] * n
            stack = []
            for j in range(n):
                while stack and h[stack[-1]] >= h[j]:
                    stack.pop()
                if stack:
                    p = stack[-1]
                    cnt[j] = cnt[p] + h[j] * (j - p)
                else:
                    cnt[j] = h[j] * (j + 1)
                stack.append(j)
                total += cnt[j]

        return total
