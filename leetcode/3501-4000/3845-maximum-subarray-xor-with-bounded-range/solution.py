from typing import List
from collections import deque

class Solution:
    def maxXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        B = 15
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] ^ v

        size = (n + 1) * B + 2
        ch0 = [0] * size
        ch1 = [0] * size
        cnt = [0] * size
        tot = 1                      # node 0 is the root

        def update(x: int, d: int) -> None:
            nonlocal tot
            node = 0
            for b in range(B - 1, -1, -1):
                if (x >> b) & 1:
                    nxt = ch1[node]
                    if not nxt:
                        nxt = tot
                        tot += 1
                        ch1[node] = nxt
                else:
                    nxt = ch0[node]
                    if not nxt:
                        nxt = tot
                        tot += 1
                        ch0[node] = nxt
                cnt[nxt] += d
                node = nxt

        def query(x: int) -> int:
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                want = ch0[node] if bit else ch1[node]   # opposite bit
                if want and cnt[want] > 0:
                    res |= 1 << b
                    node = want
                else:
                    node = ch1[node] if bit else ch0[node]
            return res

        mx = deque()   # indices, values decreasing
        mn = deque()   # indices, values increasing
        left = 0
        best = 0
        for r in range(n):
            while mx and nums[mx[-1]] <= nums[r]:
                mx.pop()
            mx.append(r)
            while mn and nums[mn[-1]] >= nums[r]:
                mn.pop()
            mn.append(r)

            update(pre[r], 1)                  # left end l = r becomes available
            while nums[mx[0]] - nums[mn[0]] > k:
                update(pre[left], -1)
                left += 1
                if mx[0] < left:
                    mx.popleft()
                if mn[0] < left:
                    mn.popleft()

            best = max(best, query(pre[r + 1]))
        return best
