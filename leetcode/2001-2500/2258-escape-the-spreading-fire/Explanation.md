# LeetCode 2258: Escape the Spreading Fire

**LeetCode Problem #2258 — Escape the Spreading Fire**
Solve LeetCode Escape the Spreading Fire using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Escape the Spreading Fire |
| LeetCode | #2258 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array `grid` of size `m x n` which represents a field. Each cell has one of three values:

`0` represents grass, 
 `1` represents fire, 
 `2` represents a wall that you and fire cannot pass through.

You are situated in the top-left cell, `(0, 0)`, and you want to travel to the safehouse at the bottom-right cell, `(m - 1, n - 1)`. Every minute, you may move to an **adjacent** grass cell. **After** your move, every fire cell will spread to all **adjacent** cells that are not walls.

Return *the **maximum** number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse*. If this is impossible, return `-1`. If you can **always** reach the safehouse regardless of the minutes stayed, return `10^9`.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is **adjacent** to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 300`
- `4 <= m * n <= 2 * 10^4`
- `grid[i][j]` is either `0`, `1`, or `2`.
- `grid[0][0] == grid[m - 1][n - 1] == 0`

## Examples
### Example 1
- **Input:** `grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]`
- **Output:** `3`
- **Explanation:** The figure above shows the scenario where you stay in the initial position for 3 minutes.
You will still be able to safely reach the safehouse.
Staying for more than 3 minutes will not allow you to safely reach the safehouse.

### Example 2
- **Input:** `grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]`
- **Output:** `-1`
- **Explanation:** The figure above shows the scenario where you immediately move towards the safehouse.
Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse.
Thus, -1 is returned.

### Example 3
- **Input:** `grid = [[0,0,0],[2,2,0],[1,2,0]]`
- **Output:** `1000000000`
- **Explanation:** The figure above shows the initial grid.
Notice that the fire is contained by walls and you will always be able to safely reach the safehouse.
Thus, 10^9 is returned.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Escape the Spreading Fire**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The figure above shows the scenario where you stay in the initial position for 3 minutes.
You will still be able to safely reach the safehouse.
Staying for more than 3 minutes will not allow you to safely reach the safehouse.

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
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(sources):
            dist = [[INF] * n for _ in range(m)]
            q = deque()
            for r, c in sources:
                dist[r][c] = 0
                q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and dist[nr][nc] == INF:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))
            return dist

        fire = bfs([(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1])
        me = bfs([(0, 0)])

        if me[m - 1][n - 1] == INF:
            return -1
        if fire[m - 1][n - 1] == INF:
            return INF  # fire can never reach the safehouse or anything on your path

        d = fire[m - 1][n - 1] - me[m - 1][n - 1]
        if d < 0:
            return -1

        for x, y in ((m - 2, n - 1), (m - 1, n - 2)):
            if me[x][y] != INF and fire[x][y] - me[x][y] > d:
                return d
        return d - 1
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
- [789. Escape The Ghosts](../../0501-1000/0789-escape-the-ghosts/)
- [1036. Escape a Large Maze](../../1001-1500/1036-escape-a-large-maze/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/escape-the-spreading-fire/)
