# LeetCode 1595: Minimum Cost to Connect Two Groups of Points

**LeetCode Problem #1595 — Minimum Cost to Connect Two Groups of Points**
Solve LeetCode Minimum Cost to Connect Two Groups of Points using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Connect Two Groups of Points |
| LeetCode | #1595 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two groups of points where the first group has `size_1` points, the second group has `size_2` points, and `size_1 >= size_2`.

The `cost` of the connection between any two points are given in an `size_1 x size_2` matrix where `cost[i][j]` is the cost of connecting point `i` of the first group and point `j` of the second group. The groups are connected if **each point in both groups is connected to one or more points in the opposite group**. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

Return *the minimum cost it takes to connect the two groups*.

## Constraints
- `size_1 == cost.length`
- `size_2 == cost[i].length`
- `1 <= size_1, size_2 <= 12`
- `size_1 >= size_2`
- `0 <= cost[i][j] <= 100`

## Examples
### Example 1
- **Input:** `cost = [[15, 96], [36, 2]]`
- **Output:** `17`
- **Explanation:** : The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

### Example 2
- **Input:** `cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]`
- **Output:** `4`
- **Explanation:** : The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.

### Example 3
- **Input:** `cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]`
- **Output:** `10`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Cost to Connect Two Groups of Points**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cost = [[15, 96], [36, 2]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `17`.
4. **Verification:** : The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[][]} cost
 * @return {number}
 */
var connectTwoGroups = function (cost) {
  const n = cost.length;
  const m = cost[0].length;
  const size = 1 << m;

  const minCol = new Array(m).fill(Infinity);
  for (let i = 0; i < n; i++)
    for (let j = 0; j < m; j++) minCol[j] = Math.min(minCol[j], cost[i][j]);

  let dp = new Array(size).fill(Infinity);
  dp[0] = 0;

  for (let i = 0; i < n; i++) {
    const next = new Array(size).fill(Infinity);
    for (let mask = 0; mask < size; mask++) {
      if (dp[mask] === Infinity) continue;
      for (let j = 0; j < m; j++) {
        const nm = mask | (1 << j);
        next[nm] = Math.min(next[nm], dp[mask] + cost[i][j]);
      }
    }
    dp = next;
  }

  let ans = Infinity;
  for (let mask = 0; mask < size; mask++) {
    if (dp[mask] === Infinity) continue;
    let extra = 0;
    for (let j = 0; j < m; j++) {
      if (!(mask & (1 << j))) extra += minCol[j];
    }
    ans = Math.min(ans, dp[mask] + extra);
  }
  return ans;
};
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
- [1584. Min Cost to Connect All Points](../../1501-2000/1584-min-cost-to-connect-all-points/)
- [599. Minimum Index Sum of Two Lists](../../0501-1000/0599-minimum-index-sum-of-two-lists/)
- [712. Minimum ASCII Delete Sum for Two Strings](../../0501-1000/0712-minimum-ascii-delete-sum-for-two-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/)
