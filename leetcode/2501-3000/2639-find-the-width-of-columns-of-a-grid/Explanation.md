# LeetCode 2639: Find the Width of Columns of a Grid

**LeetCode Problem #2639 — Find the Width of Columns of a Grid**
Solve LeetCode Find the Width of Columns of a Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Width of Columns of a Grid |
| LeetCode | #2639 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** `m x n` integer matrix `grid`. The width of a column is the maximum **length **of its integers.

For example, if `grid = [[-10], [3], [12]]`, the width of the only column is `3` since `-10` is of length `3`.

Return *an integer array* `ans` *of size* `n` *where* `ans[i]` *is the width of the* `i^th` *column*.

The **length** of an integer `x` with `len` digits is equal to `len` if `x` is non-negative, and `len + 1` otherwise.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100 `
- `-10^9 <= grid[r][c] <= 10^9`

## Examples
### Example 1
- **Input:** `grid = [[1],[22],[333]]`
- **Output:** `[3]`
- **Explanation:** In the 0^th column, 333 is of length 3.

### Example 2
- **Input:** `grid = [[-15,1,3],[15,7,12],[5,6,-2]]`
- **Output:** `[3,1,2]`
- **Explanation:** In the 0^th column, only -15 is of length 3.
In the 1^st column, all integers are of length 1. 
In the 2^nd column, both 12 and -2 are of length 2.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Width of Columns of a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1],[22],[333]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3]`.
4. **Verification:** In the 0^th column, 333 is of length 3.

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
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * n
        for row in grid:
            for j, v in enumerate(row):
                ans[j] = max(ans[j], len(str(v)))
        return ans
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
- [2812. Find the Safest Path in a Grid](../../2501-3000/2812-find-the-safest-path-in-a-grid/)
- [3030. Find the Grid of Region Average](../../3001-3500/3030-find-the-grid-of-region-average/)
- [3286. Find a Safe Walk Through a Grid](../../3001-3500/3286-find-a-safe-walk-through-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/)
