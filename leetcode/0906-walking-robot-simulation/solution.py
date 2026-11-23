class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = set(map(tuple, obstacles))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        x = y = d = 0
        best = 0

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(c):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in blocked:
                        break
                    x, y = nx, ny
                    best = max(best, x * x + y * y)
        return best
