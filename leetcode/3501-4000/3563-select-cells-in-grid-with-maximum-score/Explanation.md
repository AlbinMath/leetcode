# LeetCode 3276: Select Cells in Grid With Maximum Score

**LeetCode Problem #3276 — Select Cells in Grid With Maximum Score**
Solve LeetCode Select Cells in Grid With Maximum Score using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Select Cells in Grid With Maximum Score |
| LeetCode | #3276 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D matrix `grid` consisting of positive integers.

You have to select *one or more* cells from the matrix such that the following conditions are satisfied:

No two selected cells are in the **same** row of the matrix. 
 The values in the set of selected cells are **unique**.

Your score will be the **sum** of the values of the selected cells.

Return the **maximum** score you can achieve.

## Constraints
- `1 <= grid.length, grid[i].length <= 10`
- `1 <= grid[i][j] <= 100`

## Examples
### Example 1
- **Input:** `grid = [[1,2,3],[4,3,2],[1,1,1]]`
- **Output:** `8`
- **Explanation:** We can select the cells with values 1, 3, and 4 that are colored above.

### Example 2
- **Input:** `grid = [[8,7,6],[8,3,2]]`
- **Output:** `15`
- **Explanation:** We can select the cells with values 7 and 8 that are colored above.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Select Cells in Grid With Maximum Score**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,3],[4,3,2],[1,1,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** We can select the cells with values 1, 3, and 4 that are colored above.

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
    def maxScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = {}
        for i, row in enumerate(grid):
            for v in row:
                rows.setdefault(v, set()).add(i)

        dp = [-1] * (1 << n)
        dp[0] = 0
        for v, rs in rows.items():
            new = dp[:]
            for mask in range(1 << n):
                if dp[mask] < 0:
                    continue
                for r in rs:
                    if not mask >> r & 1:
                        nm = mask | (1 << r)
                        if dp[mask] + v > new[nm]:
                            new[nm] = dp[mask] + v
            dp = new
        return max(dp)
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
- [3742. Maximum Path Score in a Grid](../../3501-4000/3986-maximum-path-score-in-a-grid/)
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1381-maximum-score-words-formed-by-letters/)
- [1422. Maximum Score After Splitting a String](../../1501-2000/1537-maximum-score-after-splitting-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/)
