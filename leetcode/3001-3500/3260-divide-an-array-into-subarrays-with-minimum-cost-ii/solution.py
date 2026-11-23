import heapq
from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 2

        small = []            # max-heap via negation
        large = []            # min-heap
        del_small = defaultdict(int)
        del_large = defaultdict(int)
        cnt_small = 0
        sum_small = 0
        cnt_large = 0

        def clean_small():
            while small and del_small[-small[0]] > 0:
                del_small[-small[0]] -= 1
                heapq.heappop(small)

        def clean_large():
            while large and del_large[large[0]] > 0:
                del_large[large[0]] -= 1
                heapq.heappop(large)

        def rebalance():
            nonlocal cnt_small, sum_small, cnt_large
            while cnt_small > need:
                clean_small()
                v = -heapq.heappop(small)
                cnt_small -= 1
                sum_small -= v
                heapq.heappush(large, v)
                cnt_large += 1
            while cnt_small < need and cnt_large > 0:
                clean_large()
                v = heapq.heappop(large)
                cnt_large -= 1
                heapq.heappush(small, -v)
                cnt_small += 1
                sum_small += v
            while True:
                clean_small()
                clean_large()
                if small and large and -small[0] > large[0]:
                    a = -heapq.heappop(small)
                    b = heapq.heappop(large)
                    heapq.heappush(small, -b)
                    heapq.heappush(large, a)
                    sum_small += b - a
                else:
                    break

        def add(v):
            nonlocal cnt_small, sum_small, cnt_large
            clean_small()
            if small and v <= -small[0]:
                heapq.heappush(small, -v)
                cnt_small += 1
                sum_small += v
            else:
                heapq.heappush(large, v)
                cnt_large += 1
            rebalance()

        def remove(v):
            nonlocal cnt_small, sum_small, cnt_large
            clean_small()
            if small and v <= -small[0]:
                del_small[v] += 1
                cnt_small -= 1
                sum_small -= v
            else:
                del_large[v] += 1
                cnt_large -= 1
            rebalance()

        best = float('inf')
        for j in range(2, min(n - 1, 1 + dist) + 1):
            add(nums[j])
        if cnt_small == need:
            best = nums[1] + sum_small

        for i in range(2, n):
            remove(nums[i])
            if i + dist < n:
                add(nums[i + dist])
            if cnt_small == need:
                best = min(best, nums[i] + sum_small)

        return nums[0] + best
