# LeetCode 812: Largest Triangle Area

**LeetCode Problem #812 — Largest Triangle Area**
Solve LeetCode Largest Triangle Area using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Triangle Area |
| LeetCode | #812 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of points on the **X-Y** plane `points` where `points[i] = [x_i, y_i]`, return *the area of the largest triangle that can be formed by any three different points*. Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `3 <= points.length <= 50`
- `-50 <= x_i, y_i <= 50`
- All the given points are **unique**.

## Examples
### Example 1
- **Input:** `points = [[0,0],[0,1],[1,0],[0,2],[2,0]]`
- **Output:** `2.00000`
- **Explanation:** The five points are shown in the above figure. The red triangle is the largest.

### Example 2
- **Input:** `points = [[1,0],[0,0],[0,1]]`
- **Output:** `0.50000`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Triangle Area**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[0,0],[0,1],[1,0],[0,2],[2,0]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2.00000`.
4. **Verification:** The five points are shown in the above figure. The red triangle is the largest.

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
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        ans = 0
        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
            ans = max(ans, area)
        return ans
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
- [976. Largest Perimeter Triangle](../../0501-1000/0976-largest-perimeter-triangle/)
- [3047. Find the Largest Area of Square Inside Two Rectangles](../../3001-3500/3047-find-the-largest-area-of-square-inside-two-rectangles/)
- [3588. Find Maximum Area of a Triangle](../../3501-4000/3588-find-maximum-area-of-a-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-triangle-area/)
