# LeetCode 1277: Count Square Submatrices with All Ones

**LeetCode Problem #1277 — Count Square Submatrices with All Ones**
Solve LeetCode Count Square Submatrices with All Ones using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Square Submatrices with All Ones |
| LeetCode | #1277 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
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
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

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
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** There are

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

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
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1504. Count Submatrices With All Ones](../../1501-2000/1504-count-submatrices-with-all-ones/)
- [3070. Count Submatrices with Top-Left Element and Sum Less Than k](../../3001-3500/3070-count-submatrices-with-top-left-element-and-sum-less-than-k/)
- [3212. Count Submatrices With Equal Frequency of X and Y](../../3001-3500/3212-count-submatrices-with-equal-frequency-of-x-and-y/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
