class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        
        freq = {}
        good_pairs = 0
        
        for i, num in enumerate(nums):
            diff = num - i
            count = freq.get(diff, 0)
            
            good_pairs += count
            freq[diff] = count + 1
            
        return total_pairs - good_pairs
