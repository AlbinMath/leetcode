# LeetCode 3905: Multi Source Flood Fill

**LeetCode Problem #3905 — Multi Source Flood Fill**
Solve LeetCode Multi Source Flood Fill using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Multi Source Flood Fill |
| LeetCode | #3905 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `n` and `m` representing the number of rows and columns of a grid, respectively.

You are also given a 2D integer array `sources`, where `sources[i] = [r_i, c_i, color_​​​​​​​i]` indicates that the cell `(r_i, c_i)` is initially colored with `color_i`. All other cells are initially uncolored and represented as 0.

At each time step, every currently colored cell spreads its color to all adjacent **uncolored** cells in the four directions: up, down, left, and right. All spreads happen simultaneously.

If **multiple** colors reach the same uncolored cell at the same time step, the cell takes the color with the **maximum** value.

The process continues until no more cells can be colored.

Return a 2D integer array representing the final state of the grid, where each cell contains its final color.

## Constraints
- `1 <= n, m <= 10^5`
- `1 <= n * m <= 10^5`
- `1 <= sources.length <= n * m`
- `sources[i] = [r_i, c_i, color_i]`
- `0 <= r_i <= n - 1`
- `0 <= c_i <= m - 1`
- `1 <= color_i <= 10^6​​​​​​​`
- All `(r_i, c_i​​​​​​​)` in `sources` are distinct.

## Examples
### Example 1
- **Input:** `n = 3, m = 3, sources = [[0,0,1],[2,2,2]]`
- **Output:** `[[1,1,2],[1,2,2],[2,2,2]]`
- **Explanation:** The grid at each time step is as follows: 

 ​​​​​​​ 

 At time step 2, cells `(0, 2)`, `(1, 1)`, and `(2, 0)` are reached by both colors, so they are assigned color 2 as it has the maximum value among them.

### Example 2
- **Input:** `n = 3, m = 3, sources = [[0,1,3],[1,1,5]]`
- **Output:** `[[3,3,3],[5,5,5],[5,5,5]]`
- **Explanation:** The grid at each time step is as follows:

### Example 3
- **Input:** `n = 2, m = 2, sources = [[1,1,5]]`
- **Output:** `[[5,5],[5,5]]`
- **Explanation:** The grid at each time step is as follows: 

 ​​​​​​​ 

 Since there is only one source, all cells are assigned the same color.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Multi Source Flood Fill**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, m = 3, sources = [[0,0,1],[2,2,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,1,2],[1,2,2],[2,2,2]]`.
4. **Verification:** The grid at each time step is as follows: 

 ​​​​​​​ 

 At time step 2, cells `(0, 2)`, `(1, 1)`, and `(2, 0)` are reached by both colors, so they are assigned color 2 as it has the maximum value among them.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def colorGrid(self, n: int, m: int, sources: List[List[int]]) -> List[List[int]]:
        grid = [[0] * m for _ in range(n)]
        frontier = []
        for r, c, col in sources:
            grid[r][c] = col
            frontier.append((r, c))

        while frontier:
            new = {}  # (r, c) -> max color arriving this step
            for r, c in frontier:
                col = grid[r][c]
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        if new.get((nr, nc), 0) < col:
                            new[(nr, nc)] = col
            for (r, c), col in new.items():
                grid[r][c] = col
            frontier = list(new.keys())
        return grid
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [733. Flood Fill](../../0501-1000/0733-flood-fill/)
- [797. All Paths From Source to Target](../../0501-1000/0797-all-paths-from-source-to-target/)
- [1488. Avoid Flood in The City](../../1001-1500/1488-avoid-flood-in-the-city/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/multi-source-flood-fill/)
