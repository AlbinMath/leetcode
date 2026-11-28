# LeetCode 1594: Maximum Non Negative Product in a Matrix

**LeetCode Problem #1594 — Maximum Non Negative Product in a Matrix**
Solve LeetCode Maximum Non Negative Product in a Matrix using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Non Negative Product in a Matrix |
| LeetCode | #1594 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a `m x n` matrix `grid`. Initially, you are located at the top-left corner `(0, 0)`, and in each step, you can only **move right or down** in the matrix.

Among all possible paths starting from the top-left corner `(0, 0)` and ending in the bottom-right corner `(m - 1, n - 1)`, find the path with the **maximum non-negative product**. The product of a path is the product of all integers in the grid cells visited along the path.

Return the *maximum non-negative product **modulo** *`10^9 + 7`. *If the maximum product is **negative**, return *`-1`.

Notice that the modulo is performed after getting the maximum product.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 15`
- `-4 <= grid[i][j] <= 4`

## Examples
### Example 1
- **Input:** `grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]`
- **Output:** `-1`
- **Explanation:** It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

### Example 2
- **Input:** `grid = [[1,-2,1],[1,-2,1],[3,-4,1]]`
- **Output:** `8`
- **Explanation:** Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).

### Example 3
- **Input:** `grid = [[1,3],[0,-4]]`
- **Output:** `0`
- **Explanation:** Maximum non-negative product is shown (1 * 0 * -4 = 0).

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Non Negative Product in a Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `-1`.
4. **Verification:** It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

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
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]

        mx[0][0] = mn[0][0] = grid[0][0]

        for j in range(1, n):
            mx[0][j] = mn[0][j] = mx[0][j - 1] * grid[0][j]
        for i in range(1, m):
            mx[i][0] = mn[i][0] = mx[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                candidates = (
                    mx[i - 1][j] * v, mn[i - 1][j] * v,
                    mx[i][j - 1] * v, mn[i][j - 1] * v,
                )
                mx[i][j] = max(candidates)
                mn[i][j] = min(candidates)

        res = mx[m - 1][n - 1]
        return res % (10**9 + 7) if res >= 0 else -1
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
- [1351. Count Negative Numbers in a Sorted Matrix](../../1001-1500/1351-count-negative-numbers-in-a-sorted-matrix/)
- [1975. Maximum Matrix Sum](../../1501-2000/1975-maximum-matrix-sum/)
- [2713. Maximum Strictly Increasing Cells in a Matrix](../../2501-3000/2713-maximum-strictly-increasing-cells-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/)
