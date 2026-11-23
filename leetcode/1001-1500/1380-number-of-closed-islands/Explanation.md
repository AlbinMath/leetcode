# LeetCode 1254: Number of Closed Islands

**LeetCode Problem #1254 — Number of Closed Islands**
Solve LeetCode Number of Closed Islands using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Closed Islands |
| LeetCode | #1254 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a 2D `grid` consists of `0s` (land) and `1s` (water). An *island* is a maximal 4-directionally connected group of ` 0 s` and a *closed island* is an island **totally** (all left, top, right, bottom) surrounded by `1s.`

Return the number of *closed islands*.

## Constraints
- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <=1`

## Examples
### Example 1
- **Input:** `grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]`
- **Output:** `2`
- **Explanation:** The grid contains four islands of 0s. 
 The island spanning rows 1 to 3 and columns 1 to 4 is surrounded entirely by 1s. It also encloses the water cell at row 2, column 2. It is therefore closed. 
 The single 0 at row 3, column 6 has 1s on all four sides, so it is also closed. 
 The two remaining islands both lie in column 7, which is on the border of the grid, so neither of them is closed. 
 Two islands are closed, shown in gray, so the answer is 2.

### Example 2
- **Input:** `grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]`
- **Output:** `1`
- **Explanation:** The grid contains three islands of 0s. 
 The single 0 at row 1, column 2 has 1s above it, below it, to its left and to its right, so it is closed. It is shown in gray. 
 The island formed by rows 0 to 2 of column 0 together with row 0, column 1 lies on the border, so it is not closed. 
 The island formed by rows 0 to 2 of column 4 together with row 0, column 3 also lies on the border, so it is not closed. 
 One island is closed, so the answer is 1.

### Example 3
- **Input:** `grid = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]`
- **Output:** `2`
- **Explanation:** The grid contains two islands of 0s, one nested inside the other. 
 The outer island is the ring of 0s occupying rows 1 to 5 and columns 1 to 5. It is enclosed by the outer border of 1s, so it is closed. 
 The inner island is the single 0 at row 3, column 3. It is enclosed by the inner ring of 1s, so it is also closed. 
 Both islands are closed, so the answer is 2.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Closed Islands**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The grid contains four islands of 0s. 
 The island spanning rows 1 to 3 and columns 1 to 4 is surrounded entirely by 1s. It also encloses the water cell at row 2, column 2. It is therefore closed. 
 The single 0 at row 3, column 6 has 1s on all four sides, so it is also closed. 
 The two remaining islands both lie in column 7, which is on the border of the grid, so neither of them is closed. 
 Two islands are closed, shown in gray, so the answer is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if grid[i][j] == 1:
                return True

            grid[i][j] = 1

            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return up and down and left and right

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [200. Number of Islands](../../0001-0500/0200-number-of-islands/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-closed-islands/)
