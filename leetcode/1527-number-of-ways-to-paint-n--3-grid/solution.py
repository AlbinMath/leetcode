class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        aba = 6
        abc = 6
        
        for _ in range(1, n):
            aba, abc = (
                (3 * aba + 2 * abc) % MOD,
                (2 * aba + 2 * abc) % MOD
            )
            
        return (aba + abc) % MOD
