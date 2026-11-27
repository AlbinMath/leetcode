# LeetCode 3418: Maximum Amount of Money Robot Can Earn

**LeetCode Problem #3418 — Maximum Amount of Money Robot Can Earn**
Solve LeetCode Maximum Amount of Money Robot Can Earn using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Amount of Money Robot Can Earn |
| LeetCode | #3418 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` grid. A robot starts at the top-left corner of the grid `(0, 0)` and wants to reach the bottom-right corner `(m - 1, n - 1)`. The robot can move either right or down at any point in time.

The grid contains a value `coins[i][j]` in each cell:

If `coins[i][j] >= 0`, the robot gains that many coins. 
 If `coins[i][j] < 0`, the robot encounters a robber, and the robber steals the **absolute** value of `coins[i][j]` coins.

The robot has a special ability to **neutralize robbers** in at most **2 cells** on its path, preventing them from stealing coins in those cells.

**Note:** The robot's total coins can be negative.

Return the **maximum** profit the robot can gain on the route.

## Constraints
- `m == coins.length`
- `n == coins[i].length`
- `1 <= m, n <= 500`
- `-1000 <= coins[i][j] <= 1000`

## Examples
### Example 1
- **Input:** `coins = [[0,1,-1],[1,-2,3],[2,-3,4]]`
- **Output:** `8`
- **Explanation:** An optimal path for maximum coins is: 

 
 Start at `(0, 0)` with `0` coins (total coins = `0`). 
 Move to `(0, 1)`, gaining `1` coin (total coins = `0 + 1 = 1`). 
 Move to `(1, 1)`, where there's a robber stealing `2` coins. The robot uses one neutralization here, avoiding the robbery (total coins = `1`). 
 Move to `(1, 2)`, gaining `3` coins (total coins = `1 + 3 = 4`). 
 Move to `(2, 2)`, gaining `4` coins (total coins = `4 + 4 = 8`).

### Example 2
- **Input:** `coins = [[10,10,10],[10,10,10]]`
- **Output:** `40`
- **Explanation:** An optimal path for maximum coins is: 

 
 Start at `(0, 0)` with `10` coins (total coins = `10`). 
 Move to `(0, 1)`, gaining `10` coins (total coins = `10 + 10 = 20`). 
 Move to `(0, 2)`, gaining another `10` coins (total coins = `20 + 10 = 30`). 
 Move to `(1, 2)`, gaining the final `10` coins (total coins = `30 + 10 = 40`).

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Amount of Money Robot Can Earn**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coins = [[0,1,-1],[1,-2,3],[2,-3,4]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** An optimal path for maximum coins is: 

 
 Start at `(0, 0)` with `0` coins (total coins = `0`). 
 Move to `(0, 1)`, gaining `1` coin (total coins = `0 + 1 = 1`). 
 Move to `(1, 1)`, where there's a robber stealing `2` coins. The robot uses one neutralization here, avoiding the robbery (total coins = `1`). 
 Move to `(1, 2)`, gaining `3` coins (total coins = `1 + 3 = 4`). 
 Move to `(2, 2)`, gaining `4` coins (total coins = `4 + 4 = 8`).

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
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG = float('-inf')
        dp = [[[NEG] * 3 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                v = coins[i][j]
                if i == 0 and j == 0:
                    dp[0][0][0] = v
                    if v < 0:
                        dp[0][0][1] = 0
                    continue

                for k in range(3):
                    best = NEG
                    if i > 0:
                        best = max(best, dp[i - 1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k])
                    if best > NEG:
                        dp[i][j][k] = best + v

                    if v < 0 and k > 0:
                        best = NEG
                        if i > 0:
                            best = max(best, dp[i - 1][j][k - 1])
                        if j > 0:
                            best = max(best, dp[i][j - 1][k - 1])
                        if best > NEG:
                            dp[i][j][k] = max(dp[i][j][k], best)

        return max(dp[m - 1][n - 1])
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
- [3332. Maximum Points Tourist Can Earn](../../3001-3500/3332-maximum-points-tourist-can-earn/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1353. Maximum Number of Events That Can Be Attended](../../1001-1500/1353-maximum-number-of-events-that-can-be-attended/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/)
