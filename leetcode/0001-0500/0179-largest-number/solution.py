from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  # a goes first
            if a + b < b + a:
                return 1
            return 0

        strs.sort(key=cmp_to_key(compare))

        if strs[0] == "0":
            return "0"
        return "".join(strs)
