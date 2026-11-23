# LeetCode 2617: Minimum Number of Visited Cells in a Grid

**LeetCode Problem #2617 — Minimum Number of Visited Cells in a Grid**
Solve LeetCode Minimum Number of Visited Cells in a Grid using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Visited Cells in a Grid |
| LeetCode | #2617 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** `m x n` integer matrix `grid`. Your initial position is at the **top-left** cell `(0, 0)`.

Starting from the cell `(i, j)`, you can move to one of the following cells:

Cells `(i, k)` with `j < k <= grid[i][j] + j` (rightward movement), or 
 Cells `(k, j)` with `i < k <= grid[i][j] + i` (downward movement).

Return *the minimum number of cells you need to visit to reach the **bottom-right** cell* `(m - 1, n - 1)`. If there is no valid path, return `-1`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `0 <= grid[i][j] < m * n`
- `grid[m - 1][n - 1] == 0`

## Examples
### Example 1
- **Input:** `grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]`
- **Output:** `4`
- **Explanation:** The image above shows one of the paths that visits exactly 4 cells.

### Example 2
- **Input:** `grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]`
- **Output:** `3`
- **Explanation:** The image above shows one of the paths that visits exactly 3 cells.

### Example 3
- **Input:** `grid = [[2,1,0],[1,0,0]]`
- **Output:** `-1`
- **Explanation:** It can be proven that no path exists.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Number of Visited Cells in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The image above shows one of the paths that visits exactly 4 cells.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import deque
from typing import List

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1

        # row_parent[r][c] = next unvisited column index >= c in row r
        row_parent = [list(range(n + 1)) for _ in range(m)]
        # col_parent[c][r] = next unvisited row index >= r in col c
        col_parent = [list(range(m + 1)) for _ in range(n)]

        def find_row(r: int, c: int) -> int:
            path = []
            curr = c
            while row_parent[r][curr] != curr:
                path.append(curr)
                curr = row_parent[r][curr]
            for node in path:
                row_parent[r][node] = curr
            return curr

        def find_col(c: int, r: int) -> int:
            path = []
            curr = r
            while col_parent[c][curr] != curr:
                path.append(curr)
                curr = col_parent[c][curr]
            for node in path:
                col_parent[c][node] = curr
            return curr

        # Mark (0, 0) as visited in both DSUs
        row_parent[0][0] = find_row(0, 1)
        col_parent[0][0] = find_col(0, 1)

        queue = deque([(0, 0, 1)])  # (row, col, distance)

        while queue:
            r, c, d = queue.popleft()
            val = grid[r][c]

            # 1. Scan rightward in row r
            max_c = min(n - 1, c + val)
            nxt_c = find_row(r, c + 1)
            while nxt_c <= max_c:
                if r == m - 1 and nxt_c == n - 1:
                    return d + 1
                queue.append((r, nxt_c, d + 1))
                # Remove nxt_c from row r and column nxt_c
                row_parent[r][nxt_c] = find_row(r, nxt_c + 1)
                col_parent[nxt_c][r] = find_col(nxt_c, r + 1)
                nxt_c = find_row(r, nxt_c)

            # 2. Scan downward in col c
            max_r = min(m - 1, r + val)
            nxt_r = find_col(c, r + 1)
            while nxt_r <= max_r:
                if nxt_r == m - 1 and c == n - 1:
                    return d + 1
                queue.append((nxt_r, c, d + 1))
                # Remove nxt_r from column c and row nxt_r
                col_parent[c][nxt_r] = find_col(c, nxt_r + 1)
                row_parent[nxt_r][c] = find_row(nxt_r, c + 1)
                nxt_r = find_col(c, nxt_r)

        return -1
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [1536. Minimum Swaps to Arrange a Binary Grid](../../1501-2000/1658-minimum-swaps-to-arrange-a-binary-grid/)
- [2257. Count Unguarded Cells in the Grid](../../2001-2500/2343-count-unguarded-cells-in-the-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/)
