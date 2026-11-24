# LeetCode 1275: Find Winner on a Tic Tac Toe Game

**LeetCode Problem #1275 — Find Winner on a Tic Tac Toe Game**
Solve LeetCode Find Winner on a Tic Tac Toe Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Winner on a Tic Tac Toe Game |
| LeetCode | #1275 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
**Tic-tac-toe** is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares `' '`. 
 The first player `A` always places `'X'` characters, while the second player `B` always places `'O'` characters. 
 `'X'` and `'O'` characters are always placed into empty squares, never on filled ones. 
 The game ends when there are **three** of the same (non-empty) character filling any row, column, or diagonal. 
 The game also ends if all squares are non-empty. 
 No more moves can be played if the game is over.

Given a 2D integer array `moves` where `moves[i] = [row_i, col_i]` indicates that the `i^th` move will be played on `grid[row_i][col_i]`. return *the winner of the game if it exists* (`A` or `B`). In case the game ends in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of **Tic-Tac-Toe**), the grid is initially empty, and `A` will play first.

## Constraints
- `1 <= moves.length <= 9`
- `moves[i].length == 2`
- `0 <= row_i, col_i <= 2`
- There are no repeated elements on `moves`.
- `moves` follow the rules of tic tac toe.

## Examples
### Example 1
- **Input:** `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`
- **Output:** `"A"`
- **Explanation:** A wins, they always play first.

### Example 2
- **Input:** `moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]`
- **Output:** `"B"`
- **Explanation:** B wins.

### Example 3
- **Input:** `moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]`
- **Output:** `"Draw"`
- **Explanation:** The game ends in a draw since there are no moves to make.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Winner on a Tic Tac Toe Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"A"`.
4. **Verification:** A wins, they always play first.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1535. Find the Winner of an Array Game](../../1501-2000/1535-find-the-winner-of-an-array-game/)
- [1823. Find the Winner of the Circular Game](../../1501-2000/1823-find-the-winner-of-the-circular-game/)
- [794. Valid Tic-Tac-Toe State](../../0501-1000/0794-valid-tic-tac-toe-state/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)
