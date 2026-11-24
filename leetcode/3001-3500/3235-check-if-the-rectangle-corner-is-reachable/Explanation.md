# LeetCode 3235: Check if the Rectangle Corner Is Reachable

**LeetCode Problem #3235 — Check if the Rectangle Corner Is Reachable**
Solve LeetCode Check if the Rectangle Corner Is Reachable using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if the Rectangle Corner Is Reachable |
| LeetCode | #3235 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integers `xCorner` and `yCorner`, and a 2D array `circles`, where `circles[i] = [x_i, y_i, r_i]` denotes a circle with center at `(x_i, y_i)` and radius `r_i`.

There is a rectangle in the coordinate plane with its bottom left corner at the origin and top right corner at the coordinate `(xCorner, yCorner)`. You need to check whether there is a path from the bottom left corner to the top right corner such that the **entire path** lies inside the rectangle, **does not** touch or lie inside **any** circle, and touches the rectangle **only** at the two corners.

Return `true` if such a path exists, and `false` otherwise.

## Constraints
- `3 <= xCorner, yCorner <= 10^9`
- `1 <= circles.length <= 1000`
- `circles[i].length == 3`
- `1 <= x_i, y_i, r_i <= 10^9`

## Examples
### Example 1
- **Input:** `xCorner = 3, yCorner = 4, circles = [[2,1,1]]`
- **Output:** `true`
- **Explanation:** The black curve shows a possible path between `(0, 0)` and `(3, 4)`.

### Example 2
- **Input:** `xCorner = 3, yCorner = 3, circles = [[1,1,2]]`
- **Output:** `false`
- **Explanation:** No path exists from `(0, 0)` to `(3, 3)`.

### Example 3
- **Input:** `xCorner = 3, yCorner = 3, circles = [[2,1,1],[1,2,1]]`
- **Output:** `false`
- **Explanation:** No path exists from `(0, 0)` to `(3, 3)`.

### Example 4
- **Input:** `xCorner = 4, yCorner = 4, circles = [[5,5,1]]`
- **Output:** `true`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Check if the Rectangle Corner Is Reachable**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `xCorner = 3, yCorner = 4, circles = [[2,1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The black curve shows a possible path between `(0, 0)` and `(3, 4)`.

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
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        parent = list(range(n + 2))
        A, B = n, n + 1          # A = left+top edges, B = bottom+right edges
        X, Y = xCorner, yCorner

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        def clamp(v, lo, hi):
            return max(lo, min(v, hi))

        # a circle covering either corner blocks everything
        for x, y, r in circles:
            if x * x + y * y <= r * r or (x - X) ** 2 + (y - Y) ** 2 <= r * r:
                return False

        # connect circles to the edge segments they actually touch
        for i, (x, y, r) in enumerate(circles):
            r2 = r * r
            if x * x + (y - clamp(y, 0, Y)) ** 2 <= r2:          # left edge
                union(i, A)
            if (y - Y) ** 2 + (x - clamp(x, 0, X)) ** 2 <= r2:   # top edge
                union(i, A)
            if y * y + (x - clamp(x, 0, X)) ** 2 <= r2:          # bottom edge
                union(i, B)
            if (x - X) ** 2 + (y - clamp(y, 0, Y)) ** 2 <= r2:   # right edge
                union(i, B)

        # connect overlapping circles whose contact point lies inside the rectangle
        for i in range(n):
            x1, y1, r1 = circles[i]
            for j in range(i + 1, n):
                x2, y2, r2 = circles[j]
                s = r1 + r2
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= s * s:
                    px = x1 * r2 + x2 * r1          # contact x, scaled by s
                    py = y1 * r2 + y2 * r1
                    if 0 <= px <= X * s and 0 <= py <= Y * s:
                        union(i, j)

        return find(A) != find(B)
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
- [2543. Check if Point Is Reachable](../../2501-3000/2543-check-if-point-is-reachable/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)
- [1232. Check If It Is a Straight Line](../../1001-1500/1232-check-if-it-is-a-straight-line/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/)
