class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        n = len(nums)
        total_diff = 0
        
        while nums[0] > 0:
            cnt = [0] * 10
            for i in range(n):
                cnt[nums[i] % 10] += 1
                nums[i] //= 10
                
            total_diff += sum(c * (n - c) for c in cnt) // 2
            
        return total_diff
