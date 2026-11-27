class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        n = len(nums2)
        NEG_INF = float('-inf')
        dp = [NEG_INF] * (n + 1)
        
        for num1 in nums1:
            prev_diag = NEG_INF
            for j, num2 in enumerate(nums2, start=1):
                temp = dp[j]
                prod = num1 * num2
                
                take_both = prod + (prev_diag if prev_diag > 0 else 0)
                dp[j] = max(take_both, dp[j], dp[j - 1])
                
                prev_diag = temp
                
        return dp[n]
