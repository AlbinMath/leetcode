# LeetCode 3989: Maximum Consistent Columns in a Grid

**LeetCode Problem #3989 — Maximum Consistent Columns in a Grid**
Solve LeetCode Maximum Consistent Columns in a Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Consistent Columns in a Grid |
| LeetCode | #3989 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `grid` of size `m x n`, and an integer `limit`.

You may remove zero or more columns from the grid, but at least one column must remain. The **relative** order of the remaining columns must be preserved.

A grid is called **consistent** if for every row `i`, and for every pair of adjacent remaining columns `a` and `b` with `a < b`, the following holds: `|grid[i][b] - grid[i][a]| <= limit`.

Return the **maximum** number of columns that can remain such that the resulting grid is **consistent**.

## Constraints
- `1 <= m == grid.length <= 250`
- `1 <= n == grid[i].length <= 250`
- `-10^5 <= grid[i][j] <= 10^5`
- `0 <= limit <= 10^5​​​​​​​​​​​​​​​​`

## Examples
### Example 1
- **Input:** `grid = [[-2,0,3]], limit = 2`
- **Output:** `2`
- **Explanation:** Remove column 2 and keep columns 0 and 1, which gives `|grid[0][1] &minus; grid[0][0]| = |0 &minus; (&minus;2)| = 2 <= limit`. 
 Thus, the maximum number of columns that can remain is 2.

### Example 2
- **Input:** `grid = [[1,-1,1],[2,2,2]], limit = 1`
- **Output:** `2`
- **Explanation:** Remove column 1 and keep columns 0 and 2, which gives
 
 `|grid[0][2] &minus; grid[0][0]| = |1 &minus; 1| = 0 <= limit` and 
 `|grid[1][2] &minus; grid[1][0]| = |2 &minus; 2| = 0 <= limit`. 
 
 
 Thus, the maximum number of columns that can remain is 2.

### Example 3
- **Input:** `grid = [[-5,5]], limit = 9`
- **Output:** `1`
- **Explanation:** Remove either column 0 or column 1, since `|grid[0][1] &minus; grid[0][0]| = |5 &minus; (&minus;5)| = 10 > limit`. 
 Thus, the maximum number of columns that can remain is 1.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Consistent Columns in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[-2,0,3]], limit = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Remove column 2 and keep columns 0 and 1, which gives `|grid[0][1] &minus; grid[0][0]| = |0 &minus; (&minus;2)| = 2 <= limit`. 
 Thus, the maximum number of columns that can remain is 2.

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
from typing import List

class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        cols = list(zip(*grid))
        n = len(cols)
        dp = [1] * n
        for b in range(n):
            cb = cols[b]
            for a in range(b):
                if dp[a] + 1 > dp[b]:
                    ca = cols[a]
                    if all(abs(x - y) <= limit for x, y in zip(ca, cb)):
                        dp[b] = dp[a] + 1
        return max(dp)
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
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1072-flip-columns-for-maximum-number-of-equal-rows/)
- [2397. Maximum Rows Covered by Columns](../../2001-2500/2397-maximum-rows-covered-by-columns/)
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2503-maximum-number-of-points-from-grid-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/)
