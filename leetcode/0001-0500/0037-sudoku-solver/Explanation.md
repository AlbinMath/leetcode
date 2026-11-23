# LeetCode 37: Sudoku Solver

**LeetCode Problem #37 — Sudoku Solver**
Solve LeetCode Sudoku Solver using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sudoku Solver |
| LeetCode | #37 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

Each of the digits `1-9` must occur exactly once in each row. 
 Each of the digits `1-9` must occur exactly once in each column. 
 Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

## Constraints
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit or `'.'`.
- It is **guaranteed** that the input board has only one solution.

## Examples
### Example 1
- **Input:** `board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]`
- **Output:** `[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]`
- **Explanation:** The input board is shown above and the only valid solution is shown below:

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sudoku Solver**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]`.
4. **Verification:** The input board is shown above and the only valid solution is shown below:

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [36. Valid Sudoku](../../0001-0500/0036-valid-sudoku/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [22. Generate Parentheses](../../0001-0500/0022-generate-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sudoku-solver/)
