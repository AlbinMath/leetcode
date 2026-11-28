# LeetCode 934: Shortest Bridge

**LeetCode Problem #934 — Shortest Bridge**
Solve LeetCode Shortest Bridge using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Bridge |
| LeetCode | #934 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `n x n` binary matrix `grid` where `1` represents land and `0` represents water.

An **island** is a 4-directionally connected group of `1`'s not connected to any other `1`'s. There are **exactly two islands** in `grid`.

You may change `0`'s to `1`'s to connect the two islands to form **one island**.

Return *the smallest number of *`0`*'s you must flip to connect the two islands*.

## Constraints
- `n == grid.length == grid[i].length`
- `2 <= n <= 100`
- `grid[i][j]` is either `0` or `1`.
- There are exactly two islands in `grid`.

## Examples
### Example 1
- **Input:** `grid = [[0,1],[1,0]]`
- **Output:** `1`

### Example 2
- **Input:** `grid = [[0,1,0],[0,0,0],[0,0,1]]`
- **Output:** `2`

### Example 3
- **Input:** `grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Bridge**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1],[1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

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
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()

        def dfs(r: int, c: int) -> None:
            grid[r][c] = 2
            queue.append((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)

        # Locate and mark the first island
        found = False
        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        # Expand outward layer-by-layer until reaching the second island
        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
            steps += 1

        return steps
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
- [214. Shortest Palindrome](../../0001-0500/0214-shortest-palindrome/)
- [581. Shortest Unsorted Continuous Subarray](../../0501-1000/0581-shortest-unsorted-continuous-subarray/)
- [748. Shortest Completing Word](../../0501-1000/0748-shortest-completing-word/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-bridge/)
