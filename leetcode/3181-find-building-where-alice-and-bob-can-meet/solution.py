from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        size = 1
        while size < n:
            size *= 2

        t = [0] * (2 * size)
        t[size:size+n] = heights

        for i in range(size - 1, 0, -1):
            t[i] = max(t[2*i], t[2*i+1])

        def find(node, l, r, start, h):
            if r < start or t[node] <= h:
                return -1
            if l == r:
                return l if l < n else -1
            m = (l + r) // 2
            x = find(node*2, l, m, start, h)
            return x if x != -1 else find(node*2+1, m+1, r, start, h)

        ans = []
        for a, b in queries:
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                ans.append(b)
            else:
                ans.append(find(1, 0, size-1, b+1, heights[a]))

        return ans
