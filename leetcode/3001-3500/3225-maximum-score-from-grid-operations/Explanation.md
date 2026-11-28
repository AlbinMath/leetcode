# LeetCode 3225: Maximum Score From Grid Operations

**LeetCode Problem #3225 — Maximum Score From Grid Operations**
Solve LeetCode Maximum Score From Grid Operations using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score From Grid Operations |
| LeetCode | #3225 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D matrix `grid` of size `n x n`. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices `(i, j)`, and color black all the cells of the `j^th` column starting from the top row down to the `i^th` row.

The grid score is the sum of all `grid[i][j]` such that cell `(i, j)` is white and it has a horizontally adjacent black cell.

Return the **maximum** score that can be achieved after some number of operations.

## Constraints
- `1 <= n == grid.length <= 100`
- `n == grid[i].length`
- `0 <= grid[i][j] <= 10^9`

## Examples
### Example 1
- **Input:** `grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]`
- **Output:** `11`
- **Explanation:** In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is `grid[3][0] + grid[1][2] + grid[3][3]` which is equal to 11.

### Example 2
- **Input:** `grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]`
- **Output:** `94`
- **Explanation:** We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is `grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4]` which is equal to 94.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Score From Grid Operations**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is `grid[3][0] + grid[1][2] + grid[3][3]` which is equal to 11.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        NEG = -10**18

        pre = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pre[j][i + 1] = pre[j][i] + grid[i][j]

        # dp[a][b]: a = h[j-1], b = h[j]
        dp = [[NEG] * (n + 1) for _ in range(n + 1)]
        for b in range(n + 1):
            dp[0][b] = 0

        for j in range(n):
            p = pre[j]
            cs = range(n + 1) if j < n - 1 else [0]
            new = [[NEG] * (n + 1) for _ in range(n + 1)]

            for b in range(n + 1):
                pb = p[b]
                # prefix max of dp[a][b]
                pm = [NEG] * (n + 1)
                cur = NEG
                for a in range(n + 1):
                    cur = max(cur, dp[a][b])
                    pm[a] = cur
                # suffix max of dp[a][b] + S(b, a)
                sm = [NEG] * (n + 2)
                for a in range(n, -1, -1):
                    val = dp[a][b]
                    if val > NEG:
                        val += max(0, p[a] - pb)
                    sm[a] = max(sm[a + 1], val)

                for c in cs:
                    best = NEG
                    if pm[c] > NEG:
                        best = pm[c] + max(0, p[c] - pb)
                    best = max(best, sm[c + 1])
                    new[b][c] = best

            dp = new

        return max(dp[b][0] for b in range(n + 1))
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1770. Maximum Score from Performing Multiplication Operations](../../1501-2000/1770-maximum-score-from-performing-multiplication-operations/)
- [3038. Maximum Number of Operations With the Same Score I](../../3001-3500/3038-maximum-number-of-operations-with-the-same-score-i/)
- [3040. Maximum Number of Operations With the Same Score II](../../3001-3500/3040-maximum-number-of-operations-with-the-same-score-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-from-grid-operations/)
