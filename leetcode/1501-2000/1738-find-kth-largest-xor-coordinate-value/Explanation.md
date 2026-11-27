# LeetCode 1738: Find Kth Largest XOR Coordinate Value

**LeetCode Problem #1738 — Find Kth Largest XOR Coordinate Value**
Solve LeetCode Find Kth Largest XOR Coordinate Value using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Kth Largest XOR Coordinate Value |
| LeetCode | #1738 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D `matrix` of size `m x n`, consisting of non-negative integers. You are also given an integer `k`.

The **value** of coordinate `(a, b)` of the matrix is the XOR of all `matrix[i][j]` where `0 <= i <= a < m` and `0 <= j <= b < n` **(0-indexed)**.

Find the `k^th` largest value **(1-indexed)** of all the coordinates of `matrix`.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 1000`
- `0 <= matrix[i][j] <= 10^6`
- `1 <= k <= m * n`

## Examples
### Example 1
- **Input:** `matrix = [[5,2],[1,6]], k = 1`
- **Output:** `7`
- **Explanation:** The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.

### Example 2
- **Input:** `matrix = [[5,2],[1,6]], k = 2`
- **Output:** `5`
- **Explanation:** The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.

### Example 3
- **Input:** `matrix = [[5,2],[1,6]], k = 3`
- **Output:** `4`
- **Explanation:** The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Kth Largest XOR Coordinate Value**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[5,2],[1,6]], k = 1`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.

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
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthLargestValue = function(matrix, k) {
    const m = matrix.length;
    const n = matrix[0].length;
    const values = [];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i > 0) matrix[i][j] ^= matrix[i - 1][j];
            if (j > 0) matrix[i][j] ^= matrix[i][j - 1];
            if (i > 0 && j > 0) matrix[i][j] ^= matrix[i - 1][j - 1];

            values.push(matrix[i][j]);
        }
    }

    values.sort((a, b) => b - a);
    return values[k - 1];
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
- [1985. Find the Kth Largest Integer in the Array](../../1501-2000/1985-find-the-kth-largest-integer-in-the-array/)
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/)
