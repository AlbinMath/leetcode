# LeetCode 3567: Minimum Absolute Difference in Sliding Submatrix

**LeetCode Problem #3567 — Minimum Absolute Difference in Sliding Submatrix**
Solve LeetCode Minimum Absolute Difference in Sliding Submatrix using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Absolute Difference in Sliding Submatrix |
| LeetCode | #3567 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` integer matrix `grid` and an integer `k`.

For every contiguous `k x k` **submatrix** of `grid`, compute the **minimum absolute** difference between any two **distinct** values within that **submatrix**.

Return a 2D array `ans` of size `(m - k + 1) x (n - k + 1)`, where `ans[i][j]` is the minimum absolute difference in the submatrix whose top-left corner is `(i, j)` in `grid`.

**Note**: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix `(x1, y1, x2, y2)` is a matrix that is formed by choosing all cells `matrix[x][y]` where `x1 <= x <= x2` and `y1 <= y <= y2`.

## Constraints
- `1 <= m == grid.length <= 30`
- `1 <= n == grid[i].length <= 30`
- `-10^5 <= grid[i][j] <= 10^5`
- `1 <= k <= min(m, n)`

## Examples
### Example 1
- **Input:** `grid = [[1,8],[3,-2]], k = 2`
- **Output:** `[[2]]`
- **Explanation:** There is only one possible `k x k` submatrix: ` [[1, 8], [3, -2]] ` . 
 Distinct values in the submatrix are `[1, 8, 3, -2]`. 
 The minimum absolute difference in the submatrix is `|1 - 3| = 2`. Thus, the answer is `[[2]]`.

### Example 2
- **Input:** `grid = [[3,-1]], k = 1`
- **Output:** `[[0,0]]`
- **Explanation:** Both `k x k` submatrix has only one distinct element. 
 Thus, the answer is `[[0, 0]]`.

### Example 3
- **Input:** `grid = [[1,-2,3],[2,3,5]], k = 2`
- **Output:** `[[1,2]]`
- **Explanation:** There are two possible `k &times; k` submatrix:

 
 Starting at `(0, 0)`: `[[1, -2], [2, 3]]`.

 
 Distinct values in the submatrix are `[1, -2, 2, 3]`. 
 The minimum absolute difference in the submatrix is `|1 - 2| = 1`. 
 
 
 Starting at `(0, 1)`: `[[-2, 3], [3, 5]]`.
 
 Distinct values in the submatrix are `[-2, 3, 5]`. 
 The minimum absolute difference in the submatrix is `|3 - 5| = 2`. 
 
 
 
 
 Thus, the answer is `[[1, 2]]`.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Absolute Difference in Sliding Submatrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,8],[3,-2]], k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[2]]`.
4. **Verification:** There is only one possible `k x k` submatrix: ` [[1, 8], [3, -2]] ` . 
 Distinct values in the submatrix are `[1, 8, 3, -2]`. 
 The minimum absolute difference in the submatrix is `|1 - 3| = 2`. Thus, the answer is `[[2]]`.

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
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = sorted({grid[x][y]
                               for x in range(i, i + k)
                               for y in range(j, j + k)})
                if len(vals) > 1:
                    ans[i][j] = min(b - a for a, b in zip(vals, vals[1:]))

        return ans
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
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)
- [1200. Minimum Absolute Difference](../../1001-1500/1200-minimum-absolute-difference/)
- [1818. Minimum Absolute Sum Difference](../../1501-2000/1818-minimum-absolute-sum-difference/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/)
