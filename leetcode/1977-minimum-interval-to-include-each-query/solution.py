import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        res = [-1] * len(queries)
        heap = []
        k = 0
        n = len(intervals)
        for qi in order:
            q = queries[qi]
            while k < n and intervals[k][0] <= q:
                l, r = intervals[k]
                heapq.heappush(heap, (r - l + 1, r))
                k += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[qi] = heap[0][0]
        return res
