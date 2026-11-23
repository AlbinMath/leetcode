from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0  # counts of prefix parities seen so far (empty prefix is even)
        parity = 0
        ans = 0
        for x in arr:
            parity ^= (x & 1)
            if parity == 0:
                ans += odd   # need an earlier odd prefix
                even += 1
            else:
                ans += even  # need an earlier even prefix
                odd += 1
        return ans % MOD
