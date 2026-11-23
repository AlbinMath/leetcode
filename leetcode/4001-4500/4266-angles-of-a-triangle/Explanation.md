# LeetCode 3899: Angles of a Triangle

**LeetCode Problem #3899 — Angles of a Triangle**
Solve LeetCode Angles of a Triangle using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Angles of a Triangle |
| LeetCode | #3899 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer array `sides` of length 3.

Determine if there exists a triangle with **positive** area whose three side lengths are given by the elements of `sides`.

If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in **degrees**), **sorted** in **non-decreasing** order. Otherwise, return an empty array.

Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `sides.length == 3`
- `1 <= sides[i] <= 1000`

## Examples
### Example 1
- **Input:** `sides = [3,4,5]`
- **Output:** `[36.86990,53.13010,90.00000]`
- **Explanation:** You can form a right-angled triangle with side lengths 3, 4, and 5. The internal angles of this triangle are approximately 36.869897646, 53.130102354, and 90 degrees respectively.

### Example 2
- **Input:** `sides = [2,4,2]`
- **Output:** `[]`
- **Explanation:** You cannot form a triangle with positive area using side lengths 2, 4, and 2.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Angles of a Triangle**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `sides = [3,4,5]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[36.86990,53.13010,90.00000]`.
4. **Verification:** You can form a right-angled triangle with side lengths 3, 4, and 5. The internal angles of this triangle are approximately 36.869897646, 53.130102354, and 90 degrees respectively.

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
from math import acos, degrees
from typing import List

class Solution:
    def internalAngles(self, sides: List[int]) -> List[float]:
        a, b, c = sorted(sides)
        if a + b <= c:
            return []

        def angle(opp, s1, s2):
            cos_v = (s1 * s1 + s2 * s2 - opp * opp) / (2 * s1 * s2)
            cos_v = max(-1.0, min(1.0, cos_v))   # guard against float drift
            return degrees(acos(cos_v))

        return sorted([angle(a, b, c), angle(b, a, c), angle(c, a, b)])
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
- [118. Pascal's Triangle](../../0001-0500/0118-pascals-triangle/)
- [119. Pascal's Triangle II](../../0001-0500/0119-pascals-triangle-ii/)
- [120. Triangle](../../0001-0500/0120-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/angles-of-a-triangle/)
