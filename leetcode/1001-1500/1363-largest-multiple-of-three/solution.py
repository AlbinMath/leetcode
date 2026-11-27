from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()  # ascending, so the first matches are the smallest
        total = sum(digits)
        r = total % 3

        def remove(rem: int, count: int) -> bool:
            idxs = [i for i, d in enumerate(digits) if d % 3 == rem][:count]
            if len(idxs) < count:
                return False
            for i in reversed(idxs):
                digits.pop(i)
            return True

        if r == 1:
            if not remove(1, 1):
                remove(2, 2)
        elif r == 2:
            if not remove(2, 1):
                remove(1, 2)

        if not digits:
            return ""
        if digits[-1] == 0:
            return "0"
        return ''.join(map(str, reversed(digits)))
