# LeetCode 3797: Count Routes to Climb a Rectangular Grid

**LeetCode Problem #3797 — Count Routes to Climb a Rectangular Grid**
Solve LeetCode Count Routes to Climb a Rectangular Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Routes to Climb a Rectangular Grid |
| LeetCode | #3797 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string array `grid` of size `n`, where each string `grid[i]` has length `m`. The character `grid[i][j]` is one of the following symbols:

`'.'`: The cell is available. 
 `'#'`: The cell is blocked.

You want to count the number of different routes to climb `grid`. Each route must start from *any cell* in the bottom row (row `n - 1`) and end in the top row (row 0).

However, there are some constraints on the route.

You can only move from one available cell to **another** available cell. 
 The **Euclidean distance** of each move is **at most** `d`, where `d` is an integer parameter given to you. The Euclidean distance between two cells `(r1, c1)`, `(r2, c2)` is `sqrt((r1 - r2)^2 + (c1 - c2)^2)`. 
 Each move either stays on the same row or moves to the row directly above (from row `r` to `r - 1`). 
 You cannot stay on the same row for two consecutive turns. If you stay on the same row in a move (and this move is not the last move), your next move must go to the row above.

Return an integer denoting the number of such routes. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n == grid.length <= 750`
- `1 <= m == grid[i].length <= 750`
- `grid[i][j]` is `'.'` or `'#'`.
- `1 <= d <= 750`

## Examples
### Example 1
- **Input:** `grid = ["..","#."], d = 1`
- **Output:** `2`
- **Explanation:** We label the cells we visit in the routes sequentially, starting from 1. The two routes are: 

 
.2
#1
 

 
32
#1
 

 We can move from the cell (1, 1) to the cell (0, 1) because the Euclidean distance is `sqrt((1 - 0)^2 + (1 - 1)^2) = sqrt(1) <= d`. 

 However, we cannot move from the cell (1, 1) to the cell (0, 0) because the Euclidean distance is `sqrt((1 - 0)^2 + (1 - 0)^2) = sqrt(2) > d`.

### Example 2
- **Input:** `grid = ["..","#."], d = 2`
- **Output:** `4`
- **Explanation:** Two of the routes are given in

### Example 3
- **Input:** `grid = ["#"], d = 750`
- **Output:** `0`
- **Explanation:** We cannot choose any cell as the starting cell. Therefore, there are no routes.

### Example 4
- **Input:** `grid = [".."], d = 1`
- **Output:** `4`
- **Explanation:** The possible routes are: 

 
.1
 

 
1.
 

 
12
 

 
21

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Routes to Climb a Rectangular Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = ["..","#."], d = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We label the cells we visit in the routes sequentially, starting from 1. The two routes are: 

 
.2
#1
 

 
32
#1
 

 We can move from the cell (1, 1) to the cell (0, 1) because the Euclidean distance is `sqrt((1 - 0)^2 + (1 - 1)^2) = sqrt(1) <= d`. 

 However, we cannot move from the cell (1, 1) to the cell (0, 0) because the Euclidean distance is `sqrt((1 - 0)^2 + (1 - 0)^2) = sqrt(2) > d`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import isqrt

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        MOD = 10**9 + 7
        n, m = len(grid), len(grid[0])
        w = isqrt(d * d - 1)

        def window(pref, c, rad):
            lo, hi = max(0, c - rad), min(m - 1, c + rad)
            return pref[hi + 1] - pref[lo]

        def prefix(arr):
            p = [0] * (m + 1)
            for i, v in enumerate(arr):
                p[i + 1] = (p[i] + v) % MOD
            return p

        # bottom row
        A = [1 if grid[n - 1][c] == '.' else 0 for c in range(m)]
        pa = prefix(A)
        B = [0] * m
        for c in range(m):
            if grid[n - 1][c] == '.':
                B[c] = (window(pa, c, d) - A[c]) % MOD

        for r in range(n - 2, -1, -1):
            tot = [(A[c] + B[c]) % MOD for c in range(m)]
            pt = prefix(tot)
            newA = [0] * m
            for c in range(m):
                if grid[r][c] == '.':
                    newA[c] = window(pt, c, w)
            pa = prefix(newA)
            newB = [0] * m
            for c in range(m):
                if grid[r][c] == '.':
                    newB[c] = (window(pa, c, d) - newA[c]) % MOD
            A, B = newA, newB

        return (sum(A) + sum(B)) % MOD
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1575. Count All Possible Routes](../../1501-2000/1575-count-all-possible-routes/)
- [2257. Count Unguarded Cells in the Grid](../../2001-2500/2257-count-unguarded-cells-in-the-grid/)
- [815. Bus Routes](../../0501-1000/0815-bus-routes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/)
