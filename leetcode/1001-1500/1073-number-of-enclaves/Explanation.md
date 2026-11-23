# LeetCode 1020: Number of Enclaves

**LeetCode Problem #1020 — Number of Enclaves**
Solve LeetCode Number of Enclaves using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Enclaves |
| LeetCode | #1020 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` binary matrix `grid`, where `0` represents a sea cell and `1` represents a land cell.

A **move** consists of walking from one land cell to another adjacent (**4-directionally**) land cell or walking off the boundary of the `grid`.

Return *the number of land cells in* `grid` *for which we cannot walk off the boundary of the grid in any number of **moves***.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 500`
- `grid[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]`
- **Output:** `3`
- **Explanation:** There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

### Example 2
- **Input:** `grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]`
- **Output:** `0`
- **Explanation:** All 1s are either on the boundary or can reach the boundary.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Enclaves**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

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
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            grid[r][c] = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)

        # 1. Flood-fill from left and right boundaries
        for r in range(m):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][n - 1] == 1:
                dfs(r, n - 1)

        # 2. Flood-fill from top and bottom boundaries
        for c in range(n):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[m - 1][c] == 1:
                dfs(m - 1, c)

        # 3. Count remaining enclosed land cells
        return sum(grid[r][c] == 1 for r in range(m) for c in range(n))
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
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-enclaves/)
