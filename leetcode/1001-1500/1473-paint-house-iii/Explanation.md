# LeetCode 1473: Paint House III

**LeetCode Problem #1473 — Paint House III**
Solve LeetCode Paint House III using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Paint House III |
| LeetCode | #1473 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a row of `m` houses in a small city, each house must be painted with one of the `n` colors (labeled from `1` to `n`), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: `houses = [1,2,2,3,3,2,1,1]` contains `5` neighborhoods `[{1}, {2,2}, {3,3}, {2}, {1,1}]`.

Given an array `houses`, an `m x n` matrix `cost` and an integer `target` where:

`houses[i]`: is the color of the house `i`, and `0` if the house is not painted yet. 
 `cost[i][j]`: is the cost of paint the house `i` with the color `j + 1`.

Return *the minimum cost of painting all the remaining houses in such a way that there are exactly* `target` *neighborhoods*. If it is not possible, return `-1`.

## Constraints
- `m == houses.length == cost.length`
- `n == cost[i].length`
- `1 <= m <= 100`
- `1 <= n <= 20`
- `1 <= target <= m`
- `0 <= houses[i] <= n`
- `1 <= cost[i][j] <= 10^4`

## Examples
### Example 1
- **Input:** `houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- **Output:** `9`
- **Explanation:** Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

### Example 2
- **Input:** `houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- **Output:** `11`
- **Explanation:** Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

### Example 3
- **Input:** `houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3`
- **Output:** `-1`
- **Explanation:** Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Paint House III**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

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
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(target + 1)]
        
        if houses[0] != 0:
            dp[1][houses[0]] = 0
        else:
            for c in range(1, n + 1):
                dp[1][c] = cost[0][c - 1]
                
        for i in range(1, m):
            next_dp = [[INF] * (n + 1) for _ in range(target + 1)]
            max_k = min(i + 1, target)
            
            for k in range(1, max_k + 1):
                min1 = min2 = INF
                min1_color = -1
                if k > 1:
                    for c in range(1, n + 1):
                        val = dp[k - 1][c]
                        if val < min1:
                            min2 = min1
                            min1 = val
                            min1_color = c
                        elif val < min2:
                            min2 = val
                            
                colors = [houses[i]] if houses[i] != 0 else range(1, n + 1)
                
                for c in colors:
                    paint_cost = 0 if houses[i] != 0 else cost[i][c - 1]
                    
                    best_prev = dp[k][c]
                    
                    if k > 1:
                        diff_color_cost = min2 if c == min1_color else min1
                        if diff_color_cost < best_prev:
                            best_prev = diff_color_cost
                            
                    if best_prev < INF:
                        next_dp[k][c] = paint_cost + best_prev
                        
            dp = next_dp
            
        ans = min(dp[target][1:])
        return ans if ans < INF else -1
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
- [198. House Robber](../../0001-0500/0198-house-robber/)
- [213. House Robber II](../../0001-0500/0213-house-robber-ii/)
- [337. House Robber III](../../0001-0500/0337-house-robber-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/paint-house-iii/)
