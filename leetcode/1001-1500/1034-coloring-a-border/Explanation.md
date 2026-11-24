# LeetCode 1034: Coloring A Border

**LeetCode Problem #1034 — Coloring A Border**
Solve LeetCode Coloring A Border using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Coloring A Border |
| LeetCode | #1034 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` integer matrix `grid`, and three integers `row`, `col`, and `color`. Each value in the grid represents the color of the grid square at that location.

Two squares are called **adjacent** if they are next to each other in any of the 4 directions.

Two squares belong to the same **connected component** if they have the same color and they are adjacent.

The **border of a connected component** is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the **border** of the **connected component** that contains the square `grid[row][col]` with `color`.

Return *the final grid*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j], color <= 1000`
- `0 <= row < m`
- `0 <= col < n`

## Examples
### Example 1
- **Input:** `grid = [[1,1],[1,2]], row = 0, col = 0, color = 3`
- **Output:** `[[3,3],[3,2]]`

### Example 2
- **Input:** `grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3`
- **Output:** `[[1,3,3],[2,3,3]]`

### Example 3
- **Input:** `grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2`
- **Output:** `[[2,2,2],[2,1,2],[2,2,2]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Coloring A Border**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,1],[1,2]], row = 0, col = 0, color = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[3,3],[3,2]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        orig = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        border = []

        stack = [(row, col)]
        visited[row][col] = True
        while stack:
            r, c = stack.pop()
            is_border = False
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != orig:
                    is_border = True
                elif not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
            if is_border:
                border.append((r, c))

        for r, c in border:
            grid[r][c] = color
        return grid
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1145. Binary Tree Coloring Game](../../1001-1500/1145-binary-tree-coloring-game/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/coloring-a-border/)
