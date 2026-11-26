from collections import defaultdict
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        max_len = 0
        
        for num in arr:
            dp[num] = dp[num - difference] + 1
            if dp[num] > max_len:
                max_len = dp[num]
                
        return max_len
