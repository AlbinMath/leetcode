from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        w = k + 1
        cur = sum(gaps[:w])
        best = cur
        for i in range(w, len(gaps)):
            cur += gaps[i] - gaps[i - w]
            best = max(best, cur)
        return best
