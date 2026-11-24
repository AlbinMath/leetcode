from math import gcd
from collections import Counter
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c, ans = Counter(), 0
        for x in nums:
            g = gcd(x, k)
            ans += sum(v for d, v in c.items() if g * d % k == 0)
            c[g] += 1
        return ans
