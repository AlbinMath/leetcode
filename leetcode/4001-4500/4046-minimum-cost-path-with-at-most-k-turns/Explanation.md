# LeetCode 4046: Minimum Cost Path With At Most K Turns

**LeetCode Problem #4046 — Minimum Cost Path With At Most K Turns**
Solve LeetCode Minimum Cost Path With At Most K Turns using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path With At Most K Turns |
| LeetCode | #4046 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `grid` of size `m x n`, where `grid[i][j]` represents the cost of visiting cell `(i, j)`, and an integer `k`.

You start at the **top-left** cell `(0, 0)` and want to reach the **bottom-right** cell `(m - 1, n - 1)`.

From each cell, you may move one step in any of the four directions: **up**, **down**, **left**, or **right**.

The cost of a path is the sum of the values of all visited cells, **including** the starting and ending cells. If a cell is visited more than once, its value is included each time it is visited.

Return the **minimum** possible path cost to reach `(m - 1, n - 1)` using **at most** `k` turns. If no such path exists, return `-1`.

A **turn** occurs when the direction changes between two consecutive moves. For example, moving right and then down counts as one turn, while moving right and then right does not.

## Constraints
- `1 <= m == grid.length <= 75`
- `1 <= n == grid[i].length <= 75`
- `0 <= grid[i][j] <= 1000`
- `0 <= k < min(m, n)`

## Examples
### Example 1
- **Input:** `grid = [[2,7,3],[1,4,5]], k = 1`
- **Output:** `12`
- **Explanation:** An optimal path is `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2)`. The moves are down, right, right. 
 The direction changes from down to right once, so the path uses exactly `k = 1` turn. 
 The total path cost is `2 + 1 + 4 + 5 = 12`.

### Example 2
- **Input:** `grid = [[4,1,9],[3,2,5],[4,8,6]], k = 2`
- **Output:** `20`
- **Explanation:** ​​​​​​​ 

 
 An optimal path is `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2)`. The moves are down, right, right, down. 
 The direction changes from down to right and from right to down, so the path uses exactly `k = 2` turns. 
 The total path cost is `4 + 3 + 2 + 5 + 6 = 20`.

### Example 3
- **Input:** `grid = [[1,9],[3,4]], k = 0`
- **Output:** `-1`
- **Explanation:** It is impossible to reach `(1, 1)` using `k = 0` turns. Thus, the answer is -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost Path With At Most K Turns**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[2,7,3],[1,4,5]], k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** An optimal path is `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2)`. The moves are down, right, right. 
 The direction changes from down to right once, so the path uses exactly `k = 1` turn. 
 The total path cost is `2 + 1 + 4 + 5 = 12`.

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
import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Base case: single cell requires 0 moves and 0 turns
        if m == 1 and n == 1:
            return grid[0][0]
        
        # Directions: 0: Up, 1: Down, 2: Left, 3: Right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # dist[r][c][d][t] stores the minimum cost to reach (r, c)
        # entering from direction d with t turns taken.
        # Initialized to infinity.
        INF = float('inf')
        dist = [[[[INF] * (k + 1) for _ in range(4)] for _ in range(n)] for _ in range(m)]
        
        pq = []
        
        # Push initial moves from (0, 0)
        # The first move does not count as a turn (turns = 0).
        for d, (dr, dc) in enumerate(dirs):
            nr, nc = dr, dc
            if 0 <= nr < m and 0 <= nc < n:
                cost = grid[0][0] + grid[nr][nc]
                dist[nr][nc][d][0] = cost
                heapq.heappush(pq, (cost, nr, nc, d, 0))
        
        while pq:
            cost, r, c, d, t = heapq.heappop(pq)
            
            # Reached target with optimal cost
            if r == m - 1 and c == n - 1:
                return cost
            
            if cost > dist[r][c][d][t]:
                continue
            
            for nd, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nt = t if nd == d else t + 1
                    
                    if nt <= k:
                        next_cost = cost + grid[nr][nc]
                        if next_cost < dist[nr][nc][nd][nt]:
                            dist[nr][nc][nd][nt] = next_cost
                            heapq.heappush(pq, (next_cost, nr, nc, nd, nt))
        
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2662-minimum-cost-of-a-path-with-special-roads/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/)
