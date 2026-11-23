# LeetCode 566: Reshape the Matrix

**LeetCode Problem #566 — Reshape the Matrix**
Solve LeetCode Reshape the Matrix using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reshape the Matrix |
| LeetCode | #566 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
In MATLAB, there is a handy function called `reshape` which can reshape an `m x n` matrix into a new one with a different size `r x c` keeping its original data.

You are given an `m x n` matrix `mat` and two integers `r` and `c` representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the `reshape` operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `-1000 <= mat[i][j] <= 1000`
- `1 <= r, c <= 300`

## Examples
### Example 1
- **Input:** `mat = [[1,2],[3,4]], r = 1, c = 4`
- **Output:** `[[1,2,3,4]]`

### Example 2
- **Input:** `mat = [[1,2],[3,4]], r = 2, c = 4`
- **Output:** `[[1,2],[3,4]]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reshape the Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,2],[3,4]], r = 1, c = 4`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,3,4]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        # Reshape is impossible
        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                index = i * n + j

                new_row = index // c
                new_col = index % c

                result[new_row][new_col] = mat[i][j]

        return result
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
- [2888. Reshape Data: Concatenate](../../3001-3500/3064-reshape-data-concatenate/)
- [2889. Reshape Data: Pivot](../../3001-3500/3072-reshape-data-pivot/)
- [2890. Reshape Data: Melt](../../3001-3500/3073-reshape-data-melt/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reshape-the-matrix/)
