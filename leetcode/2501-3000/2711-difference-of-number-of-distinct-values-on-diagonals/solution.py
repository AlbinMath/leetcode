class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]

        # diagonals start in the top row or the left column
        starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(1, m)]

        for r0, c0 in starts:
            # collect the cells of this diagonal
            cells = []
            r, c = r0, c0
            while r < m and c < n:
                cells.append((r, c))
                r += 1
                c += 1

            seen = set()
            for r, c in cells:               # top-left -> bottom-right
                left[r][c] = len(seen)       # excludes the cell itself
                seen.add(grid[r][c])

            seen = set()
            for r, c in reversed(cells):     # bottom-right -> top-left
                right[r][c] = len(seen)
                seen.add(grid[r][c])

        return [[abs(left[i][j] - right[i][j]) for j in range(n)] for i in range(m)]
