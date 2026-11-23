# LeetCode 2290: Minimum Obstacle Removal to Reach Corner

**LeetCode Problem #2290 — Minimum Obstacle Removal to Reach Corner**
Solve LeetCode Minimum Obstacle Removal to Reach Corner using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Obstacle Removal to Reach Corner |
| LeetCode | #2290 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array `grid` of size `m x n`. Each cell has one of two values:

`0` represents an **empty** cell, 
 `1` represents an **obstacle** that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return *the **minimum** number of **obstacles** to **remove** so you can move from the upper left corner *`(0, 0)`* to the lower right corner *`(m - 1, n - 1)`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- `grid[i][j]` is either `0` **or** `1`.
- `grid[0][0] == grid[m - 1][n - 1] == 0`

## Examples
### Example 1
- **Input:** `grid = [[0,1,1],[1,1,0],[1,1,0]]`
- **Output:** `2`
- **Explanation:** We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

### Example 2
- **Input:** `grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]`
- **Output:** `0`
- **Explanation:** We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Obstacle Removal to Reach Corner**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1,1],[1,1,0],[1,1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

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
from collections import deque

class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        d = [[float('inf')]*n for _ in range(m)]
        d[0][0] = 0
        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                x, y = r+dr, c+dc
                if 0 <= x < m and 0 <= y < n:
                    w = d[r][c] + grid[x][y]
                    if w < d[x][y]:
                        d[x][y] = w
                        if grid[x][y]:
                            q.append((x,y))
                        else:
                            q.appendleft((x,y))

        return d[m-1][n-1]
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
- [1210. Minimum Moves to Reach Target with Rotations](../../1001-1500/1322-minimum-moves-to-reach-target-with-rotations/)
- [1557. Minimum Number of Vertices to Reach All Nodes](../../1501-2000/1661-minimum-number-of-vertices-to-reach-all-nodes/)
- [1654. Minimum Jumps to Reach Home](../../1501-2000/1757-minimum-jumps-to-reach-home/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/)
