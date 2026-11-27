# LeetCode 4052: Cyclically Shift Rows and Columns

**LeetCode Problem #4052 — Cyclically Shift Rows and Columns**
Solve LeetCode Cyclically Shift Rows and Columns using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cyclically Shift Rows and Columns |
| LeetCode | #4052 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`, a 2D integer array `grid` of size `n x n`, and two integer arrays `rowShift` and `colShift`, each of length `n`, where:

`rowShift[i]` represents the number of positions to **cyclically shift** the `i^th` row of `grid` to the **left**. 
 `colShift[j]` represents the number of positions to **cyclically shift** the `j^th` column of `grid` **upward**.

First, cyclically shift each row according to `rowShift`, then cyclically shift each column of the resulting grid according to `colShift`.

Return the resulting grid after performing all the shifts.

A **cyclic left shift** of a row by `k` positions moves the element at column `j` to column `(j - k + n) % n`. All other rows remain unchanged.

A **cyclic upward shift** of a column by `k` positions moves the element at row `i` to row `(i - k + n) % n`. All other columns remain unchanged.

## Constraints
- `1 <= n == grid.length == grid[i].length <= 10`
- `1 <= grid[i][j] <= 100`
- `rowShift.length == colShift.length == n`
- `0 <= rowShift[i], colShift[i] < n`

## Examples
### Example 1
- **Input:** `n = 2, `grid` = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1]`
- **Output:** `[[2,4],[3,1]]`
- **Explanation:** The `grid` changes as follows:

### Example 2
- **Input:** `n = 3, `grid` = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1]`
- **Output:** `[[7,8,5],[2,3,9],[6,4,1]]`
- **Explanation:** The `grid` changes as follows:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Cyclically Shift Rows and Columns**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, `grid` = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[2,4],[3,1]]`.
4. **Verification:** The `grid` changes as follows:

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
    def cyclicShift(self, n: int, grid: list[list[int]],
                    rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        # shift rows left
        rows = [grid[i][rowShift[i]:] + grid[i][:rowShift[i]] for i in range(n)]
        # shift columns up
        res = [[0] * n for _ in range(n)]
        for j in range(n):
            k = colShift[j]
            for i in range(n):
                res[i][j] = rows[(i + k) % n][j]
        return res
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
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1072-flip-columns-for-maximum-number-of-equal-rows/)
- [2397. Maximum Rows Covered by Columns](../../2001-2500/2397-maximum-rows-covered-by-columns/)
- [1260. Shift 2D Grid](../../1001-1500/1260-shift-2d-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cyclically-shift-rows-and-columns/)
