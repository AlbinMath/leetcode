from collections import Counter

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        freq = Counter(nums)
        total_ops = 0
        
        for count in freq.values():
            if count == 1:
                return -1
            total_ops += (count + 2) // 3
            
        return total_ops
