# LeetCode 2684: Maximum Number of Moves in a Grid

**LeetCode Problem #2684 — Maximum Number of Moves in a Grid**
Solve LeetCode Maximum Number of Moves in a Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Moves in a Grid |
| LeetCode | #2684 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** `m x n` matrix `grid` consisting of **positive** integers.

You can start at **any** cell in the first column of the matrix, and traverse the grid in the following way:

From a cell `(row, col)`, you can move to any of the cells: `(row - 1, col + 1)`, `(row, col + 1)` and `(row + 1, col + 1)` such that the value of the cell you move to, should be **strictly** bigger than the value of the current cell.

Return *the **maximum** number of **moves** that you can perform.*

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10^5`
- `1 <= grid[i][j] <= 10^6`

## Examples
### Example 1
- **Input:** `grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]`
- **Output:** `3`
- **Explanation:** We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.

### Example 2
- **Input:** `grid = [[3,2,4],[2,1,9],[1,1,7]]`
- **Output:** `0`
- **Explanation:** Starting from any cell in the first column we cannot perform any moves.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Moves in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.

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
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reach = [True] * m  # reachable rows in the current column

        for c in range(n - 1):
            nxt = [False] * m
            for r in range(m):
                if not reach[r]:
                    continue
                for nr in (r - 1, r, r + 1):
                    if 0 <= nr < m and grid[nr][c + 1] > grid[r][c]:
                        nxt[nr] = True
            if not any(nxt):
                return c
            reach = nxt

        return n - 1
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
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2503-maximum-number-of-points-from-grid-queries/)
- [2658. Maximum Number of Fish in a Grid](../../2501-3000/2658-maximum-number-of-fish-in-a-grid/)
- [3283. Maximum Number of Moves to Kill All Pawns](../../3001-3500/3283-maximum-number-of-moves-to-kill-all-pawns/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/)
