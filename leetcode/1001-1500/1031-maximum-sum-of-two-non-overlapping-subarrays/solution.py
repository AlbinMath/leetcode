from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def max_two(L: int, M: int) -> int:
            sum_L = sum(nums[:L])
            sum_M = sum(nums[L : L + M])
            max_L = sum_L
            ans = max_L + sum_M
            
            for i in range(L + M, len(nums)):
                sum_L += nums[i - M] - nums[i - M - L]
                sum_M += nums[i] - nums[i - M]
                if sum_L > max_L:
                    max_L = sum_L
                if max_L + sum_M > ans:
                    ans = max_L + sum_M
                    
            return ans
            
        return max(max_two(firstLen, secondLen), max_two(secondLen, firstLen))
