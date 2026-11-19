from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt = defaultdict(int)   # prefix value -> how many earlier indices
        total = defaultdict(int) # prefix value -> sum of those indices
        cnt[0] = 1               # p[0] = 0 at index 0
        total[0] = 0

        pref = 0
        ans = 0
        for m in range(1, len(arr) + 1):
            pref ^= arr[m - 1]
            ans += cnt[pref] * (m - 1) - total[pref]
            cnt[pref] += 1
            total[pref] += m

        return ans
