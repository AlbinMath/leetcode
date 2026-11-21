class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        ends_with_0 = 0
        ends_with_1 = 0
        has_zero = 0
        
        for ch in binary:
            if ch == '0':
                ends_with_0 = (ends_with_0 + ends_with_1) % MOD
                has_zero = 1
            else:
                ends_with_1 = (ends_with_0 + ends_with_1 + 1) % MOD
                
        return (ends_with_0 + ends_with_1 + has_zero) % MOD
