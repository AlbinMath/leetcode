from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = nums[n // 2]

        def mirror(left: int, odd: bool) -> int:
            s = str(left)
            return int(s + (s[-2::-1] if odd else s[::-1]))

        s = str(m)
        L = len(s)
        half = int(s[:(L + 1) // 2])
        odd = L % 2 == 1

        cands = set()
        for h in (half - 1, half, half + 1):
            if h > 0:
                cands.add(mirror(h, odd))
        # length-boundary palindromes
        cands.add(10 ** (L - 1) - 1)   # 99...9 with L-1 digits
        cands.add(10 ** L + 1)         # 100...01 with L+1 digits
        cands = {c for c in cands if c >= 1}

        def cost(x: int) -> int:
            return sum(abs(a - x) for a in nums)

        return min(cost(c) for c in cands)
