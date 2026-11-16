from collections import Counter

class Solution(object):
    def waysToPartition(self, nums, k):
        n = len(nums)
        total = sum(nums)
        
        left = Counter()
        right = Counter()
        
        pref = 0
        for i in range(n - 1):
            pref += nums[i]
            right[total - 2 * pref] += 1
            
        ans = right[0]
        
        pref = 0
        for i in range(n):
            d = k - nums[i]
            ans = max(ans, left[-d] + right[d])
            
            if i < n - 1:
                pref += nums[i]
                diff = total - 2 * pref
                right[diff] -= 1
                left[diff] += 1
                
        return ans
