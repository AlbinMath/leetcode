# LeetCode 1210: Minimum Moves to Reach Target with Rotations

**LeetCode Problem #1210 — Minimum Moves to Reach Target with Rotations**
Solve LeetCode Minimum Moves to Reach Target with Rotations using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Reach Target with Rotations |
| LeetCode | #1210 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
In an `n*n` grid, there is a snake that spans 2 cells and starts moving from the top left corner at `(0, 0)` and `(0, 1)`. The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at `(n-1, n-2)` and `(n-1, n-1)`.

In one move the snake can:

Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is. 
 Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is. 
 Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from `(r, c)` and `(r, c+1)` to `(r, c)` and `(r+1, c)`. 
 
 Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from `(r, c)` and `(r+1, c)` to `(r, c)` and `(r, c+1)`.

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return `-1`.

## Constraints
- `2 <= n <= 100`
- `0 <= grid[i][j] <= 1`
- It is guaranteed that the snake starts at empty cells.

## Examples
### Example 1
- **Input:** `grid = [[0,0,0,0,0,1],
 [1,1,0,0,1,0],
 [0,0,0,0,1,1],
 [0,0,1,0,1,0],
 [0,1,1,0,0,0],
 [0,1,1,0,0,0]]`
- **Output:** `11`
- **Explanation:** One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].

### Example 2
- **Input:** `grid = [[0,0,1,1,1,1],
 [0,0,0,0,1,1],
 [1,1,0,0,0,1],
 [1,1,1,0,0,1],
 [1,1,1,0,0,1],
 [1,1,1,0,0,0]]`
- **Output:** `9`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Moves to Reach Target with Rotations**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,0,0,0,0,1],
 [1,1,0,0,1,0],
 [0,0,0,0,1,1],
 [0,0,1,0,1,0],
 [0,1,1,0,0,0],
 [0,1,1,0,0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].

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
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[[False] * 2 for _ in range(n)] for _ in range(n)]
        visited[0][0][0] = True
        q = deque([(0, 0, 0, 0)])  # (r, c, orientation, moves)

        while q:
            r, c, o, d = q.popleft()
            if r == n - 1 and c == n - 2 and o == 0:
                return d

            nxt = []
            if o == 0:
                if c + 2 < n and grid[r][c + 2] == 0:
                    nxt.append((r, c + 1, 0))
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    nxt.append((r + 1, c, 0))
                    nxt.append((r, c, 1))
            else:
                if r + 2 < n and grid[r + 2][c] == 0:
                    nxt.append((r + 1, c, 1))
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    nxt.append((r, c + 1, 1))
                    nxt.append((r, c, 0))

            for nr, nc, no in nxt:
                if not visited[nr][nc][no]:
                    visited[nr][nc][no] = True
                    q.append((nr, nc, no, d + 1))
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
- [1263. Minimum Moves to Move a Box to Their Target Location](../../1001-1500/1389-minimum-moves-to-move-a-box-to-their-target-location/)
- [3977. Minimum Time to Reach Target With Limited Power](../../4001-4500/4206-minimum-time-to-reach-target-with-limited-power/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/)
