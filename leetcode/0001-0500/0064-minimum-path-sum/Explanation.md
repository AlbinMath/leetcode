# LeetCode 64: Minimum Path Sum

**LeetCode Problem #64 — Minimum Path Sum**
Solve LeetCode Minimum Path Sum using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Path Sum |
| LeetCode | #64 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

## Examples
### Example 1
- **Input:** `grid = [[1,3,1],[1,5,1],[4,2,1]]`
- **Output:** `7`
- **Explanation:** Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.

### Example 2
- **Input:** `grid = [[1,2,3],[4,5,6]]`
- **Output:** `12`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Path Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,3,1],[1,5,1],[4,2,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var minPathSum = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    // Initialize the first column.
    for (let i = 1; i < m; i++) {
        grid[i][0] += grid[i - 1][0];
    }

    // Initialize the first row.
    for (let j = 1; j < n; j++) {
        grid[0][j] += grid[0][j - 1];
    }

    // Calculate the minimum sum for each remaining cell.
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            grid[i][j] += Math.min(
                grid[i - 1][j],  // From above
                grid[i][j - 1]   // From the left
            );
        }
    }

    return grid[m - 1][n - 1];
};
```

### Python
```python
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n

        for row in range(m):
            for col in range(n):

                if row == 0 and col == 0:
                    dp[col] = grid[row][col]

                elif row == 0:
                    dp[col] = dp[col - 1] + grid[row][col]

                elif col == 0:
                    dp[col] = dp[col] + grid[row][col]

                else:
                    dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[n - 1]
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
- [931. Minimum Falling Path Sum](../../0501-1000/0967-minimum-falling-path-sum/)
- [1289. Minimum Falling Path Sum II](../../1001-1500/1224-minimum-falling-path-sum-ii/)
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-path-sum/)
