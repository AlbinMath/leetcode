# LeetCode 2245: Maximum Trailing Zeros in a Cornered Path

**LeetCode Problem #2245 — Maximum Trailing Zeros in a Cornered Path**
Solve LeetCode Maximum Trailing Zeros in a Cornered Path using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Trailing Zeros in a Cornered Path |
| LeetCode | #2245 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `grid` of size `m x n`, where each cell contains a positive integer.

A **cornered path** is defined as a set of adjacent cells with **at most** one turn. More specifically, the path should exclusively move either **horizontally** or **vertically** up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the **alternate** direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.

The **product** of a path is defined as the product of all the values in the path.

Return *the **maximum** number of **trailing zeros** in the product of a cornered path found in *`grid`.

**Horizontal** movement means moving in either the left or right direction. 
 **Vertical** movement means moving in either the up or down direction.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `1 <= grid[i][j] <= 1000`

## Examples
### Example 1
- **Input:** `grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]`
- **Output:** `3`
- **Explanation:** The grid on the left shows a valid cornered path.
It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
It can be shown that this is the maximum trailing zeros in the product of a cornered path.

The grid in the middle is not a cornered path as it has more than one turn.
The grid on the right is not a cornered path as it requires a return to a previously visited cell.

### Example 2
- **Input:** `grid = [[4,3,2],[7,6,1],[8,8,8]]`
- **Output:** `0`
- **Explanation:** The grid is shown in the figure above.
There are no cornered paths in the grid that result in a product with a trailing zero.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Trailing Zeros in a Cornered Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The grid on the left shows a valid cornered path.
It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
It can be shown that this is the maximum trailing zeros in the product of a cornered path.

The grid in the middle is not a cornered path as it has more than one turn.
The grid on the right is not a cornered path as it requires a return to a previously visited cell.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def factor(v, p):
            c = 0
            while v % p == 0:
                v //= p
                c += 1
            return c

        t = [[factor(v, 2) for v in row] for row in grid]
        f = [[factor(v, 5) for v in row] for row in grid]

        def build(a):
            row = [[0] * n for _ in range(m)]
            col = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    row[i][j] = a[i][j] + (row[i][j - 1] if j else 0)
                    col[i][j] = a[i][j] + (col[i - 1][j] if i else 0)
            return row, col

        rt, ct = build(t)
        rf, cf = build(f)

        res = 0
        for i in range(m):
            for j in range(n):
                c2, c5 = t[i][j], f[i][j]
                # (horizontal arm, vertical arm) options for 2s
                L2 = rt[i][j]
                R2 = rt[i][n - 1] - rt[i][j] + c2
                U2 = ct[i][j]
                D2 = ct[m - 1][j] - ct[i][j] + c2
                L5 = rf[i][j]
                R5 = rf[i][n - 1] - rf[i][j] + c5
                U5 = cf[i][j]
                D5 = cf[m - 1][j] - cf[i][j] + c5

                for H2, H5 in ((L2, L5), (R2, R5)):
                    for V2, V5 in ((U2, U5), (D2, D5)):
                        res = max(res, min(H2 + V2 - c2, H5 + V5 - c5))
        return res
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [1219. Path with Maximum Gold](../../1001-1500/1219-path-with-maximum-gold/)
- [1514. Path with Maximum Probability](../../1501-2000/1514-path-with-maximum-probability/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/)
