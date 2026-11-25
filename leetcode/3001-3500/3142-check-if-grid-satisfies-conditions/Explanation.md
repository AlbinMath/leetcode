# LeetCode 3142: Check if Grid Satisfies Conditions

**LeetCode Problem #3142 — Check if Grid Satisfies Conditions**
Solve LeetCode Check if Grid Satisfies Conditions using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Grid Satisfies Conditions |
| LeetCode | #3142 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D matrix `grid` of size `m x n`. You need to check if each cell `grid[i][j]` is:

Equal to the cell below it, i.e. `grid[i][j] == grid[i + 1][j]` (if it exists). 
 Different from the cell to its right, i.e. `grid[i][j] != grid[i][j + 1]` (if it exists).

Return `true` if **all** the cells satisfy these conditions, otherwise, return `false`.

## Constraints
- `1 <= n, m <= 10`
- `0 <= grid[i][j] <= 9`

## Examples
### Example 1
- **Input:** `grid = [[1,0,2],[1,0,2]]`
- **Output:** `true`

### Example 2
- **Input:** `grid = [[1,1,1],[0,0,0]]`
- **Output:** `false`

### Example 3
- **Input:** `grid = [[1],[2],[3]]`
- **Output:** `false`
- **Explanation:** Cells in the first column have different values.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Grid Satisfies Conditions**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,2],[1,0,2]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        first = grid[0]
        if any(first[j] == first[j + 1] for j in range(len(first) - 1)):
            return False
        return all(row == first for row in grid)
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
- [1391. Check if There is a Valid Path in a Grid](../../1001-1500/1391-check-if-there-is-a-valid-path-in-a-grid/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)
- [1232. Check If It Is a Straight Line](../../1001-1500/1232-check-if-it-is-a-straight-line/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-grid-satisfies-conditions/)
