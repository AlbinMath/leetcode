class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # directions: N, E, S, W
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        d = 0  # index into dirs, 0 = north

        for c in instructions:
            if c == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif c == 'L':
                d = (d - 1) % 4
            else:  # 'R'
                d = (d + 1) % 4

        return (x == 0 and y == 0) or d != 0
