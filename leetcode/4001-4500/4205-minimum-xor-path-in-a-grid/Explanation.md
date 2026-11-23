# LeetCode 3882: Minimum XOR Path in a Grid

**LeetCode Problem #3882 — Minimum XOR Path in a Grid**
Solve LeetCode Minimum XOR Path in a Grid using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum XOR Path in a Grid |
| LeetCode | #3882 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `grid` of size `m * n`.

You start at the **top-left** cell `(0, 0)` and want to reach the **bottom-right** cell `(m - 1, n - 1)`.

At each step, you **may** move either **right or down**.

The **cost** of a path is defined as the **bitwise XOR** of all the values in the cells along that path, **including** the start and end cells.

Return the **minimum** possible XOR value among all valid paths from `(0, 0)` to `(m - 1, n - 1)`.

## Constraints
- `1 <= m == grid.length <= 1000`
- `1 <= n == grid[i].length <= 1000`
- `m * n <= 1000`
- `0 <= grid[i][j] <= 1023​`

## Examples
### Example 1
- **Input:** `grid = [[1,2],[3,4]]`
- **Output:** `6`
- **Explanation:** There are two valid paths: 

 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1)` with XOR: `1 XOR 2 XOR 4 = 7` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1)` with XOR: `1 XOR 3 XOR 4 = 6` 
 

 The minimum XOR value among all valid paths is 6.

### Example 2
- **Input:** `grid = [[6,7],[5,8]]`
- **Output:** `9`
- **Explanation:** There are two valid paths: 

 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1)` with XOR: `6 XOR 7 XOR 8 = 9` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1)` with XOR: `6 XOR 5 XOR 8 = 11` 
 

 The minimum XOR value among all valid paths is 9.

### Example 3
- **Input:** `grid = [[2,7,5]]`
- **Output:** `0`
- **Explanation:** There is only one valid path: 

 
 `(0, 0) &rarr; (0, 1) &rarr; (0, 2)` with XOR: `2 XOR 7 XOR 5 = 0` 
 

 The XOR value of this path is 0, which is the minimum possible.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum XOR Path in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2],[3,4]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are two valid paths: 

 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1)` with XOR: `1 XOR 2 XOR 4 = 7` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1)` with XOR: `1 XOR 3 XOR 4 = 6` 
 

 The minimum XOR value among all valid paths is 6.

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
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if i > 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ grid[i][j])

                if j > 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ grid[i][j])

        return min(dp[m - 1][n - 1])
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [4100. Minimum Cost Path With Even XOR Parity](../../4001-4500/4431-minimum-cost-path-with-even-xor-parity/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)
