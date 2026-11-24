
from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""] * 3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            player = "A" if i % 2 == 0 else "B"
            board[r][c] = "X" if player == "A" else "O"

            mark = board[r][c]

            # Check row and column
            if all(board[r][j] == mark for j in range(3)):
                return player

            if all(board[j][c] == mark for j in range(3)):
                return player

            # Check diagonals
            if r == c and all(board[j][j] == mark for j in range(3)):
                return player

            if r + c == 2 and all(board[j][2 - j] == mark for j in range(3)):
                return player

        return "Draw" if len(moves) == 9 else "Pending"

