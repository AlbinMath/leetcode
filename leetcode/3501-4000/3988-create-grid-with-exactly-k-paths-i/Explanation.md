# LeetCode 3988: Create Grid With Exactly K Paths I

**LeetCode Problem #3988 — Create Grid With Exactly K Paths I**
Solve LeetCode Create Grid With Exactly K Paths I using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Grid With Exactly K Paths I |
| LeetCode | #3988 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given three integers `m`, `n`, and `k`.

Construct **any** `m x n` grid consisting only of the characters `'.'` and `'#'`, where:

`'.'` represents a free cell. 
 `'#'` represents an obstacle cell.

A **valid path** is a sequence of free cells that:

Starts at the top-left cell `(0, 0)`. 
 Ends at the bottom-right cell `(m - 1, n - 1)`. 
 Moves only:
 
 Right, from `(i, j)` to `(i, j + 1)`, or 
 Down, from `(i, j)` to `(i + 1, j)`.

Return any grid such that there are **exactly** `k` **valid paths** from the top-left cell to the bottom-right cell. If no such grid exists, return an empty array.

## Constraints
- `1 <= m, n <= 10`
- `1 <= k <= 4`

## Examples
### Example 1
- **Input:** `m = 2, n = 3, k = 2`
- **Output:** `["...","#.."]`
- **Explanation:** There are exactly `k = 2` valid paths from `(0, 0)` to `(1, 2)`: 

 
 `(0, 0) &rarr; (0, 1) &rarr; (0, 2) &rarr; (1, 2)` 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (1, 2)`

### Example 2
- **Input:** `m = 3, n = 3, k = 4`
- **Output:** `["..#","...","#.."]`
- **Explanation:** There are exactly `k = 4` valid paths from `(0, 0)` to `(2, 2)`: 

 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2)` 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2)` 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (2, 1) &rarr; (2, 2)`

### Example 3
- **Input:** `m = 1, n = 4, k = 2`
- **Output:** `[]`
- **Explanation:** ​ 

 No grid exists with exactly `k = 2` valid paths for a `1 x 4` grid, so the answer is an empty array.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Create Grid With Exactly K Paths I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 2, n = 3, k = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["...","#.."]`.
4. **Verification:** There are exactly `k = 2` valid paths from `(0, 0)` to `(1, 2)`: 

 
 `(0, 0) &rarr; (0, 1) &rarr; (0, 2) &rarr; (1, 2)` 
 `(0, 0) &rarr; (0, 1) &rarr; (1, 1) &rarr; (1, 2)`

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
from typing import List

class Solution:
    def createGrid(self, m: int, n: int, k: int) -> List[str]:
        # Single row or column: exactly one path if all free
        if m == 1 or n == 1:
            if k == 1:
                return ["." * n for _ in range(m)]
            return []

        # Row-based construction: k <= n
        if k <= n:
            g = [['#'] * n for _ in range(m)]
            for j in range(n):
                g[0][j] = '.'
            for i in range(m):
                g[i][n - 1] = '.'
            for j in range(n - k, n):
                g[1][j] = '.'
            return ["".join(r) for r in g]

        # Column-based construction: k <= m
        if k <= m:
            g = [['#'] * n for _ in range(m)]
            for i in range(m):
                g[i][0] = '.'
            for j in range(n):
                g[m - 1][j] = '.'
            for i in range(m - k, m):
                g[i][1] = '.'
            return ["".join(r) for r in g]

        # Remaining: k > n and k > m  -> only 3x3 with k = 4 works
        if m == 3 and n == 3 and k == 4:
            return ["..#", "...", "#.."]
        return []
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
- [3963. Create Grid With Exactly One Path](../../3501-4000/3963-create-grid-with-exactly-one-path/)
- [2328. Number of Increasing Paths in a Grid](../../2001-2500/2328-number-of-increasing-paths-in-a-grid/)
- [2435. Paths in Matrix Whose Sum Is Divisible by K](../../2001-2500/2435-paths-in-matrix-whose-sum-is-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/)
