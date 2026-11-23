# LeetCode 1293: Shortest Path in a Grid with Obstacles Elimination

**LeetCode Problem #1293 — Shortest Path in a Grid with Obstacles Elimination**
Solve LeetCode Shortest Path in a Grid with Obstacles Elimination using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path in a Grid with Obstacles Elimination |
| LeetCode | #1293 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` integer matrix `grid` where each cell is either `0` (empty) or `1` (obstacle). You can move up, down, left, or right from and to an empty cell in **one step**.

Return *the minimum number of **steps** to walk from the upper left corner *`(0, 0)`* to the lower right corner *`(m - 1, n - 1)`* given that you can eliminate **at most** *`k`* obstacles*. If it is not possible to find such walk return `-1`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 40`
- `1 <= k <= m * n`
- `grid[i][j]` is either `0` **or** `1`.
- `grid[0][0] == grid[m - 1][n - 1] == 0`

## Examples
### Example 1
- **Input:** `grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1`
- **Output:** `6`
- **Explanation:** The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) ->

### Example 2
- **Input:** `grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1`
- **Output:** `-1`
- **Explanation:** We need to eliminate at least two obstacles to find such a walk.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Path in a Grid with Obstacles Elimination**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) ->

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
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 3:
            return m + n - 2

        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
        visited[0][0][0] = True
        q = deque([(0, 0, 0, 0)])  # (r, c, obstacles used, steps)

        while q:
            r, c, used, d = q.popleft()
            if r == m - 1 and c == n - 1:
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nu = used + grid[nr][nc]
                    if nu <= k and not visited[nr][nc][nu]:
                        visited[nr][nc][nu] = True
                        q.append((nr, nc, nu, d + 1))
        return -1
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [1391. Check if There is a Valid Path in a Grid](../../1501-2000/1507-check-if-there-is-a-valid-path-in-a-grid/)
- [2812. Find the Safest Path in a Grid](../../2501-3000/2914-find-the-safest-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)
