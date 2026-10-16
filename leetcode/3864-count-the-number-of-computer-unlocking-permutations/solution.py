from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        c0 = complexity[0]
        for v in complexity[1:]:
            if v <= c0:
                return 0
        ans = 1
        for i in range(2, len(complexity)):
            ans = ans * i % MOD
        return ans
