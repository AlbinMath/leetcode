# LeetCode 1631: Path With Minimum Effort

**LeetCode Problem #1631 — Path With Minimum Effort**
Solve LeetCode Path With Minimum Effort using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Path With Minimum Effort |
| LeetCode | #1631 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)` (i.e., **0-indexed**). You can move **up**, **down**, **left**, or **right**, and you wish to find a route that requires the minimum **effort**.

A route's **effort** is the **maximum absolute difference**** **in heights between two consecutive cells of the route.

Return *the minimum **effort** required to travel from the top-left cell to the bottom-right cell.*

## Constraints
- `rows == heights.length`
- `columns == heights[i].length`
- `1 <= rows, columns <= 100`
- `1 <= heights[i][j] <= 10^6`

## Examples
### Example 1
- **Input:** `heights = [[1,2,2],[3,8,2],[5,3,5]]`
- **Output:** `2`
- **Explanation:** The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

### Example 2
- **Input:** `heights = [[1,2,3],[3,8,4],[5,3,5]]`
- **Output:** `1`
- **Explanation:** The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

### Example 3
- **Input:** `heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]`
- **Output:** `0`
- **Explanation:** This route does not require any effort.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Path With Minimum Effort**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `heights = [[1,2,2],[3,8,2],[5,3,5]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

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

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        d = [[float('inf')]*n for _ in range(m)]
        d[0][0] = 0
        q = [(0, 0, 0)]

        while q:
            e, r, c = heapq.heappop(q)
            if (r, c) == (m-1, n-1):
                return e
            if e > d[r][c]:
                continue
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                x, y = r+dr, c+dc
                if 0 <= x < m and 0 <= y < n:
                    ne = max(e, abs(heights[r][c]-heights[x][y]))
                    if ne < d[x][y]:
                        d[x][y] = ne
                        heapq.heappush(q, (ne, x, y))
        return 0
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
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [931. Minimum Falling Path Sum](../../0501-1000/0931-minimum-falling-path-sum/)
- [1289. Minimum Falling Path Sum II](../../1001-1500/1289-minimum-falling-path-sum-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/path-with-minimum-effort/)
