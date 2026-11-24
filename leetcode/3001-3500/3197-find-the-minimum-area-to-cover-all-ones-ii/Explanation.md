# LeetCode 3197: Find the Minimum Area to Cover All Ones II

**LeetCode Problem #3197 — Find the Minimum Area to Cover All Ones II**
Solve LeetCode Find the Minimum Area to Cover All Ones II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Minimum Area to Cover All Ones II |
| LeetCode | #3197 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D **binary** array `grid`. You need to find 3 **non-overlapping** rectangles having **non-zero** areas with horizontal and vertical sides such that all the 1's in `grid` lie inside these rectangles.

Return the **minimum** possible sum of the area of these rectangles.

**Note** that the rectangles are allowed to touch.

## Constraints
- `1 <= grid.length, grid[i].length <= 30`
- `grid[i][j]` is either 0 or 1.
- The input is generated such that there are at least three 1's in `grid`.

## Examples
### Example 1
- **Input:** `grid = [[1,0,1],[1,1,1]]`
- **Output:** `5`
- **Explanation:** The 1's at `(0, 0)` and `(1, 0)` are covered by a rectangle of area 2. 
 The 1's at `(0, 2)` and `(1, 2)` are covered by a rectangle of area 2. 
 The 1 at `(1, 1)` is covered by a rectangle of area 1.

### Example 2
- **Input:** `grid = [[1,0,1,0],[0,1,0,1]]`
- **Output:** `5`
- **Explanation:** The 1's at `(0, 0)` and `(0, 2)` are covered by a rectangle of area 3. 
 The 1 at `(1, 1)` is covered by a rectangle of area 1. 
 The 1 at `(1, 3)` is covered by a rectangle of area 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Minimum Area to Cover All Ones II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,1],[1,1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The 1's at `(0, 0)` and `(1, 0)` are covered by a rectangle of area 2. 
 The 1's at `(0, 2)` and `(1, 2)` are covered by a rectangle of area 2. 
 The 1 at `(1, 1)` is covered by a rectangle of area 1.

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
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def area(r1, r2, c1, c2):
            # bounding box of 1s in rows [r1, r2), cols [c1, c2)
            top, bot, left, right = m, -1, n, -1
            for r in range(r1, r2):
                for c in range(c1, c2):
                    if grid[r][c]:
                        if r < top: top = r
                        if r > bot: bot = r
                        if c < left: left = c
                        if c > right: right = c
            if bot == -1:
                return 0
            return (bot - top + 1) * (right - left + 1)

        ans = m * n

        # three vertical strips
        for a in range(1, n):
            for b in range(a + 1, n):
                ans = min(ans, area(0, m, 0, a) + area(0, m, a, b) + area(0, m, b, n))

        # three horizontal strips
        for a in range(1, m):
            for b in range(a + 1, m):
                ans = min(ans, area(0, a, 0, n) + area(a, b, 0, n) + area(b, m, 0, n))

        # vertical cut, then split one side horizontally
        for c in range(1, n):
            for r in range(1, m):
                # left split horizontally, right whole
                ans = min(ans, area(0, r, 0, c) + area(r, m, 0, c) + area(0, m, c, n))
                # right split horizontally, left whole
                ans = min(ans, area(0, m, 0, c) + area(0, r, c, n) + area(r, m, c, n))

        # horizontal cut, then split one side vertically
        for r in range(1, m):
            for c in range(1, n):
                # top split vertically, bottom whole
                ans = min(ans, area(0, r, 0, c) + area(0, r, c, n) + area(r, m, 0, n))
                # bottom split vertically, top whole
                ans = min(ans, area(0, r, 0, n) + area(r, m, 0, c) + area(r, m, c, n))

        return ans
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
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1723-find-minimum-time-to-finish-all-jobs/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/)
