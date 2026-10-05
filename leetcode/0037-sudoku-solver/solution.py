class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing digits
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    digit = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box].add(digit)

        digits = set("123456789")

        def backtrack():

            # Find the empty cell with the fewest choices
            best_cell = None
            best_choices = None

            for r in range(9):
                for c in range(9):

                    if board[r][c] == ".":

                        box = (r // 3) * 3 + (c // 3)

                        used = rows[r] | cols[c] | boxes[box]
                        choices = digits - used

                        # No possible digit
                        if not choices:
                            return False

                        # Choose the cell with minimum choices
                        if best_choices is None or len(choices) < len(best_choices):
                            best_cell = (r, c, box)
                            best_choices = choices

                            # Can't get better than one choice
                            if len(best_choices) == 1:
                                break

                if best_choices is not None and len(best_choices) == 1:
                    break

            # No empty cells → Sudoku solved
            if best_cell is None:
                return True

            r, c, box = best_cell

            # Try each possible digit
            for digit in best_choices:

                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

                if backtrack():
                    return True

                # Undo
                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)

            return False

        backtrack()
