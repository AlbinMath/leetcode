from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        diameter = 2 * k + 1
        
        if diameter > n:
            return avgs
            
        window_sum = sum(nums[:diameter])
        avgs[k] = window_sum // diameter
        
        for right in range(diameter, n):
            window_sum += nums[right] - nums[right - diameter]
            avgs[right - k] = window_sum // diameter
            
        return avgs
