import heapq
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        a = nums[:]
        nxt = list(range(1, n + 1))          # nxt[i] == n means no next
        prv = list(range(-1, n - 1))         # prv[i] == -1 means no prev
        alive = [True] * n

        bad = sum(1 for i in range(n - 1) if a[i] > a[i + 1])
        heap = [(a[i] + a[i + 1], i) for i in range(n - 1)]
        heapq.heapify(heap)

        ops = 0
        while bad > 0:
            s, i = heapq.heappop(heap)
            # validate entry: i alive, has a next, and sum still matches
            if not alive[i]:
                continue
            j = nxt[i]
            if j >= n or not alive[j] or a[i] + a[j] != s:
                continue

            p = prv[i]
            k = nxt[j]

            # remove contributions of old pairs (p,i), (i,j), (j,k)
            if p >= 0 and a[p] > a[i]:
                bad -= 1
            if a[i] > a[j]:
                bad -= 1
            if k < n and a[j] > a[k]:
                bad -= 1

            # merge j into i
            a[i] = s
            alive[j] = False
            nxt[i] = k
            if k < n:
                prv[k] = i

            # add contributions of new pairs (p,i), (i,k)
            if p >= 0 and a[p] > a[i]:
                bad += 1
            if k < n and a[i] > a[k]:
                bad += 1

            # push new candidate pair sums
            if p >= 0:
                heapq.heappush(heap, (a[p] + a[i], p))
            if k < n:
                heapq.heappush(heap, (a[i] + a[k], i))

            ops += 1
        return ops
