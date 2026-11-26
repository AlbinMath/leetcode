# LeetCode 1391: Check if There is a Valid Path in a Grid

**LeetCode Problem #1391 — Check if There is a Valid Path in a Grid**
Solve LeetCode Check if There is a Valid Path in a Grid using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if There is a Valid Path in a Grid |
| LeetCode | #1391 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` `grid`. Each cell of `grid` represents a street. The street of `grid[i][j]` can be:

`1` which means a street connecting the left cell and the right cell. 
 `2` which means a street connecting the upper cell and the lower cell. 
 `3` which means a street connecting the left cell and the lower cell. 
 `4` which means a street connecting the right cell and the lower cell. 
 `5` which means a street connecting the left cell and the upper cell. 
 `6` which means a street connecting the right cell and the upper cell. 
 
 
 You will initially start at the street of the upper-left cell `(0, 0)`. A valid path in the grid is a path that starts from the upper left cell `(0, 0)` and ends at the bottom-right cell `(m - 1, n - 1)`. **The path should only follow the streets**.

**Notice** that you are **not allowed** to change any street.

Return `true`* if there is a valid path in the grid or *`false`* otherwise*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `1 <= grid[i][j] <= 6`

## Examples
### Example 1
- **Input:** `grid = [[2,4,3],[6,5,2]]`
- **Output:** `true`
- **Explanation:** As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

### Example 2
- **Input:** `grid = [[1,2,1],[1,2,1]]`
- **Output:** `false`
- **Explanation:** As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

### Example 3
- **Input:** `grid = [[1,1,2]]`
- **Output:** `false`
- **Explanation:** You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Check if There is a Valid Path in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[2,4,3],[6,5,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

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
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True

        # Mapping: direction -> (dr, dc, opposite_direction)
        dirs = {
            'U': (-1, 0, 'D'),
            'D': (1, 0, 'U'),
            'L': (0, -1, 'R'),
            'R': (0, 1, 'L')
        }

        # Street openings for types 1 to 6
        openings = {
            1: ['L', 'R'],
            2: ['U', 'D'],
            3: ['L', 'D'],
            4: ['R', 'D'],
            5: ['L', 'U'],
            6: ['R', 'U']
        }

        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True

            curr_type = grid[r][c]
            for d in openings[curr_type]:
                dr, dc, opp_d = dirs[d]
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    neighbor_type = grid[nr][nc]
                    # Check if neighbor opens toward the current cell
                    if opp_d in openings[neighbor_type]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return False
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2267-check-if-there-is-a-valid-parentheses-string-path/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/)
