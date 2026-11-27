# LeetCode 3122: Minimum Number of Operations to Satisfy Conditions

**LeetCode Problem #3122 — Minimum Number of Operations to Satisfy Conditions**
Solve LeetCode Minimum Number of Operations to Satisfy Conditions using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Operations to Satisfy Conditions |
| LeetCode | #3122 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D matrix `grid` of size `m x n`. In one **operation**, you can change the value of **any** cell to **any** non-negative number. You need to perform some **operations** such that each cell `grid[i][j]` is:

Equal to the cell below it, i.e. `grid[i][j] == grid[i + 1][j]` (if it exists). 
 Different from the cell to its right, i.e. `grid[i][j] != grid[i][j + 1]` (if it exists).

Return the **minimum** number of operations needed.

## Constraints
- `1 <= n, m <= 1000`
- `0 <= grid[i][j] <= 9`

## Examples
### Example 1
- **Input:** `grid = [[1,0,2],[1,0,2]]`
- **Output:** `0`

### Example 2
- **Input:** `grid = [[1,1,1],[0,0,0]]`
- **Output:** `3`

### Example 3
- **Input:** `grid = [[1],[2],[3]]`
- **Output:** `2`
- **Explanation:** There is a single column. We can change the value to 1 in each cell using 2 operations.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Number of Operations to Satisfy Conditions**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,2],[1,0,2]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.

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
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        count = [[0] * 10 for _ in range(n)]
        for row in grid:
            for j, v in enumerate(row):
                count[j][v] += 1

        dp = [m - count[0][v] for v in range(10)]

        for j in range(1, n):
            nxt = [0] * 10
            for v in range(10):
                best = min(dp[u] for u in range(10) if u != v)
                nxt[v] = best + m - count[j][v]
            dp = nxt

        return min(dp)
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
- [1737. Change Minimum Characters to Satisfy One of Three Conditions](../../1501-2000/1737-change-minimum-characters-to-satisfy-one-of-three-conditions/)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1769-minimum-number-of-operations-to-move-all-balls-to-each-box/)
- [1775. Equal Sum Arrays With Minimum Number of Operations](../../1501-2000/1775-equal-sum-arrays-with-minimum-number-of-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/)
