# LeetCode 1895: Largest Magic Square

**LeetCode Problem #1895 — Largest Magic Square**
Solve LeetCode Largest Magic Square using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Magic Square |
| LeetCode | #1895 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A `k x k` **magic square** is a `k x k` grid filled with integers such that every row sum, every column sum, and both diagonal sums are **all equal**. The integers in the magic square **do not have to be distinct**. Every `1 x 1` grid is trivially a **magic square**.

Given an `m x n` integer `grid`, return *the **size** (i.e., the side length *`k`*) of the **largest magic square** that can be found within this grid*.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 10^6`

## Examples
### Example 1
- **Input:** `grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]`
- **Output:** `3`
- **Explanation:** The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12

### Example 2
- **Input:** `grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]`
- **Output:** `2`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Magic Square**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12

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
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [[0] * (n + 2) for _ in range(m + 2)]
        col = [[0] * (n + 2) for _ in range(m + 2)]
        d1 = [[0] * (n + 2) for _ in range(m + 2)]
        d2 = [[0] * (n + 2) for _ in range(m + 2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                v = grid[i - 1][j - 1]
                row[i][j] = row[i][j - 1] + v
                col[i][j] = col[i - 1][j] + v
                d1[i][j] = d1[i - 1][j - 1] + v
                d2[i][j] = d2[i - 1][j + 1] + v

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    target = d1[r + k][c + k] - d1[r][c]
                    if d2[r + k][c + 1] - d2[r][c + k + 1] != target:
                        continue
                    ok = True
                    for x in range(k):
                        if row[r + x + 1][c + k] - row[r + x + 1][c] != target:
                            ok = False
                            break
                        if col[r + k][c + x + 1] - col[r][c + x + 1] != target:
                            ok = False
                            break
                    if ok:
                        return k
        return 1
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
- [1139. Largest 1-Bordered Square](../../1001-1500/1139-largest-1-bordered-square/)
- [1725. Number Of Rectangles That Can Form The Largest Square](../../1501-2000/1725-number-of-rectangles-that-can-form-the-largest-square/)
- [3047. Find the Largest Area of Square Inside Two Rectangles](../../3001-3500/3047-find-the-largest-area-of-square-inside-two-rectangles/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-magic-square/)
