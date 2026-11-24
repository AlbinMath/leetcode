class Solution:
    def specialGrid(self, n):
        size = 1 << n
        grid = [[0] * size for _ in range(size)]

        def fill(r, c, s, base):
            if s == 1:
                grid[r][c] = base
                return
            if s == 2:
                grid[r][c + 1] = base
                grid[r + 1][c + 1] = base + 1
                grid[r + 1][c] = base + 2
                grid[r][c] = base + 3
                return
            h = s // 2
            q = h * h
            fill(r, c + h, h, base)
            fill(r + h, c + h, h, base + q)
            fill(r + h, c, h, base + 2 * q)
            fill(r, c, h, base + 3 * q)

        fill(0, 0, size, 0)
        return grid
