# LeetCode 1277: Count Square Submatrices with All Ones

**LeetCode Problem #1277 — Count Square Submatrices with All Ones**
Solve LeetCode Count Square Submatrices with All Ones using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Square Submatrices with All Ones |
| LeetCode | #1277 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `m * n` matrix of ones and zeros, return how many **square** submatrices have all ones.

## Constraints
- `1 <= arr.length <= 300`
- `1 <= arr[0].length <= 300`
- `0 <= arr[i][j] <= 1`

## Examples
### Example 1
- **Input:** `matrix =
[
 [0,1,1,1],
 [1,1,1,1],
 [0,1,1,1]
]`
- **Output:** `15`
- **Explanation:** There are

### Example 2
- **Input:** `matrix = 
[
 [1,0,1],
 [1,1,0],
 [1,1,0]
]`
- **Output:** `7`
- **Explanation:** There are 6 squares of side 1. 
There is

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count Square Submatrices with All Ones**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix =
[
 [0,1,1,1],
 [1,1,1,1],
 [0,1,1,1]
]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** There are

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
var countSquares = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const dp = new Int32Array(n);
    let totalSquares = 0;

    for (let r = 0; r < m; r++) {
        let prevDiag = 0; // Stores dp[r - 1][c - 1]
        for (let c = 0; c < n; c++) {
            const temp = dp[c]; // Save dp[r - 1][c] before overwriting
            if (matrix[r][c] === 1) {
                if (r === 0 || c === 0) {
                    dp[c] = 1;
                } else {
                    dp[c] = 1 + Math.min(dp[c], dp[c - 1], prevDiag);
                }
                totalSquares += dp[c];
            } else {
                dp[c] = 0;
            }
            prevDiag = temp;
        }
    }

    return totalSquares;
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
- [1504. Count Submatrices With All Ones](../../1501-2000/1504-count-submatrices-with-all-ones/)
- [3195. Find the Minimum Area to Cover All Ones I](../../3001-3500/3195-find-the-minimum-area-to-cover-all-ones-i/)
- [3197. Find the Minimum Area to Cover All Ones II](../../3001-3500/3197-find-the-minimum-area-to-cover-all-ones-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
