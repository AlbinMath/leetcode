from typing import List

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        def key(arr):
            odd = sorted(x for x in arr if x % 2)
            even = sorted(x for x in arr if x % 2 == 0)
            return even, odd

        ne, no = key(nums)
        te, to = key(target)
        total = 0
        for a, b in zip(ne, te):
            total += abs(a - b)
        for a, b in zip(no, to):
            total += abs(a - b)
        return total // 4
