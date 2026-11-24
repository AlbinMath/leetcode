# LeetCode 2946: Matrix Similarity After Cyclic Shifts

**LeetCode Problem #2946 — Matrix Similarity After Cyclic Shifts**
Solve LeetCode Matrix Similarity After Cyclic Shifts using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Matrix Similarity After Cyclic Shifts |
| LeetCode | #2946 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` integer matrix `mat` and an integer `k`. The matrix rows are 0-indexed.

The following process happens `k` times:

**Even-indexed** rows (0, 2, 4, ...) are cyclically shifted to the left.

**Odd-indexed** rows (1, 3, 5, ...) are cyclically shifted to the right.

Return `true` if the final modified matrix after `k` steps is identical to the original matrix, and `false` otherwise.

## Constraints
- `1 <= mat.length <= 25`
- `1 <= mat[i].length <= 25`
- `1 <= mat[i][j] <= 25`
- `1 <= k <= 50`

## Examples
### Example 1
- **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4`
- **Output:** `false`
- **Explanation:** In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).

### Example 2
- **Input:** `mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2`
- **Output:** `true`

### Example 3
- **Input:** `mat = [[2,2],[2,2]], k = 3`
- **Output:** `true`
- **Explanation:** As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Matrix Similarity After Cyclic Shifts**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).

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
var areSimilar = function(mat, k) {
    const n = mat[0].length;
    const shift = k % n;

    if (shift === 0) return true;

    for (const row of mat) {
        for (let j = 0; j < n; j++) {
            if (row[j] !== row[(j + shift) % n]) {
                return false;
            }
        }
    }

    return true;
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
- [861. Score After Flipping Matrix](../../0501-1000/0891-score-after-flipping-matrix/)
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [957. Prison Cells After N Days](../../0501-1000/0994-prison-cells-after-n-days/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/)
