# LeetCode 3651: Minimum Cost Path with Teleportations

**LeetCode Problem #3651 — Minimum Cost Path with Teleportations**
Solve LeetCode Minimum Cost Path with Teleportations using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path with Teleportations |
| LeetCode | #3651 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a `m x n` 2D integer array `grid` and an integer `k`. You start at the top-left cell `(0, 0)` and your goal is to reach the bottom‐right cell `(m - 1, n - 1)`.

There are two types of moves available:

**Normal move**: You can move right or down from your current cell `(i, j)`, i.e. you can move to `(i, j + 1)` (right) or `(i + 1, j)` (down). The cost is the value of the destination cell.

**Teleportation**: You can teleport from any cell `(i, j)`, to any cell `(x, y)` such that `grid[x][y] <= grid[i][j]`; the cost of this move is 0. You may teleport at most `k` times.

Return the **minimum** total cost to reach cell `(m - 1, n - 1)` from `(0, 0)`.

## Constraints
- `2 <= m, n <= 80`
- `m == grid.length`
- `n == grid[i].length`
- `0 <= grid[i][j] <= 10^4`
- `0 <= k <= 10`

## Examples
### Example 1
- **Input:** `grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2`
- **Output:** `7`
- **Explanation:** Initially we are at (0, 0) and cost is 0. 

 
 
 
 Current Position 
 Move 
 New Position 
 Total Cost 
 
 
 `(0, 0)` 
 Move Down 
 `(1, 0)` 
 `0 + 2 = 2` 
 
 
 `(1, 0)` 
 Move Right 
 `(1, 1)` 
 `2 + 5 = 7` 
 
 
 `(1, 1)` 
 Teleport to `(2, 2)` 
 `(2, 2)` 
 `7 + 0 = 7` 
 
 
 

 The minimum cost to reach bottom-right cell is 7.

### Example 2
- **Input:** `grid = [[1,2],[2,3],[3,4]], k = 1`
- **Output:** `9`
- **Explanation:** Initially we are at (0, 0) and cost is 0. 

 
 
 
 Current Position 
 Move 
 New Position 
 Total Cost 
 
 
 `(0, 0)` 
 Move Down 
 `(1, 0)` 
 `0 + 2 = 2` 
 
 
 `(1, 0)` 
 Move Right 
 `(1, 1)` 
 `2 + 3 = 5` 
 
 
 `(1, 1)` 
 Move Down 
 `(2, 1)` 
 `5 + 4 = 9` 
 
 
 

 The minimum cost to reach bottom-right cell is 9.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost Path with Teleportations**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Initially we are at (0, 0) and cost is 0. 

 
 
 
 Current Position 
 Move 
 New Position 
 Total Cost 
 
 
 `(0, 0)` 
 Move Down 
 `(1, 0)` 
 `0 + 2 = 2` 
 
 
 `(1, 0)` 
 Move Right 
 `(1, 1)` 
 `2 + 5 = 7` 
 
 
 `(1, 1)` 
 Teleport to `(2, 2)` 
 `(2, 2)` 
 `7 + 0 = 7` 
 
 
 

 The minimum cost to reach bottom-right cell is 7.

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
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        cells = sorted(((grid[i][j], i, j) for i in range(m) for j in range(n)),
                       reverse=True)

        def relax(base):
            dp = [[INF] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        dp[0][0] = 0
                        continue
                    best = base[i][j]
                    if i > 0:
                        best = min(best, dp[i - 1][j] + grid[i][j])
                    if j > 0:
                        best = min(best, dp[i][j - 1] + grid[i][j])
                    dp[i][j] = best
            return dp

        dp = relax([[INF] * n for _ in range(m)])  # layer 0

        for _ in range(k):
            tele = [[INF] * n for _ in range(m)]
            run = INF
            idx = 0
            total = len(cells)
            while idx < total:
                v = cells[idx][0]
                j2 = idx
                # include the whole group of equal values before reading run
                while j2 < total and cells[j2][0] == v:
                    _, a, b = cells[j2]
                    run = min(run, dp[a][b])
                    j2 += 1
                for t in range(idx, j2):
                    _, a, b = cells[t]
                    tele[a][b] = run
                idx = j2

            base = [[min(dp[i][j], tele[i][j]) for j in range(n)] for i in range(m)]
            dp = relax(base)

        return dp[m - 1][n - 1]
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2304. Minimum Path Cost in a Grid](../../2001-2500/2304-minimum-path-cost-in-a-grid/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2662-minimum-cost-of-a-path-with-special-roads/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-teleportations/)
