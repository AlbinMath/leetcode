# LeetCode 1314: Matrix Block Sum

**LeetCode Problem #1314 — Matrix Block Sum**
Solve LeetCode Matrix Block Sum using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Matrix Block Sum |
| LeetCode | #1314 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `m x n` matrix `mat` and an integer `k`, return *a matrix* `answer` *where each* `answer[i][j]` *is the sum of all elements* `mat[r][c]` *for*:

`i - k <= r <= i + k,` 
 `j - k <= c <= j + k`, and 
 `(r, c)` is a valid position in the matrix.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n, k <= 100`
- `1 <= mat[i][j] <= 100`

## Examples
### Example 1
- **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
- **Output:** `[[12,21,16],[27,45,33],[24,39,28]]`

### Example 2
- **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2`
- **Output:** `[[45,45,45],[45,45,45],[45,45,45]]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Matrix Block Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[12,21,16],[27,45,33],[24,39,28]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var matrixBlockSum = function(mat, k) {
    const m = mat.length;
    const n = mat[0].length;
    const prefix = Array.from({ length: m + 1 }, () => new Int32Array(n + 1));

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            prefix[r + 1][c + 1] =
                mat[r][c] +
                prefix[r][c + 1] +
                prefix[r + 1][c] -
                prefix[r][c];
        }
    }

    const answer = Array.from({ length: m }, () => new Array(n));
    for (let i = 0; i < m; i++) {
        const r1 = Math.max(0, i - k);
        const r2 = Math.min(m - 1, i + k);
        for (let j = 0; j < n; j++) {
            const c1 = Math.max(0, j - k);
            const c2 = Math.min(n - 1, j + k);
            answer[i][j] =
                prefix[r2 + 1][c2 + 1] -
                prefix[r1][c2 + 1] -
                prefix[r2 + 1][c1] +
                prefix[r1][c1];
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](../../1001-1500/1439-find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)
- [1572. Matrix Diagonal Sum](../../1501-2000/1572-matrix-diagonal-sum/)
- [1975. Maximum Matrix Sum](../../1501-2000/1975-maximum-matrix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/matrix-block-sum/)
