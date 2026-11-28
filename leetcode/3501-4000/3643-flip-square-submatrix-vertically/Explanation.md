# LeetCode 3643: Flip Square Submatrix Vertically

**LeetCode Problem #3643 — Flip Square Submatrix Vertically**
Solve LeetCode Flip Square Submatrix Vertically using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flip Square Submatrix Vertically |
| LeetCode | #3643 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` integer matrix `grid`, and three integers `x`, `y`, and `k`.

The integers `x` and `y` represent the row and column indices of the **top-left** corner of a **square** submatrix and the integer `k` represents the size (side length) of the square submatrix.

Your task is to flip the submatrix by reversing the order of its rows vertically.

Return the updated matrix.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 100`
- `0 <= x < m`
- `0 <= y < n`
- `1 <= k <= min(m - x, n - y)`

## Examples
### Example 1
- **Input:** `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] , x = 1, y = 0, k = 3`
- **Output:** `[[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]`
- **Explanation:** The diagram above shows the grid before and after the transformation.

### Example 2
- **Input:** `grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2`
- **Output:** `[[3,4,4,2],[2,3,2,3]]`
- **Explanation:** The diagram above shows the grid before and after the transformation.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Flip Square Submatrix Vertically**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] , x = 1, y = 0, k = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]`.
4. **Verification:** The diagram above shows the grid before and after the transformation.

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
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for t in range(k // 2):
            a, b = x + t, x + k - 1 - t
            grid[a][y:y + k], grid[b][y:y + k] = grid[b][y:y + k], grid[a][y:y + k]
        return grid
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
- [221. Maximal Square](../../0001-0500/0221-maximal-square/)
- [367. Valid Perfect Square](../../0001-0500/0367-valid-perfect-square/)
- [473. Matchsticks to Square](../../0001-0500/0473-matchsticks-to-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flip-square-submatrix-vertically/)
