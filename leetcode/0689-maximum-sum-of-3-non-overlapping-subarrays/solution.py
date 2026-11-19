from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = n - k + 1
        
        win = [0] * m
        curr_sum = sum(nums[:k])
        win[0] = curr_sum
        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]
            win[i - k + 1] = curr_sum
            
        left = [0] * m
        best_left = 0
        for i in range(m):
            if win[i] > win[best_left]:
                best_left = i
            left[i] = best_left
            
        right = [0] * m
        best_right = m - 1
        for i in range(m - 1, -1, -1):
            if win[i] >= win[best_right]:
                best_right = i
            right[i] = best_right
            
        ans = [0, k, 2 * k]
        max_total = -1
        for j in range(k, m - k):
            i = left[j - k]
            l = right[j + k]
            total = win[i] + win[j] + win[l]
            if total > max_total:
                max_total = total
                ans = [i, j, l]
                
        return ans
