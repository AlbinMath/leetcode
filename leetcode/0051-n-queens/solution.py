class Solution:
    def solveNQueens(self, n):
        result = []

        board = [["."] * n for _ in range(n)]

        columns = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):
            # All queens have been placed
            if row == n:
                solution = ["".join(r) for r in board]
                result.append(solution)
                return

            for col in range(n):

                # Check if this position is attacked
                if col in columns:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row][col] = "."
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return result
