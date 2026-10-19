from typing import List

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)     # appended in increasing order

        # iterative post-order DFS building the global string
        start = [0] * n
        end = [0] * n
        chars = []
        stack = [(0, 0)]                      # (node, next child index)
        start[0] = 0
        while stack:
            x, idx = stack.pop()
            if idx == 0:
                start[x] = len(chars)
            if idx < len(children[x]):
                stack.append((x, idx + 1))
                stack.append((children[x][idx], 0))
            else:
                chars.append(s[x])
                end[x] = len(chars) - 1

        # Manacher on '#'-separated string
        t = '#' + '#'.join(chars) + '#'
        m = len(t)
        p = [0] * m
        c = r = 0
        for i in range(m):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < m and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]

        ans = [False] * n
        for x in range(n):
            l, rr = start[x], end[x]
            ans[x] = p[l + rr + 1] >= rr - l + 1
        return ans
