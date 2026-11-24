from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
            
        g = [i - r for r, i in enumerate(idx for idx, val in enumerate(nums) if val == 1)]
        m = len(g)
        
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = pref[i] + g[i]
            
        min_swaps = float('inf')
        for i in range(m - k + 1):
            mid = i + k // 2
            median_val = g[mid]
            left_cost = median_val * (mid - i) - (pref[mid] - pref[i])
            right_cost = (pref[i + k] - pref[mid + 1]) - median_val * (i + k - 1 - mid)
            if left_cost + right_cost < min_swaps:
                min_swaps = left_cost + right_cost
                
        return min_swaps
