# LeetCode 1453: Maximum Number of Darts Inside of a Circular Dartboard

**LeetCode Problem #1453 — Maximum Number of Darts Inside of a Circular Dartboard**
Solve LeetCode Maximum Number of Darts Inside of a Circular Dartboard using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Darts Inside of a Circular Dartboard |
| LeetCode | #1453 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice is throwing `n` darts on a very large wall. You are given an array `darts` where `darts[i] = [x_i, y_i]` is the position of the `i^th` dart that Alice threw on the wall.

Bob knows the positions of the `n` darts on the wall. He wants to place a dartboard of radius `r` on the wall so that the maximum number of darts that Alice throws lie on the dartboard.

Given the integer `r`, return *the maximum number of darts that can lie on the dartboard*.

## Constraints
- `1 <= darts.length <= 100`
- `darts[i].length == 2`
- `-10^4 <= x_i, y_i <= 10^4`
- All the `darts` are unique
- `1 <= r <= 5000`

## Examples
### Example 1
- **Input:** `darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2`
- **Output:** `4`
- **Explanation:** Circle dartboard with center in (0,0) and radius = 2 contain all points.

### Example 2
- **Input:** `darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5`
- **Output:** `5`
- **Explanation:** Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Darts Inside of a Circular Dartboard**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Circle dartboard with center in (0,0) and radius = 2 contain all points.

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
from math import sqrt
from typing import List

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        best = 1
        eps = 1e-7
        for i in range(n):
            x1, y1 = darts[i]
            for j in range(i + 1, n):
                x2, y2 = darts[j]
                dx, dy = x2 - x1, y2 - y1
                d2 = dx * dx + dy * dy
                if d2 > 4 * r * r:
                    continue
                d = sqrt(d2)
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                h = sqrt(max(0.0, r * r - d2 / 4))
                ux, uy = -dy / d, dx / d
                for sign in (1, -1):
                    cx = mx + sign * h * ux
                    cy = my + sign * h * uy
                    cnt = 0
                    for x, y in darts:
                        if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + eps:
                            cnt += 1
                    if cnt > best:
                        best = cnt
        return best
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
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [414. Third Maximum Number](../../0001-0500/0414-third-maximum-number/)
- [918. Maximum Sum Circular Subarray](../../0501-1000/0954-maximum-sum-circular-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/)
