class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        freq = {}
        pairs = 0
        
        for num in nums:
            pairs += freq.get(num - k, 0) + freq.get(num + k, 0)
            freq[num] = freq.get(num, 0) + 1
            
        return pairs
