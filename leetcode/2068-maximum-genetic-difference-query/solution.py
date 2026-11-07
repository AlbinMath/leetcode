from typing import List

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        B = 18

        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        qs = [[] for _ in range(n)]
        for qi, (node, val) in enumerate(queries):
            qs[node].append((val, qi))

        # trie: child arrays and pass-through counts
        c0, c1, cnt = [0], [0], [0]

        def update(v, delta):
            node = 0
            for b in range(B - 1, -1, -1):
                if (v >> b) & 1:
                    if not c1[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c1[node] = len(cnt) - 1
                    node = c1[node]
                else:
                    if not c0[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c0[node] = len(cnt) - 1
                    node = c0[node]
                cnt[node] += delta

        def best(x):
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                if (x >> b) & 1:
                    want = c0[node]   # opposite bit is 0
                    other = c1[node]
                else:
                    want = c1[node]
                    other = c0[node]
                if want and cnt[want] > 0:
                    res |= 1 << b
                    node = want
                else:
                    node = other
            return res

        ans = [0] * len(queries)
        # iterative DFS: (node, state) with state 0 = enter, 1 = exit
        stack = [(root, 0)]
        while stack:
            u, state = stack.pop()
            if state == 1:
                update(u, -1)
                continue
            update(u, 1)
            for val, qi in qs[u]:
                ans[qi] = best(val)
            stack.append((u, 1))
            for c in children[u]:
                stack.append((c, 0))
        return ans
