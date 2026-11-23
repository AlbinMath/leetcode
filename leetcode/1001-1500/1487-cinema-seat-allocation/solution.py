from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:
        rows = defaultdict(int)

        # Record reserved seats using bits 1 through 10
        for row, seat in reservedSeats:
            rows[row] |= 1 << seat

        # Seat blocks: 2-5, 4-7, 6-9
        left =  sum(1 << s for s in range(2, 6))
        middle = sum(1 << s for s in range(4, 8))
        right = sum(1 << s for s in range(6, 10))

        result = 2 * n

        for mask in rows.values():
            left_free = (mask & left) == 0
            middle_free = (mask & middle) == 0
            right_free = (mask & right) == 0

            if left_free and right_free:
                # Two families fit in this row
                continue
            elif left_free or middle_free or right_free:
                # Only one family fits
                result -= 1
            else:
                # No family fits
                result -= 2

        return result
