# LeetCode 3240: Minimum Number of Flips to Make Binary Grid Palindromic II

**LeetCode Problem #3240 — Minimum Number of Flips to Make Binary Grid Palindromic II**
Solve LeetCode Minimum Number of Flips to Make Binary Grid Palindromic II using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Flips to Make Binary Grid Palindromic II |
| LeetCode | #3240 |
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

Return the **minimum** number of cells that need to be flipped to make **all** rows and columns **palindromic**, and the total number of `1`'s in `grid` **divisible** by `4`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m * n <= 2 * 10^5`
- `0 <= grid[i][j] <= 1`

## Examples
### Example 1
- **Input:** `grid = [[1,0,0],[0,1,0],[0,0,1]]`
- **Output:** `3`

### Example 2
- **Input:** `grid = [[0,1],[0,1],[0,0]]`
- **Output:** `2`

### Example 3
- **Input:** `grid = [[1],[1]]`
- **Output:** `2`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Flips to Make Binary Grid Palindromic II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,0],[0,1,0],[0,0,1]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
        res = 0

        # groups of 4
        for i in range(m // 2):
            for j in range(n // 2):
                k = (grid[i][j] + grid[i][n - 1 - j]
                     + grid[m - 1 - i][j] + grid[m - 1 - i][n - 1 - j])
                res += min(k, 4 - k)

        diff = both1 = 0

        # middle row pairs
        if m % 2:
            mid = m // 2
            for j in range(n // 2):
                a, b = grid[mid][j], grid[mid][n - 1 - j]
                if a != b:
                    diff += 1
                elif a == 1:
                    both1 += 1

        # middle column pairs
        if n % 2:
            mid = n // 2
            for i in range(m // 2):
                a, b = grid[i][mid], grid[m - 1 - i][mid]
                if a != b:
                    diff += 1
                elif a == 1:
                    both1 += 1

        # center cell
        if m % 2 and n % 2 and grid[m // 2][n // 2] == 1:
            res += 1

        res += diff
        if diff == 0 and both1 % 2:
            res += 2

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
- [3239. Minimum Number of Flips to Make Binary Grid Palindromic I](../../3001-3500/3239-minimum-number-of-flips-to-make-binary-grid-palindromic-i/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/)
