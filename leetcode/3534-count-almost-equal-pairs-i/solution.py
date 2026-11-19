from typing import List

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        L = max(len(str(x)) for x in nums)
        strs = [str(x).zfill(L) for x in nums]

        def almost(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            diff = [i for i in range(L) if a[i] != b[i]]
            return len(diff) == 2

        ans = 0
        n = len(strs)
        for i in range(n):
            for j in range(i + 1, n):
                if almost(strs[i], strs[j]):
                    ans += 1
        return ans
