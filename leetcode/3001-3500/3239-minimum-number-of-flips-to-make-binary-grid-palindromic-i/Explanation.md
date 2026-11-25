# LeetCode 3239: Minimum Number of Flips to Make Binary Grid Palindromic I

**LeetCode Problem #3239 — Minimum Number of Flips to Make Binary Grid Palindromic I**
Solve LeetCode Minimum Number of Flips to Make Binary Grid Palindromic I using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Flips to Make Binary Grid Palindromic I |
| LeetCode | #3239 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` binary matrix `grid`.

A row or column is considered **palindromic** if its values read the same forward and backward.

You can **flip** any number of cells in `grid` from `0` to `1`, or from `1` to `0`.

Return the **minimum** number of cells that need to be flipped to make **either** all rows **palindromic** or all columns **palindromic**.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m * n <= 2 * 10^5`
- `0 <= grid[i][j] <= 1`

## Examples
### Example 1
- **Input:** `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- **Output:** `2`
- **Explanation:** Flipping the highlighted cells makes all the rows palindromic.

### Example 2
- **Input:** `grid = [[0,1],[0,1],[0,0]]`
- **Output:** `1`
- **Explanation:** Flipping the highlighted cell makes all the columns palindromic.

### Example 3
- **Input:** `grid = [[1],[0]]`
- **Output:** `0`
- **Explanation:** All rows are already palindromic.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Flips to Make Binary Grid Palindromic I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,0],[0,0,0],[0,0,1]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Flipping the highlighted cells makes all the rows palindromic.

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
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows = 0
        for row in grid:
            for j in range(n // 2):
                if row[j] != row[n - 1 - j]:
                    rows += 1

        cols = 0
        for i in range(m // 2):
            top, bot = grid[i], grid[m - 1 - i]
            for j in range(n):
                if top[j] != bot[j]:
                    cols += 1

        return min(rows, cols)
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
- [3240. Minimum Number of Flips to Make Binary Grid Palindromic II](../../3001-3500/3240-minimum-number-of-flips-to-make-binary-grid-palindromic-ii/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1864-minimum-number-of-swaps-to-make-the-binary-string-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/)
