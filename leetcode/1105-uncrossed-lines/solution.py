class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        n = len(nums2)
        dp = [0] * (n + 1)
        
        for num1 in nums1:
            prev_diag = 0
            for j, num2 in enumerate(nums2, start=1):
                temp = dp[j]
                if num1 == num2:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp
                
        return dp[n]
