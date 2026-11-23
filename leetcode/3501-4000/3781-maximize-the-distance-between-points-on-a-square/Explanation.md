# LeetCode 3464: Maximize the Distance Between Points on a Square

**LeetCode Problem #3464 — Maximize the Distance Between Points on a Square**
Solve LeetCode Maximize the Distance Between Points on a Square using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Distance Between Points on a Square |
| LeetCode | #3464 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer ` side `, representing the edge length of a square with corners at `(0, 0)`, `(0, side)`, `(side, 0)`, and `(side, side)` on a Cartesian plane.

You are also given a **positive** integer `k` and a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinate of a point lying on the **boundary** of the square.

You need to select `k` elements among `points` such that the **minimum** Manhattan distance between any two points is **maximized**.

Return the **maximum** possible **minimum** Manhattan distance between the selected `k` points.

The Manhattan Distance between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.

## Constraints
- `1 <= side <= 10^9`
- `4 <= points.length <= min(4 * side, 15 * 10^3)`
- `points[i] == [x_i, y_i]`
- The input is generated such that:
 
 `points[i]` lies on the boundary of the square.
- All `points[i]` are **unique**.
- `4 <= k <= min(25, points.length)`

## Examples
### Example 1
- **Input:** `side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4`
- **Output:** `2`
- **Explanation:** Select all four points.

### Example 2
- **Input:** `side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4`
- **Output:** `1`
- **Explanation:** Select the points `(0, 0)`, `(2, 0)`, `(2, 2)`, and `(2, 1)`.

### Example 3
- **Input:** `side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5`
- **Output:** `1`
- **Explanation:** Select the points `(0, 0)`, `(0, 1)`, `(0, 2)`, `(1, 2)`, and `(2, 2)`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize the Distance Between Points on a Square**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Select all four points.

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
from bisect import bisect_left
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        pos = []
        for x, y in points:
            if y == 0:
                pos.append(x)
            elif x == side:
                pos.append(side + y)
            elif y == side:
                pos.append(3 * side - x)
            else:
                pos.append(4 * side - y)
        pos.sort()
        n = len(pos)
        total = 4 * side

        def ok(d: int) -> bool:
            nxt = [bisect_left(pos, p + d) for p in pos]
            for i in range(n):
                j = i
                for _ in range(k - 1):
                    j = nxt[j]
                    if j >= n:
                        break
                else:
                    if pos[j] - pos[i] <= total - d:
                        return True
            return False

        lo, hi = 1, side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
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
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0799-minimum-distance-between-bst-nodes/)
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1486-find-the-distance-value-between-two-arrays/)
- [1617. Count Subtrees With Max Distance Between Cities](../../1501-2000/1740-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/)
