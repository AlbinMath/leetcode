class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        even = 0  
        odd = 0  
        
        for x in nums:
            even, odd = max(even, odd + x), max(odd, even - x)
            
        return even
