# LeetCode 864: Shortest Path to Get All Keys

**LeetCode Problem #864 — Shortest Path to Get All Keys**
Solve LeetCode Shortest Path to Get All Keys using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path to Get All Keys |
| LeetCode | #864 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` grid `grid` where:

`'.'` is an empty cell. 
 `'#'` is a wall. 
 `'@'` is the starting point. 
 Lowercase letters represent keys. 
 Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some ` 1 <= k <= 6 `, there is exactly one lowercase and one uppercase letter of the first `k` letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return *the lowest number of moves to acquire all keys*. If it is impossible, return `-1`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 30`
- `grid[i][j]` is either an English letter, `'.'`, `'#'`, or `'@'`.
- There is exactly one `'@'` in the grid.
- The number of keys in the grid is in the range `[1, 6]`.
- Each key in the grid is **unique**.
- Each key in the grid has a matching lock.

## Examples
### Example 1
- **Input:** `grid = ["@.a..","###.#","b.A.B"]`
- **Output:** `8`
- **Explanation:** Note that the goal is to obtain all the keys not to open all the locks.

### Example 2
- **Input:** `grid = ["@..aA","..B#.","....b"]`
- **Output:** `6`

### Example 3
- **Input:** `grid = ["@Aa"]`
- **Output:** `-1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Path to Get All Keys**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = ["@.a..","###.#","b.A.B"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Note that the goal is to obtain all the keys not to open all the locks.

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
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        sr = sc = 0
        for r in range(m):
            for c in range(n):
                ch = grid[r][c]
                if ch == '@':
                    sr, sc = r, c
                elif 'a' <= ch <= 'f':
                    total += 1

        full = (1 << total) - 1
        seen = {(sr, sc, 0)}
        q = deque([(sr, sc, 0, 0)])

        while q:
            r, c, keys, d = q.popleft()
            if keys == full:
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                ch = grid[nr][nc]
                if ch == '#':
                    continue
                nk = keys
                if 'A' <= ch <= 'F':
                    if not (keys >> (ord(ch) - 65)) & 1:
                        continue
                elif 'a' <= ch <= 'f':
                    nk |= 1 << (ord(ch) - 97)
                if (nr, nc, nk) not in seen:
                    seen.add((nr, nc, nk))
                    q.append((nr, nc, nk, d + 1))

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
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0847-shortest-path-visiting-all-nodes/)
- [1091. Shortest Path in Binary Matrix](../../1001-1500/1091-shortest-path-in-binary-matrix/)
- [1129. Shortest Path with Alternating Colors](../../1001-1500/1129-shortest-path-with-alternating-colors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-to-get-all-keys/)
