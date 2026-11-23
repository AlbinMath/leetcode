class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        n = len(nums)
        freq = [0] * 1001
        
        for arr in nums:
            for num in arr:
                freq[num] += 1
                
        return [num for num in range(1, 1001) if freq[num] == n]
