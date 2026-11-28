# LeetCode 51: N-Queens

**LeetCode Problem #51 — N-Queens**
Solve LeetCode N-Queens using JavaScript, Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | N-Queens |
| LeetCode | #51 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

## Constraints
- `1 <= n <= 9`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]`
- **Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above

### Example 2
- **Input:** `n = 1`
- **Output:** `[["Q"]]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **N-Queens**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]`.
4. **Verification:** There exist two distinct solutions to the 4-queens puzzle as shown above

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var solveNQueens = function(n) {
    const result = [];
    const board = Array.from({ length: n }, () => ".".repeat(n));

    const cols = new Set();
    const diag1 = new Set(); // row - col
    const diag2 = new Set(); // row + col

    function backtrack(row) {
        if (row === n) {
            result.push([...board]);
            return;
        }

        for (let col = 0; col < n; col++) {
            if (
                cols.has(col) ||
                diag1.has(row - col) ||
                diag2.has(row + col)
            ) {
                continue;
            }

            // Place the queen
            board[row] =
                board[row].substring(0, col) +
                "Q" +
                board[row].substring(col + 1);

            cols.add(col);
            diag1.add(row - col);
            diag2.add(row + col);

            backtrack(row + 1);

            // Backtrack: remove the queen
            board[row] =
                board[row].substring(0, col) +
                "." +
                board[row].substring(col + 1);

            cols.delete(col);
            diag1.delete(row - col);
            diag2.delete(row + col);
        }
    }

    backtrack(0);
    return result;
};
```

### Python
```python
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
- [52. N-Queens II](../../0001-0500/0052-n-queens-ii/)
- [1222. Queens That Can Attack the King](../../1001-1500/1222-queens-that-can-attack-the-king/)
- [50. Pow(x, n)](../../0001-0500/0050-powx-n/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/n-queens/)
