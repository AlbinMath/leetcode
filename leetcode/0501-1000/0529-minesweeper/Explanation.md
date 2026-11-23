# LeetCode 529: Minesweeper

**LeetCode Problem #529 — Minesweeper**
Solve LeetCode Minesweeper using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minesweeper |
| LeetCode | #529 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Let's play the minesweeper game ( Wikipedia , online game )!

You are given an `m x n` char matrix `board` representing the game board where:

`'M'` represents an unrevealed mine, 
 `'E'` represents an unrevealed empty square, 
 `'B'` represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals), 
 digit (`'1'` to `'8'`) represents how many mines are adjacent to this revealed square, and 
 `'X'` represents a revealed mine.

You are also given an integer array `click` where `click = [click_r, click_c]` represents the next click position among all the unrevealed squares (`'M'` or `'E'`).

Return *the board after revealing this position according to the following rules*:

If a mine `'M'` is revealed, then the game is over. You should change it to `'X'`. 
 If an empty square `'E'` with no adjacent mines is revealed, then change it to a revealed blank `'B'` and all of its adjacent unrevealed squares should be revealed recursively. 
 If an empty square `'E'` with at least one adjacent mine is revealed, then change it to a digit (`'1'` to `'8'`) representing the number of adjacent mines. 
 Return the board when no more squares will be revealed.

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 50`
- `board[i][j]` is either `'M'`, `'E'`, `'B'`, or a digit from `'1'` to `'8'`.
- `click.length == 2`
- `0 <= click_r < m`
- `0 <= click_c < n`
- `board[click_r][click_c]` is either `'M'` or `'E'`.

## Examples
### Example 1
- **Input:** `board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]`
- **Output:** `[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]`

### Example 2
- **Input:** `board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]`
- **Output:** `[["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minesweeper**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click
        
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
            
        dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        
        def dfs(cr: int, cc: int) -> None:
            mines = 0
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    mines += 1
                    
            if mines > 0:
                board[cr][cc] = str(mines)
                return
                
            board[cr][cc] = 'B'
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                    dfs(nr, nc)
                    
        dfs(r, c)
        return board
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [6. Zigzag Conversion](../../0001-0500/0006-zigzag-conversion/)
- [79. Word Search](../../0001-0500/0079-word-search/)
- [112. Path Sum](../../0001-0500/0112-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minesweeper/)
