from typing import List
from collections import Counter

class Solution:
    def findGoodIntegers(self, n: int) -> List[int]:
        cnt = Counter()
        a = 1
        while 2 * a ** 3 <= n:          # smallest sum with this a is a^3 + a^3
            b = a
            while True:
                s = a ** 3 + b ** 3
                if s > n:
                    break
                cnt[s] += 1
                b += 1
            a += 1
        return sorted(s for s, c in cnt.items() if c >= 2)
