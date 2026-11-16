class Solution(object):
    def sumOfFlooredPairs(self, nums):
        MOD = 10**9 + 7
        max_val = max(nums)
        
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        pref = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            pref[i] = pref[i - 1] + freq[i]
            
        ans = 0
        for d in range(1, max_val + 1):
            c = freq[d]
            if c == 0:
                continue
            
            k = 1
            while k * d <= max_val:
                left = k * d
                right = min(max_val, (k + 1) * d - 1)
                count_in_range = pref[right] - pref[left - 1]
                ans = (ans + c * k * count_in_range) % MOD
                k += 1
                
        return ans
