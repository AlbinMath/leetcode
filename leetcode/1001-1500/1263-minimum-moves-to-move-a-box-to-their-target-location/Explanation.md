# LeetCode 1263: Minimum Moves to Move a Box to Their Target Location

**LeetCode Problem #1263 — Minimum Moves to Move a Box to Their Target Location**
Solve LeetCode Minimum Moves to Move a Box to Their Target Location using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Move a Box to Their Target Location |
| LeetCode | #1263 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an `m x n` grid of characters `grid` where each element is a wall, floor, or box.

Your task is to move the box `'B'` to the target position `'T'` under the following rules:

The character `'S'` represents the player. The player can move up, down, left, right in `grid` if it is a floor (empty cell). 
 The character `'.'` represents the floor which means a free cell to walk. 
 The character `'#'` represents the wall which means an obstacle (impossible to walk there). 
 There is only one box `'B'` and one target cell `'T'` in the `grid`. 
 The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a **push**. 
 The player cannot walk through the box.

Return *the minimum number of **pushes** to move the box to the target*. If there is no way to reach the target, return `-1`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 20`
- `grid` contains only characters `'.'`, `'#'`, `'S'`, `'T'`, or `'B'`.
- There is only one character `'S'`, `'B'`, and `'T'` in the `grid`.

## Examples
### Example 1
- **Input:** `grid = [["#","#","#","#","#","#"],
 ["#","T","#","#","#","#"],
 ["#",".",".","B",".","#"],
 ["#",".","#","#",".","#"],
 ["#",".",".",".","S","#"],
 ["#","#","#","#","#","#"]]`
- **Output:** `3`
- **Explanation:** We return only the number of times the box is pushed.

### Example 2
- **Input:** `grid = [["#","#","#","#","#","#"],
 ["#","T","#","#","#","#"],
 ["#",".",".","B",".","#"],
 ["#","#","#","#",".","#"],
 ["#",".",".",".","S","#"],
 ["#","#","#","#","#","#"]]`
- **Output:** `-1`

### Example 3
- **Input:** `grid = [["#","#","#","#","#","#"],
 ["#","T",".",".","#","#"],
 ["#",".","#","B",".","#"],
 ["#",".",".",".",".","#"],
 ["#",".",".",".","S","#"],
 ["#","#","#","#","#","#"]]`
- **Output:** `5`
- **Explanation:** push the box down, left, left, up and up.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Moves to Move a Box to Their Target Location**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [["#","#","#","#","#","#"],
 ["#","T","#","#","#","#"],
 ["#",".",".","B",".","#"],
 ["#",".","#","#",".","#"],
 ["#",".",".",".","S","#"],
 ["#","#","#","#","#","#"]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We return only the number of times the box is pushed.

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
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sr, sc = i, j
                elif grid[i][j] == 'B':
                    br, bc = i, j
                elif grid[i][j] == 'T':
                    tr, tc = i, j

        def free(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] != '#'

        def can_reach(src, dst, box):
            # can the player walk from src to dst without stepping on the box?
            if src == dst:
                return True
            seen = {src}
            q = deque([src])
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) == box or (nr, nc) in seen or not free(nr, nc):
                        continue
                    if (nr, nc) == dst:
                        return True
                    seen.add((nr, nc))
                    q.append((nr, nc))
            return False

        start = (br, bc, sr, sc)
        visited = {start}
        q = deque([(br, bc, sr, sc, 0)])
        while q:
            r, c, pr, pc, d = q.popleft()
            if (r, c) == (tr, tc):
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc          # box destination
                stand = (r - dr, c - dc)         # where player must stand
                if not free(nr, nc) or not free(*stand):
                    continue
                # after the push the player will be at (r, c)
                if (nr, nc, r, c) in visited:
                    continue
                if can_reach((pr, pc), stand, (r, c)):
                    visited.add((nr, nc, r, c))
                    q.append((nr, nc, r, c, d + 1))
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
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1769-minimum-number-of-operations-to-move-all-balls-to-each-box/)
- [1210. Minimum Moves to Reach Target with Rotations](../../1001-1500/1210-minimum-moves-to-reach-target-with-rotations/)
- [2139. Minimum Moves to Reach Target Score](../../2001-2500/2139-minimum-moves-to-reach-target-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/)
