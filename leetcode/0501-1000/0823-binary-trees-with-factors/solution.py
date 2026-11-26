from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {x: 1 for x in arr}
        
        for i, x in enumerate(arr):
            for j in range(i):
                a = arr[j]
                if a * a > x:
                    break
                    
                if x % a == 0:
                    b = x // a
                    if b in dp:
                        if a == b:
                            dp[x] = (dp[x] + dp[a] * dp[a]) % MOD
                        else:
                            dp[x] = (dp[x] + 2 * dp[a] * dp[b]) % MOD
                            
        return sum(dp.values()) % MOD
