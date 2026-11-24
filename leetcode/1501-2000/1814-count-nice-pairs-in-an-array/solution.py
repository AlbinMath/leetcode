class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        freq = {}
        nice_pairs = 0
        
        def rev(x: int) -> int:
            res = 0
            while x > 0:
                res = res * 10 + x % 10
                x //= 10
            return res
        
        for num in nums:
            diff = num - rev(num)
            count = freq.get(diff, 0)
            
            nice_pairs = (nice_pairs + count) % MOD
            freq[diff] = count + 1
            
        return nice_pairs
