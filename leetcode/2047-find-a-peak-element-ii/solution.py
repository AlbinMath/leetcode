from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # row of the maximum in column mid
            r = max(range(m), key=lambda i: mat[i][mid])
            val = mat[r][mid]

            left = mat[r][mid - 1] if mid > 0 else -1
            right = mat[r][mid + 1] if mid < n - 1 else -1

            if val > left and val > right:
                return [r, mid]
            if left > val:
                hi = mid - 1
            else:
                lo = mid + 1

        return [-1, -1]  # unreachable given the problem guarantees
