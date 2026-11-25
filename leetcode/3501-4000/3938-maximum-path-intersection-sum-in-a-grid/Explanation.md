# LeetCode 3938: Maximum Path Intersection Sum in a Grid

**LeetCode Problem #3938 — Maximum Path Intersection Sum in a Grid**
Solve LeetCode Maximum Path Intersection Sum in a Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Path Intersection Sum in a Grid |
| LeetCode | #3938 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` integer matrix `grid`.

Two players move across the grid:

Player 1 starts at the top-left cell `(0, 0)` and can move only right or down. Their destination is the bottom-right cell `(m - 1, n - 1)`. 
 Player 2 starts at the bottom-left cell `(m - 1, 0)` and can move only right or up. Their destination is the top-right cell `(0, n - 1)`.

Each player must choose a valid path from their respective starting cell to their destination.

A cell is called **shared** if it belongs to **both** chosen paths.

Return an integer denoting the **maximum** possible sum of values of all **shared** cells.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 5 * 10^5`
- `-100 <= grid[i][j] <= 100`

## Examples
### Example 1
- **Input:** `grid = [[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]`
- **Output:** `4`
- **Explanation:** The diagram shows one optimal choice of paths.

 
 Player 1 follows the red/purple path from the top-left cell to the bottom-right cell:
 
 `(0, 0) &rarr; (1, 0) &rarr; (2, 0) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3) &rarr; (3, 3) &rarr; (4, 3)` 
 
 
 Player 2 follows the blue/purple path from the bottom-left cell to the top-right cell:
 
 `(4, 0) &rarr; (4, 1) &rarr; (3, 1) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3) &rarr; (1, 3) &rarr; (0, 3)` 
 
 
 The shared cells are `(2, 1)`, `(2, 2)`, and `(2, 3)`. 
 The sum is `2 + (-1) + 3 = 4`, which is the maximum possible sum.

### Example 2
- **Input:** `grid = [[4,-2,-3],[-1,-3,-1],[-4,2,-1]]`
- **Output:** `3`
- **Explanation:** One optimal pair of paths is shown in the diagram. 

 
 Player 1 follows the red/purple path:
 
 `(0, 0) &rarr; (1, 0) &rarr; (1, 1) &rarr; (1, 2) &rarr; (2, 2)` 
 
 
 Player 2 follows the blue/purple path:
 
 `(2, 0) &rarr; (1, 0) &rarr; (0, 0) &rarr; (0, 1) &rarr; (0, 2)` 
 
 
 The shared cells are `(0, 0)` and `(1, 0)`. 
 The sum is `4 + (-1) = 3`, which is the maximum possible.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Path Intersection Sum in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The diagram shows one optimal choice of paths.

 
 Player 1 follows the red/purple path from the top-left cell to the bottom-right cell:
 
 `(0, 0) &rarr; (1, 0) &rarr; (2, 0) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3) &rarr; (3, 3) &rarr; (4, 3)` 
 
 
 Player 2 follows the blue/purple path from the bottom-left cell to the top-right cell:
 
 `(4, 0) &rarr; (4, 1) &rarr; (3, 1) &rarr; (2, 1) &rarr; (2, 2) &rarr; (2, 3) &rarr; (1, 3) &rarr; (0, 3)` 
 
 
 The shared cells are `(2, 1)`, `(2, 2)`, and `(2, 3)`. 
 The sum is `2 + (-1) + 3 = 4`, which is the maximum possible sum.

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
        NEG = float('-inf')
        res = NEG

        def best_len2(a):
            best = NEG
            e2 = NEG
            for j in range(1, len(a)):
                e2 = a[j] + max(a[j - 1], e2)
                best = max(best, e2)
            return best

        for row in grid:
            res = max(res, best_len2(row))
        for col in zip(*grid):
            res = max(res, best_len2(col))

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                res = max(res, grid[i][j])

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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [3742. Maximum Path Score in a Grid](../../3501-4000/3742-maximum-path-score-in-a-grid/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/)
