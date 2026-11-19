from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        pre = [0] * (n + 1)
        suf = [0] * (n + 2)
        pre[0] = gaps[0]
        for i in range(1, n + 1):
            pre[i] = max(pre[i - 1], gaps[i])
        for i in range(n, -1, -1):
            suf[i] = max(suf[i + 1], gaps[i])

        ans = 0
        for i in range(n):
            d = endTime[i] - startTime[i]
            other = max(pre[i - 1] if i >= 1 else 0, suf[i + 2])
            merged = gaps[i] + gaps[i + 1]
            if other >= d:
                merged += d
            ans = max(ans, merged)
        return ans
