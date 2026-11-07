import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        cost = self._window_costs(nums, x)  # length n - x + 1

        INF = float('inf')
        prev = [0] * (n + 1)  # dp for j = 0
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] != INF:
                    cur[i] = min(cur[i], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]

    def _window_costs(self, nums, x):
        n = len(nums)
        lo = []  # max-heap via negatives
        hi = []  # min-heap
        delayed = defaultdict(int)
        lo_size = hi_size = 0
        lo_sum = hi_sum = 0

        def prune(heap, is_lo):
            while heap:
                v = -heap[0] if is_lo else heap[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            target = (lo_size + hi_size + 1) // 2
            while lo_size > target:
                prune(lo, True)
                v = -heapq.heappop(lo)
                heapq.heappush(hi, v)
                lo_size -= 1; hi_size += 1
                lo_sum -= v; hi_sum += v
            while lo_size < target:
                prune(hi, False)
                v = heapq.heappop(hi)
                heapq.heappush(lo, -v)
                hi_size -= 1; lo_size += 1
                hi_sum -= v; lo_sum += v

        def add(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            prune(lo, True)
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v)
                lo_size += 1; lo_sum += v
            else:
                heapq.heappush(hi, v)
                hi_size += 1; hi_sum += v
            rebalance()

        def remove(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            prune(lo, True)
            delayed[v] += 1
            if v <= -lo[0]:
                lo_size -= 1; lo_sum -= v
                prune(lo, True)
            else:
                hi_size -= 1; hi_sum -= v
                prune(hi, False)
            rebalance()

        res = []
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                prune(lo, True)
                med = -lo[0]
                res.append(med * lo_size - lo_sum + hi_sum - med * hi_size)
        return res
