from collections import Counter

class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        pairs = 0
        leftovers = 0
        
        for count in freq.values():
            pairs += count // 2
            leftovers += count % 2
            
        return [pairs, leftovers]
