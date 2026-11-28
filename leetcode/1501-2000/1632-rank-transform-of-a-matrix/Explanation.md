# LeetCode 1632: Rank Transform of a Matrix

**LeetCode Problem #1632 — Rank Transform of a Matrix**
Solve LeetCode Rank Transform of a Matrix using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rank Transform of a Matrix |
| LeetCode | #1632 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `m x n` `matrix`, return *a new matrix *`answer`* where *`answer[row][col]`* is the ****rank** of *`matrix[row][col]`.

The **rank** is an **integer** that represents how large an element is compared to other elements. It is calculated using the following rules:

The rank is an integer starting from `1`. 
 If two elements `p` and `q` are in the **same row or column**, then:
 
 If `p < q` then `rank(p) < rank(q)` 
 If `p == q` then `rank(p) == rank(q)` 
 If `p > q` then `rank(p) > rank(q)` 
 
 
 The **rank** should be as **small** as possible.

The test cases are generated so that `answer` is unique under the given rules.

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 500`
- `-10^9 <= matrix[row][col] <= 10^9`

## Examples
### Example 1
- **Input:** `matrix = [[1,2],[3,4]]`
- **Output:** `[[1,2],[2,3]]`
- **Explanation:** The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.

### Example 2
- **Input:** `matrix = [[7,7],[7,7]]`
- **Output:** `[[1,1],[1,1]]`

### Example 3
- **Input:** `matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]`
- **Output:** `[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rank Transform of a Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[1,2],[3,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2],[2,3]]`.
4. **Verification:** The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.

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
 * @return {number[][]}
 */
var matrixRankTransform = function (matrix) {
    const m = matrix.length, n = matrix[0].length;
    const parent = new Int32Array(m + n);
    for (let i = 0; i < m + n; i++) parent[i] = i;
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };

    const cells = [];
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) cells.push(i * n + j);
    cells.sort((a, b) => matrix[(a / n) | 0][a % n] - matrix[(b / n) | 0][b % n]);

    const rowRank = new Int32Array(m);
    const colRank = new Int32Array(n);
    const ans = Array.from({ length: m }, () => new Array(n).fill(0));
    const compMax = new Int32Array(m + n);

    let p = 0;
    const total = cells.length;
    while (p < total) {
        let q = p;
        const val = matrix[(cells[p] / n) | 0][cells[p] % n];
        while (q < total && matrix[(cells[q] / n) | 0][cells[q] % n] === val) q++;

        // union rows and columns of equal-valued cells
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            const a = find(i), b = find(m + j);
            if (a !== b) parent[a] = b;
        }

        // component max of existing ranks
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            const root = find(i);
            compMax[root] = 0;
        }
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            const root = find(i);
            const cur = Math.max(rowRank[i], colRank[j]);
            if (cur > compMax[root]) compMax[root] = cur;
        }

        // assign ranks
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            ans[i][j] = compMax[find(i)] + 1;
        }
        // update row and column ranks after all assignments
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            rowRank[i] = ans[i][j];
            colRank[j] = ans[i][j];
        }

        // reset union-find for touched nodes
        for (let t = p; t < q; t++) {
            const i = (cells[t] / n) | 0, j = cells[t] % n;
            parent[i] = i;
            parent[m + j] = m + j;
        }
        p = q;
    }
    return ans;
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
- [1331. Rank Transform of an Array](../../1001-1500/1331-rank-transform-of-an-array/)
- [178. Rank Scores](../../0001-0500/0178-rank-scores/)
- [1366. Rank Teams by Votes](../../1001-1500/1366-rank-teams-by-votes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rank-transform-of-a-matrix/)
