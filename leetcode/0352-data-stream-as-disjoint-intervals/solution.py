from bisect import bisect_right
from typing import List

class SummaryRanges:
    def __init__(self):
        self.starts = []
        self.ends = []

    def addNum(self, value: int) -> None:
        i = bisect_right(self.starts, value)  # first interval with start > value
        # already covered by the previous interval
        if i > 0 and self.ends[i - 1] >= value:
            return
        join_left = i > 0 and self.ends[i - 1] + 1 == value
        join_right = i < len(self.starts) and self.starts[i] - 1 == value
        if join_left and join_right:
            self.ends[i - 1] = self.ends[i]
            del self.starts[i]
            del self.ends[i]
        elif join_left:
            self.ends[i - 1] = value
        elif join_right:
            self.starts[i] = value
        else:
            self.starts.insert(i, value)
            self.ends.insert(i, value)

    def getIntervals(self) -> List[List[int]]:
        return [[s, e] for s, e in zip(self.starts, self.ends)]
