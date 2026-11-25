# LeetCode 3148: Maximum Difference Score in a Grid

**LeetCode Problem #3148 — Maximum Difference Score in a Grid**
Solve LeetCode Maximum Difference Score in a Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Difference Score in a Grid |
| LeetCode | #3148 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` matrix `grid` consisting of **positive** integers. You can move from a cell in the matrix to **any** other cell that is either to the bottom or to the right (not necessarily adjacent). The score of a move from a cell with the value `c1` to a cell with the value `c2` is `c2 - c1`.

You can start at **any** cell, and you have to make **at least** one move.

Return the **maximum** total score you can achieve.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10^5`
- `1 <= grid[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]`
- **Output:** `9`
- **Explanation:** We start at the cell `(0, 1)`, and we perform the following moves: 
- Move from the cell `(0, 1)` to `(2, 1)` with a score of `7 - 5 = 2`. 
- Move from the cell `(2, 1)` to `(2, 2)` with a score of `14 - 7 = 7`. 
The total score is `2 + 7 = 9`.

### Example 2
- **Input:** `grid = [[4,3,2],[3,2,1]]`
- **Output:** `-1`
- **Explanation:** We start at the cell `(0, 0)`, and we perform one move: `(0, 0)` to `(0, 1)`. The score is `3 - 4 = -1`.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Difference Score in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** We start at the cell `(0, 1)`, and we perform the following moves: 
- Move from the cell `(0, 1)` to `(2, 1)` with a score of `7 - 5 = 2`. 
- Move from the cell `(2, 1)` to `(2, 2)` with a score of `14 - 7 = 7`. 
The total score is `2 + 7 = 9`.

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
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        mn = [[INF] * n for _ in range(m)]
        res = -INF

        for i in range(m):
            for j in range(n):
                prev = INF
                if i > 0:
                    prev = min(prev, mn[i - 1][j])
                if j > 0:
                    prev = min(prev, mn[i][j - 1])

                if prev != INF:
                    res = max(res, grid[i][j] - prev)

                mn[i][j] = min(grid[i][j], prev)

        return res
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
- [3225. Maximum Score From Grid Operations](../../3001-3500/3225-maximum-score-from-grid-operations/)
- [3276. Select Cells in Grid With Maximum Score](../../3001-3500/3276-select-cells-in-grid-with-maximum-score/)
- [3742. Maximum Path Score in a Grid](../../3501-4000/3742-maximum-path-score-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-difference-score-in-a-grid/)
