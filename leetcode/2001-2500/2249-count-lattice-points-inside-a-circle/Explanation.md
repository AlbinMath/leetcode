# LeetCode 2249: Count Lattice Points Inside a Circle

**LeetCode Problem #2249 — Count Lattice Points Inside a Circle**
Solve LeetCode Count Lattice Points Inside a Circle using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Lattice Points Inside a Circle |
| LeetCode | #2249 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a 2D integer array `circles` where `circles[i] = [x_i, y_i, r_i]` represents the center `(x_i, y_i)` and radius `r_i` of the `i^th` circle drawn on a grid, return *the **number of lattice points** **that are present inside **at least one** circle*.

**Note:**

A **lattice point** is a point with integer coordinates. 
 Points that lie **on the circumference of a circle** are also considered to be inside it.

## Constraints
- `1 <= circles.length <= 200`
- `circles[i].length == 3`
- `1 <= x_i, y_i <= 100`
- `1 <= r_i <= min(x_i, y_i)`

## Examples
### Example 1
- **Input:** `circles = [[2,2,1]]`
- **Output:** `5`
- **Explanation:** The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.

### Example 2
- **Input:** `circles = [[2,2,2],[3,4,1]]`
- **Output:** `16`
- **Explanation:** The figure above shows the given circles.
There are exactly 16 lattice points which are present inside at least one circle. 
Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Lattice Points Inside a Circle**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `circles = [[2,2,1]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.

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
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        pts = set()
        for cx, cy, r in circles:
            r2 = r * r
            for x in range(cx - r, cx + r + 1):
                dx = x - cx
                for y in range(cy - r, cy + r + 1):
                    dy = y - cy
                    if dx * dx + dy * dy <= r2:
                        pts.add((x, y))
        return len(pts)
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
- [1828. Queries on Number of Points Inside a Circle](../../1501-2000/1828-queries-on-number-of-points-inside-a-circle/)
- [2857. Count Pairs of Points With Distance k](../../2501-3000/2857-count-pairs-of-points-with-distance-k/)
- [38. Count and Say](../../0001-0500/0038-count-and-say/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-lattice-points-inside-a-circle/)
