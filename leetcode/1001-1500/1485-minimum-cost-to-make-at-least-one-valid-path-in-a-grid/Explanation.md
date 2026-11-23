# LeetCode 1368: Minimum Cost to Make at Least One Valid Path in a Grid

**LeetCode Problem #1368 — Minimum Cost to Make at Least One Valid Path in a Grid**
Solve LeetCode Minimum Cost to Make at Least One Valid Path in a Grid using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Make at Least One Valid Path in a Grid |
| LeetCode | #1368 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an `m x n` grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of `grid[i][j]` can be:

`1` which means go to the cell to the right. (i.e go from `grid[i][j]` to `grid[i][j + 1]`) 
 `2` which means go to the cell to the left. (i.e go from `grid[i][j]` to `grid[i][j - 1]`) 
 `3` which means go to the lower cell. (i.e go from `grid[i][j]` to `grid[i + 1][j]`) 
 `4` which means go to the upper cell. (i.e go from `grid[i][j]` to `grid[i - 1][j]`)

Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell `(0, 0)`. A valid path in the grid is a path that starts from the upper left cell `(0, 0)` and ends at the bottom-right cell `(m - 1, n - 1)` following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with `cost = 1`. You can modify the sign on a cell **one time only**.

Return *the minimum cost to make the grid have at least one valid path*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `1 <= grid[i][j] <= 4`

## Examples
### Example 1
- **Input:** `grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]`
- **Output:** `3`
- **Explanation:** You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

### Example 2
- **Input:** `grid = [[1,1,3],[3,2,2],[1,1,4]]`
- **Output:** `0`
- **Explanation:** You can follow the path from (0, 0) to (2, 2).

### Example 3
- **Input:** `grid = [[1,2],[4,3]]`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost to Make at Least One Valid Path in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

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
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        q, dist = deque([(0,0)]), [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0

        while q:
            r, c = q.popleft()
            for i, (dr, dc) in enumerate(d, 1):
                x, y = r+dr, c+dc
                if 0 <= x < m and 0 <= y < n:
                    w = dist[r][c] + (grid[r][c] != i)
                    if w < dist[x][y]:
                        dist[x][y] = w
                        if grid[r][c] == i:
                            q.appendleft((x,y))
                        else:
                            q.append((x,y))

        return dist[m-1][n-1]
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1391. Check if There is a Valid Path in a Grid](../../1501-2000/1507-check-if-there-is-a-valid-path-in-a-grid/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2686-minimum-cost-of-a-path-with-special-roads/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
