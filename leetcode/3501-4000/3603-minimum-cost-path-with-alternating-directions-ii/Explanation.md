# LeetCode 3603: Minimum Cost Path with Alternating Directions II

**LeetCode Problem #3603 — Minimum Cost Path with Alternating Directions II**
Solve LeetCode Minimum Cost Path with Alternating Directions II using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path with Alternating Directions II |
| LeetCode | #3603 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `m` and `n` representing the number of rows and columns of a grid, respectively.

The cost to enter cell `(i, j)` is defined as `(i + 1) * (j + 1)`.

You are also given a 2D integer array `waitCost` where `waitCost[i][j]` defines the cost to **wait** on that cell.

The path will always begin by entering cell `(0, 0)` on move 1 and paying the entrance cost.

At each step, you follow an alternating pattern:

On **odd-numbered** seconds, you must move **right** or **down** to an **adjacent** cell, paying its entry cost. 
 On **even-numbered** seconds, you must **wait** in place for **exactly** one second and pay `waitCost[i][j]` during that second.

Return the **minimum** total cost required to reach `(m - 1, n - 1)`.

## Constraints
- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- `waitCost.length == m`
- `waitCost[0].length == n`
- `0 <= waitCost[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `m = 1, n = 2, waitCost = [[1,2]]`
- **Output:** `3`
- **Explanation:** The optimal path is: 

 
 Start at cell `(0, 0)` at second 1 with entry cost `(0 + 1) * (0 + 1) = 1`.

### Example 2
- **Input:** `m = 2, n = 2, waitCost = [[3,5],[2,4]]`
- **Output:** `9`
- **Explanation:** The optimal path is: 

 
 Start at cell `(0, 0)` at second 1 with entry cost `(0 + 1) * (0 + 1) = 1`.

### Example 3
- **Input:** `m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]]`
- **Output:** `16`
- **Explanation:** The optimal path is: 

 
 Start at cell `(0, 0)` at second 1 with entry cost `(0 + 1) * (0 + 1) = 1`.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost Path with Alternating Directions II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 1, n = 2, waitCost = [[1,2]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The optimal path is: 

 
 Start at cell `(0, 0)` at second 1 with entry cost `(0 + 1) * (0 + 1) = 1`.

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
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = float('inf')
        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = 1

        def w(x, y):
            return 0 if x == 0 and y == 0 else waitCost[x][y]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                best = INF
                if i > 0:
                    best = min(best, dp[i - 1][j] + w(i - 1, j))
                if j > 0:
                    best = min(best, dp[i][j - 1] + w(i, j - 1))
                dp[i][j] = best + (i + 1) * (j + 1)

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
- [4003. Minimum Cost Path with Alternating Directions III](../../4001-4500/4003-minimum-cost-path-with-alternating-directions-iii/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2304. Minimum Path Cost in a Grid](../../2001-2500/2304-minimum-path-cost-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/)
