from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = defaultdict(int)
        top = SortedList()    # pairs (count, value), the x largest
        rest = SortedList()   # remaining pairs
        top_sum = 0

        def remove(v):
            nonlocal top_sum
            c = cnt[v]
            if c == 0:
                return
            p = (c, v)
            if p in top:
                top.remove(p)
                top_sum -= c * v
            else:
                rest.remove(p)

        def insert(v):
            nonlocal top_sum
            c = cnt[v]
            if c == 0:
                return
            p = (c, v)
            top.add(p)
            top_sum += c * v

        def rebalance():
            nonlocal top_sum
            # keep top at most x
            while len(top) > x:
                p = top.pop(0)               # smallest of top
                top_sum -= p[0] * p[1]
                rest.add(p)
            # fill top up to x from rest
            while len(top) < x and rest:
                p = rest.pop()               # largest of rest
                top.add(p)
                top_sum += p[0] * p[1]
            # swap while the best of rest beats the worst of top
            while rest and top and rest[-1] > top[0]:
                a = rest.pop()
                b = top.pop(0)
                top.add(a)
                rest.add(b)
                top_sum += a[0] * a[1] - b[0] * b[1]

        def change(v, delta):
            remove(v)
            cnt[v] += delta
            insert(v)
            rebalance()

        res = []
        for i, v in enumerate(nums):
            change(v, 1)
            if i >= k:
                change(nums[i - k], -1)
            if i >= k - 1:
                res.append(top_sum)
        return res
