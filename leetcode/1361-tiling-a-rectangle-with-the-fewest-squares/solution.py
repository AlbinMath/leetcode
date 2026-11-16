class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # n rows, m columns; heights[c] = filled height of column c
        best = n * m
        heights = [0] * m

        def dfs(count: int) -> None:
            nonlocal best
            if count >= best:
                return
            # find the lowest column (leftmost on ties)
            low = min(heights)
            if low == n:
                best = count
                return
            start = heights.index(low)

            # width of the flat segment starting at `start`
            end = start
            while end < m and heights[end] == low:
                end += 1
            max_side = min(end - start, n - low)

            for side in range(max_side, 0, -1):
                for c in range(start, start + side):
                    heights[c] += side
                dfs(count + 1)
                for c in range(start, start + side):
                    heights[c] -= side

        dfs(0)
        return best
