class Solution:
    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                digit = board[r][c]

                # Ignore empty cells
                if digit == ".":
                    continue

                # Find which 3x3 box this cell belongs to
                box = (r // 3) * 3 + (c // 3)

                # Check duplicate
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False

                # Add digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

        return True
