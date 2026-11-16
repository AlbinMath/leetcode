from typing import List
from math import gcd

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        coprime = [[] for _ in range(51)]
        for a in range(1, 51):
            for b in range(1, 51):
                if gcd(a, b) == 1:
                    coprime[a].append(b)

        ans = [-1] * n
        last = [(-1, -1)] * 51  # value -> (node, depth) of nearest ancestor with it

        # stack entries: (node, parent, depth, saved_entry, exiting)
        stack = [(0, -1, 0, None, False)]
        while stack:
            u, p, d, saved, exiting = stack.pop()
            if exiting:
                last[nums[u]] = saved
                continue

            best_depth = -1
            for v in coprime[nums[u]]:
                node, depth = last[v]
                if depth > best_depth:
                    best_depth = depth
                    ans[u] = node

            stack.append((u, p, d, last[nums[u]], True))  # restore on exit
            last[nums[u]] = (u, d)
            for w in adj[u]:
                if w != p:
                    stack.append((w, u, d + 1, None, False))
        return ans
