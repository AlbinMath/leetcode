# LeetCode 931: Minimum Falling Path Sum

**LeetCode Problem #931 — Minimum Falling Path Sum**
Solve LeetCode Minimum Falling Path Sum using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Falling Path Sum |
| LeetCode | #931 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any **falling path** through* `matrix`.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

## Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `-100 <= matrix[i][j] <= 100`

## Examples
### Example 1
- **Input:** `matrix = [[2,1,3],[6,5,4],[7,8,9]]`
- **Output:** `13`
- **Explanation:** There are two falling paths with a minimum sum as shown.

### Example 2
- **Input:** `matrix = [[-19,57],[-40,-5]]`
- **Output:** `-59`
- **Explanation:** The falling path with a minimum sum is shown.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Falling Path Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[2,1,3],[6,5,4],[7,8,9]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** There are two falling paths with a minimum sum as shown.

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
var minFallingPathSum = function(matrix) {
    const n = matrix.length;
    let dp = [...matrix[0]];

    for (let r = 1; r < n; r++) {
        const nextDp = new Array(n);
        for (let c = 0; c < n; c++) {
            let bestPrev = dp[c];
            if (c > 0 && dp[c - 1] < bestPrev) bestPrev = dp[c - 1];
            if (c + 1 < n && dp[c + 1] < bestPrev) bestPrev = dp[c + 1];
            nextDp[c] = matrix[r][c] + bestPrev;
        }
        dp = nextDp;
    }

    return Math.min(...dp);
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
- [1289. Minimum Falling Path Sum II](../../1001-1500/1289-minimum-falling-path-sum-ii/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/)
