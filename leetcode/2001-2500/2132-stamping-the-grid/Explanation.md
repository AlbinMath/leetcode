# LeetCode 2132: Stamping the Grid

**LeetCode Problem #2132 — Stamping the Grid**
Solve LeetCode Stamping the Grid using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stamping the Grid |
| LeetCode | #2132 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` binary matrix `grid` where each cell is either `0` (empty) or `1` (occupied).

You are then given stamps of size `stampHeight x stampWidth`. We want to fit the stamps such that they follow the given **restrictions** and **requirements**:

Cover all the **empty** cells. 
 Do not cover any of the **occupied** cells. 
 We can put as **many** stamps as we want. 
 Stamps can **overlap** with each other. 
 Stamps are not allowed to be **rotated**. 
 Stamps must stay completely **inside** the grid.

Return `true` *if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return* `false`.

## Constraints
- `m == grid.length`
- `n == grid[r].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 2 * 10^5`
- `grid[r][c]` is either `0` or `1`.
- `1 <= stampHeight, stampWidth <= 10^5`

## Examples
### Example 1
- **Input:** `grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3`
- **Output:** `true`
- **Explanation:** We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.

### Example 2
- **Input:** `grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2`
- **Output:** `false`
- **Explanation:** There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Stamping the Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        # prefix sum of grid
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                P[i + 1][j + 1] = P[i][j + 1] + P[i + 1][j] - P[i][j] + grid[i][j]

        # difference array for stamps
        D = [[0] * (n + 2) for _ in range(m + 2)]
        for r in range(m - stampHeight + 1):
            for c in range(n - stampWidth + 1):
                r2, c2 = r + stampHeight, c + stampWidth
                if P[r2][c2] - P[r][c2] - P[r2][c] + P[r][c] == 0:
                    D[r][c] += 1
                    D[r][c2] -= 1
                    D[r2][c] -= 1
                    D[r2][c2] += 1

        # accumulate and verify coverage
        cover = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                cover[i + 1][j + 1] = (
                    cover[i][j + 1] + cover[i + 1][j] - cover[i][j] + D[i][j]
                )
                if grid[i][j] == 0 and cover[i + 1][j + 1] == 0:
                    return False
        return True
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [936. Stamping The Sequence](../../0501-1000/0936-stamping-the-sequence/)
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1001. Grid Illumination](../../1001-1500/1001-grid-illumination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stamping-the-grid/)
