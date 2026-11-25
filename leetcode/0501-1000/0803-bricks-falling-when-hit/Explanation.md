# LeetCode 803: Bricks Falling When Hit

**LeetCode Problem #803 — Bricks Falling When Hit**
Solve LeetCode Bricks Falling When Hit using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bricks Falling When Hit |
| LeetCode | #803 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` binary `grid`, where each `1` represents a brick and `0` represents an empty space. A brick is **stable** if:

It is directly connected to the top of the grid, or 
 At least one other brick in its four adjacent cells is **stable**.

You are also given an array `hits`, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location `hits[i] = (row_i, col_i)`. The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will **fall**. Once a brick falls, it is **immediately** erased from the `grid` (i.e., it does not land on other stable bricks).

Return *an array *`result`*, where each *`result[i]`* is the number of bricks that will **fall** after the *`i^th`* erasure is applied.*

**Note** that an erasure may refer to a location with no brick, and if it does, no bricks drop.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `grid[i][j]` is `0` or `1`.
- `1 <= hits.length <= 4 * 10^4`
- `hits[i].length == 2`
- `0 <= x_i <= m - 1`
- `0 <= y_i <= n - 1`
- All `(x_i, y_i)` are unique.

## Examples
### Example 1
- **Input:** `grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]`
- **Output:** `[2]`
- **Explanation:** Starting with the grid:
[[1,0,0,0],
 [ 1 ,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0, 1 , 1 ,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].

### Example 2
- **Input:** `grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]`
- **Output:** `[0,0]`
- **Explanation:** Starting with the grid:
[[1,0,0,0],
 [1, 1 ,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [ 1 ,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Bricks Falling When Hit**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2]`.
4. **Verification:** Starting with the grid:
[[1,0,0,0],
 [ 1 ,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0, 1 , 1 ,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        roof = m * n
        dsu = DSU(roof + 1)

        def node_id(r, c):
            return r * n + c

        # 1. Copy grid and apply all hits
        A = [row[:] for row in grid]
        for r, c in hits:
            A[r][c] -= 1

        # 2. Build DSU for the final state
        for r in range(m):
            for c in range(n):
                if A[r][c] == 1:
                    u = node_id(r, c)
                    if r == 0:
                        dsu.union(u, roof)
                    if r > 0 and A[r - 1][c] == 1:
                        dsu.union(u, node_id(r - 1, c))
                    if c > 0 and A[r][c - 1] == 1:
                        dsu.union(u, node_id(r, c - 1))

        # 3. Process hits in reverse
        res = [0] * len(hits)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            A[r][c] += 1

            # If it wasn't a brick originally, no bricks fall
            if A[r][c] != 1:
                continue

            prev_roof_size = dsu.get_size(roof)
            u = node_id(r, c)

            # Reconnect to neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and A[nr][nc] == 1:
                    dsu.union(u, node_id(nr, nc))

            # Connect to roof if it is on the top row
            if r == 0:
                dsu.union(u, roof)

            curr_roof_size = dsu.get_size(roof)
            # Fallen bricks = newly attached minus the brick itself
            res[i] = max(0, curr_roof_size - prev_roof_size - 1)

        return res
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [931. Minimum Falling Path Sum](../../0501-1000/0931-minimum-falling-path-sum/)
- [1289. Minimum Falling Path Sum II](../../1001-1500/1289-minimum-falling-path-sum-ii/)
- [2039. The Time When the Network Becomes Idle](../../2001-2500/2039-the-time-when-the-network-becomes-idle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bricks-falling-when-hit/)
