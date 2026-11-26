from collections import defaultdict
from typing import List

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = defaultdict(int)  # number -> occurrences
        freq = defaultdict(int)   # occurrences -> count of distinct numbers with this frequency
        max_freq = 0
        ans = 0
        
        for i, num in enumerate(nums):
            prev_f = count[num]
            if prev_f > 0:
                freq[prev_f] -= 1
                
            curr_f = prev_f + 1
            count[num] = curr_f
            freq[curr_f] += 1
            
            if curr_f > max_freq:
                max_freq = curr_f
                
            prefix_len = i + 1
            
            # Check the 3 valid prefix conditions
            case1 = (max_freq == 1)
            case2 = (freq[max_freq] * max_freq + 1 == prefix_len)
            case3 = (freq[max_freq] == 1 and max_freq + freq[max_freq - 1] * (max_freq - 1) == prefix_len)
            
            if case1 or case2 or case3:
                ans = prefix_len
                
        return ans
