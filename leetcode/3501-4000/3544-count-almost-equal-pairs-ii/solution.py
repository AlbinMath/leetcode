from typing import List
from collections import Counter

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        L = len(str(max(nums)))
        cnt = Counter()
        ans = 0

        for x in nums:
            s = str(x).zfill(L)
            reach = {s}
            lst = list(s)

            for i in range(L):
                for j in range(i + 1, L):
                    lst[i], lst[j] = lst[j], lst[i]
                    reach.add(''.join(lst))
                    for p in range(L):
                        for q in range(p + 1, L):
                            lst[p], lst[q] = lst[q], lst[p]
                            reach.add(''.join(lst))
                            lst[p], lst[q] = lst[q], lst[p]
                    lst[i], lst[j] = lst[j], lst[i]

            for r in reach:
                ans += cnt[r]
            cnt[s] += 1

        return ans
