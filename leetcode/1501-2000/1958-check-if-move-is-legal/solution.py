class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        opp = 'W' if color == 'B' else 'B'
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dr, dc in directions:
            r, c = rMove + dr, cMove + dc
            length = 1
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opp:
                r += dr
                c += dc
                length += 1

            if length >= 2 and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                return True

        return False
