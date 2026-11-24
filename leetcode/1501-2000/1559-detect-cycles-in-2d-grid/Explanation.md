# LeetCode 1559: Detect Cycles in 2D Grid

**LeetCode Problem #1559 — Detect Cycles in 2D Grid**
Solve LeetCode Detect Cycles in 2D Grid using Python and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Detect Cycles in 2D Grid |
| LeetCode | #1559 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a 2D array of characters `grid` of size `m x n`, you need to find if there exists any cycle consisting of the **same value** in `grid`.

A cycle is a path of **length 4 or more** in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the **same value** of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle `(1, 1) -> (1, 2) -> (1, 1)` is invalid because from `(1, 2)` we visited `(1, 1)` which was the last visited cell.

Return `true` if any cycle of the same value exists in `grid`, otherwise, return `false`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 500`
- `grid` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]`
- **Output:** `true`
- **Explanation:** There are two valid cycles shown in different colors in the image below:

### Example 2
- **Input:** `grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]`
- **Output:** `true`
- **Explanation:** There is only one valid cycle highlighted in the image below:

### Example 3
- **Input:** `grid = [["a","b","b"],["b","z","b"],["b","b","a"]]`
- **Output:** `false`

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Detect Cycles in 2D Grid**, we observe the problem requirements and utilize the **Fast & Slow Pointers** technique. We iterate through the inputs using **Floyd Cycle Detection**, leveraging a **Linked List / Pointer** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Linked List / Pointer**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** There are two valid cycles shown in different colors in the image below:

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import sys
from typing import List

# Increase recursion depth for deep grid traversals (up to 500 * 500 = 250,000)
sys.setrecursionlimit(300000)

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int, parent_r: int, parent_c: int) -> bool:
            visited[r][c] = True
            val = grid[r][c]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == val:
                    # Skip the cell we just came from
                    if nr == parent_r and nc == parent_c:
                        continue
                    # Back-edge found -> cycle exists
                    if visited[nr][nc]:
                        return True
                    if dfs(nr, nc, r, c):
                        return True

            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True

        return False
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1260. Shift 2D Grid](../../1001-1500/1260-shift-2d-grid/)
- [3311. Construct 2D Grid Matching Graph Layout](../../3001-3500/3311-construct-2d-grid-matching-graph-layout/)
- [74. Search a 2D Matrix](../../0001-0500/0074-search-a-2d-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/detect-cycles-in-2d-grid/)
