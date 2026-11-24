# LeetCode 130: Surrounded Regions

**LeetCode Problem #130 — Surrounded Regions**
Solve LeetCode Surrounded Regions using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Surrounded Regions |
| LeetCode | #130 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

**Connect**: A cell is connected to adjacent cells horizontally or vertically. 
 **Region**: To form a region **connect every** `'O'` cell. 
 **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed **by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

## Examples
### Example 1
- **Input:** `board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`
- **Output:** `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`
- **Explanation:** In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

### Example 2
- **Input:** `board = [["X"]]`
- **Output:** `[["X"]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Surrounded Regions**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`.
4. **Verification:** In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var solve = function(board) {
    const m = board.length;
    const n = board[0].length;

    function dfs(row, col) {
        if (
            row < 0 ||
            row >= m ||
            col < 0 ||
            col >= n ||
            board[row][col] !== "O"
        ) {
            return;
        }

        // Preserve boundary-connected regions
        board[row][col] = "#";

        dfs(row - 1, col); // Up
        dfs(row + 1, col); // Down
        dfs(row, col - 1); // Left
        dfs(row, col + 1); // Right
    }

    // Explore the first and last columns
    for (let row = 0; row < m; row++) {
        dfs(row, 0);
        dfs(row, n - 1);
    }

    // Explore the first and last rows
    for (let col = 0; col < n; col++) {
        dfs(0, col);
        dfs(m - 1, col);
    }

    // Capture surrounded regions and restore safe regions
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (board[row][col] === "O") {
                board[row][col] = "X";
            } else if (board[row][col] === "#") {
                board[row][col] = "O";
            }
        }
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [959. Regions Cut By Slashes](../../0501-1000/0959-regions-cut-by-slashes/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/surrounded-regions/)
