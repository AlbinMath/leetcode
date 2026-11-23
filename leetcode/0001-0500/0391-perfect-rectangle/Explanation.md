# LeetCode 391: Perfect Rectangle

**LeetCode Problem #391 — Perfect Rectangle**
Solve LeetCode Perfect Rectangle using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Perfect Rectangle |
| LeetCode | #391 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `rectangles` where `rectangles[i] = [x_i, y_i, a_i, b_i]` represents an axis-aligned rectangle. The bottom-left point of the rectangle is `(x_i, y_i)` and the top-right point of it is `(a_i, b_i)`.

Return `true` *if all the rectangles together form an exact cover of a rectangular region*.

## Constraints
- `1 <= rectangles.length <= 2 * 10^4`
- `rectangles[i].length == 4`
- `-10^5 <= x_i < a_i <= 10^5`
- `-10^5 <= y_i < b_i <= 10^5`

## Examples
### Example 1
- **Input:** `rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]`
- **Output:** `true`
- **Explanation:** All 5 rectangles together form an exact cover of a rectangular region.

### Example 2
- **Input:** `rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]`
- **Output:** `false`
- **Explanation:** Because there is a gap between the two rectangular regions.

### Example 3
- **Input:** `rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]`
- **Output:** `false`
- **Explanation:** Because two of the rectangles overlap with each other.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Perfect Rectangle**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** All 5 rectangles together form an exact cover of a rectangular region.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0
        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')
        for a, b, c, d in rectangles:
            area += (c - a) * (d - b)
            x1, y1 = min(x1, a), min(y1, b)
            x2, y2 = max(x2, c), max(y2, d)
            for p in ((a, b), (a, d), (c, b), (c, d)):
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
        if area != (x2 - x1) * (y2 - y1):
            return False
        return corners == {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [84. Largest Rectangle in Histogram](../../0001-0500/0084-largest-rectangle-in-histogram/)
- [85. Maximal Rectangle](../../0001-0500/0085-maximal-rectangle/)
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/perfect-rectangle/)
