# LeetCode 52: N-Queens II

**LeetCode Problem #52 — N-Queens II**
Solve LeetCode N-Queens II using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | N-Queens II |
| LeetCode | #52 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *the number of distinct solutions to the **n-queens puzzle***.

## Constraints
- `1 <= n <= 9`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `2`
- **Explanation:** There are two distinct solutions to the 4-queens puzzle as shown.

### Example 2
- **Input:** `n = 1`
- **Output:** `1`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **N-Queens II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

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
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are two distinct solutions to the 4-queens puzzle as shown.

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
    def totalNQueens(self, n):
        columns = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):
            # All queens placed successfully
            if row == n:
                return 1

            count = 0

            for col in range(n):

                # Check column
                if col in columns:
                    continue

                # Check \ diagonal
                if row - col in diag1:
                    continue

                # Check / diagonal
                if row + col in diag2:
                    continue

                # Place queen
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Explore
                count += backtrack(row + 1)

                # Backtrack
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return count

        return backtrack(0)
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
- [51. N-Queens](../../0001-0500/0051-n-queens/)
- [50. Pow(x, n)](../../0001-0500/0050-powx-n/)
- [429. N-ary Tree Level Order Traversal](../../0001-0500/0429-n-ary-tree-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/n-queens-ii/)
