
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row, col = i, j

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for dr, dc in directions:
            r, c = row + dr, col + dc

            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'B':
                    break

                if board[r][c] == 'p':
                    count += 1
                    break

                r += dr
                c += dc

        return count

