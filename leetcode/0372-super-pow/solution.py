from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD
        res = 1
        for d in b:
            res = pow(res, 10, MOD) * pow(a, d, MOD) % MOD
        return res
