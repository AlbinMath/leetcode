
from collections import defaultdict
from bisect import bisect_left, bisect_right


class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.positions = defaultdict(list)

        # Store each value's occurrence indices
        for i, value in enumerate(arr):
            self.positions[value].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        indices = self.positions[value]

        # Count indices in the inclusive range [left, right]
        start = bisect_left(indices, left)
        end = bisect_right(indices, right)

        return end - start

