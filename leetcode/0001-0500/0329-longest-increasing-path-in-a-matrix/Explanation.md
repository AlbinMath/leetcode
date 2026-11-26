# LeetCode 329: Longest Increasing Path in a Matrix

**LeetCode Problem #329 — Longest Increasing Path in a Matrix**
Solve LeetCode Longest Increasing Path in a Matrix using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Increasing Path in a Matrix |
| LeetCode | #329 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `m x n` integers `matrix`, return *the length of the longest increasing path in *`matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `matrix = [[9,9,4],[6,6,8],[2,1,1]]`
- **Output:** `4`
- **Explanation:** The longest increasing path is `[1, 2, 6, 9]`.

### Example 2
- **Input:** `matrix = [[3,4,5],[3,2,6],[2,2,1]]`
- **Output:** `4`
- **Explanation:** The longest increasing path is `[3, 4, 5, 6]`. Moving diagonally is not allowed.

### Example 3
- **Input:** `matrix = [[1]]`
- **Output:** `1`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Increasing Path in a Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[9,9,4],[6,6,8],[2,1,1]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The longest increasing path is `[1, 2, 6, 9]`.

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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cells = sorted(((matrix[i][j], i, j) for i in range(m) for j in range(n)),
                       reverse=True)
        L = [[1] * n for _ in range(m)]
        best = 1
        for v, i, j in cells:
            cur = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > v:
                    if L[x][y] + 1 > cur:
                        cur = L[x][y] + 1
            L[i][j] = cur
            if cur > best:
                best = cur
        return best
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
- [3288. Length of the Longest Increasing Path](../../3001-3500/3288-length-of-the-longest-increasing-path/)
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [673. Number of Longest Increasing Subsequence](../../0501-1000/0673-number-of-longest-increasing-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
