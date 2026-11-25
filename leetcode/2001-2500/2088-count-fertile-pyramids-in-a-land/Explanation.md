# LeetCode 2088: Count Fertile Pyramids in a Land

**LeetCode Problem #2088 — Count Fertile Pyramids in a Land**
Solve LeetCode Count Fertile Pyramids in a Land using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Fertile Pyramids in a Land |
| LeetCode | #2088 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A farmer has a **rectangular grid** of land with `m` rows and `n` columns that can be divided into unit cells. Each cell is either **fertile** (represented by a `1`) or **barren** (represented by a `0`). All cells outside the grid are considered barren.

A **pyramidal plot** of land can be defined as a set of cells with the following criteria:

The number of cells in the set has to be **greater than **`1` and all cells must be **fertile**. 
 The **apex** of a pyramid is the **topmost** cell of the pyramid. The **height** of a pyramid is the number of rows it covers. Let `(r, c)` be the apex of the pyramid, and its height be `h`. Then, the plot comprises of cells `(i, j)` where `r <= i <= r + h - 1` **and** `c - (i - r) <= j <= c + (i - r)`.

An **inverse pyramidal plot** of land can be defined as a set of cells with similar criteria:

The number of cells in the set has to be **greater than **`1` and all cells must be **fertile**. 
 The **apex** of an inverse pyramid is the **bottommost** cell of the inverse pyramid. The **height** of an inverse pyramid is the number of rows it covers. Let `(r, c)` be the apex of the pyramid, and its height be `h`. Then, the plot comprises of cells `(i, j)` where `r - h + 1 <= i <= r` **and** `c - (r - i) <= j <= c + (r - i)`.

Some examples of valid and invalid pyramidal (and inverse pyramidal) plots are shown below. Black cells indicate fertile cells.

Given a **0-indexed** `m x n` binary matrix `grid` representing the farmland, return *the **total number** of pyramidal and inverse pyramidal plots that can be found in* `grid`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 1000`
- `1 <= m * n <= 10^5`
- `grid[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `grid = [[0,1,1,0],[1,1,1,1]]`
- **Output:** `2`
- **Explanation:** The 2 possible pyramidal plots are shown in blue and red respectively.
There are no inverse pyramidal plots in this grid. 
Hence total number of pyramidal and inverse pyramidal plots is 2 + 0 = 2.

### Example 2
- **Input:** `grid = [[1,1,1],[1,1,1]]`
- **Output:** `2`
- **Explanation:** The pyramidal plot is shown in blue, and the inverse pyramidal plot is shown in red. 
Hence the total number of plots is 1 + 1 = 2.

### Example 3
- **Input:** `grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]`
- **Output:** `13`
- **Explanation:** There are 7 pyramidal plots, 3 of which are shown in the 2nd and 3rd figures.
There are 6 inverse pyramidal plots, 2 of which are shown in the last figure.
The total number of plots is 7 + 6 = 13.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Fertile Pyramids in a Land**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1,1,0],[1,1,1,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The 2 possible pyramidal plots are shown in blue and red respectively.
There are no inverse pyramidal plots in this grid. 
Hence total number of pyramidal and inverse pyramidal plots is 2 + 0 = 2.

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
class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def count(g):
            m, n = len(g), len(g[0])
            dp = [[0] * n for _ in range(m)]
            res = 0
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 0:
                        continue
                    if i == 0 or j == 0 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + 1
                    res += dp[i][j] - 1
            return res

        return count(grid) + count(grid[::-1])
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
- [1162. As Far from Land as Possible](../../1001-1500/1162-as-far-from-land-as-possible/)
- [3633. Earliest Finish Time for Land and Water Rides I](../../3501-4000/3633-earliest-finish-time-for-land-and-water-rides-i/)
- [3635. Earliest Finish Time for Land and Water Rides II](../../3501-4000/3635-earliest-finish-time-for-land-and-water-rides-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-fertile-pyramids-in-a-land/)
