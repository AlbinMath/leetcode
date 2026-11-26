from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        max_len = 0
        
        for k in range(2, n):
            left, right = 0, k - 1
            target = arr[k]
            while left < right:
                pair_sum = arr[left] + arr[right]
                if pair_sum < target:
                    left += 1
                elif pair_sum > target:
                    right -= 1
                else:
                    dp[right][k] = dp[left][right] + 1
                    if dp[right][k] > max_len:
                        max_len = dp[right][k]
                    left += 1
                    right -= 1
                    
        return max_len
