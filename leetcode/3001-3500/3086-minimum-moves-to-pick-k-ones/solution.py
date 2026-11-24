from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        best = float('inf')
        for i in range(n):
            a = nums[i]
            b = (nums[i - 1] if i > 0 else 0) + (nums[i + 1] if i + 1 < n else 0)
            t = min(k, a + b)
            r = k - t
            if r <= maxChanges:
                best = min(best, (t - a) + 2 * r)
        pos = [i for i, v in enumerate(nums) if v]
        m = len(pos)
        need = k - maxChanges
        if 1 <= need <= m:
            P = [0] * (m + 1)
            for i, p in enumerate(pos):
                P[i + 1] = P[i] + p
            cost2 = float('inf')
            for l in range(m - need + 1):
                r = l + need - 1
                mid = l + need // 2
                left = pos[mid] * (mid - l) - (P[mid] - P[l])
                right = (P[r + 1] - P[mid + 1]) - pos[mid] * (r - mid)
                cost2 = min(cost2, left + right)
            best = min(best, cost2 + 2 * maxChanges)

        return best
