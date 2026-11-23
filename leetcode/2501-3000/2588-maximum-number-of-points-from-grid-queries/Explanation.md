# LeetCode 2503: Maximum Number of Points From Grid Queries

**LeetCode Problem #2503 — Maximum Number of Points From Grid Queries**
Solve LeetCode Maximum Number of Points From Grid Queries using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Points From Grid Queries |
| LeetCode | #2503 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` integer matrix `grid` and an array `queries` of size `k`.

Find an array `answer` of size `k` such that for each integer `queries[i]` you start in the **top left** cell of the matrix and repeat the following process:

If `queries[i]` is **strictly** greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any **adjacent** cell in all `4` directions: up, down, left, and right. 
 Otherwise, you do not get any points, and you end this process.

After the process, `answer[i]` is the **maximum** number of points you can get. **Note** that for each query you are allowed to visit the same cell **multiple** times.

Return *the resulting array* `answer`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10^5`
- `k == queries.length`
- `1 <= k <= 10^4`
- `1 <= grid[i][j], queries[i] <= 10^6`

## Examples
### Example 1
- **Input:** `grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]`
- **Output:** `[5,8,1]`
- **Explanation:** The diagrams above show which cells we visit to get points for each query.

### Example 2
- **Input:** `grid = [[5,2,1],[1,1,2]], queries = [3]`
- **Output:** `[0]`
- **Explanation:** We can not get any points because the value of the top left cell is already greater than or equal to 3.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Points From Grid Queries**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,8,1]`.
4. **Verification:** The diagrams above show which cells we visit to get points for each query.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)

        # Sort queries while preserving original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        ans = [0] * k
        visited = [[False] * n for _ in range(m)]

        # Min-heap stores: (grid[r][c], r, c)
        pq = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        points = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for orig_idx, q_val in sorted_queries:
            # Expand all reachable boundary cells with value strictly less than q_val
            while pq and pq[0][0] < q_val:
                val, r, c = heapq.heappop(pq)
                points += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(pq, (grid[nr][nc], nr, nc))

            ans[orig_idx] = points

        return ans
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1423. Maximum Points You Can Obtain from Cards](../../1501-2000/1538-maximum-points-you-can-obtain-from-cards/)
- [1610. Maximum Number of Visible Points](../../1501-2000/1733-maximum-number-of-visible-points/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/)
