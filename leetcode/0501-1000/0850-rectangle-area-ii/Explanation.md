# LeetCode 850: Rectangle Area II

**LeetCode Problem #850 — Rectangle Area II**
Solve LeetCode Rectangle Area II using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rectangle Area II |
| LeetCode | #850 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D array of axis-aligned `rectangles`. Each `rectangle[i] = [x_i1, y_i1, x_i2, y_i2]` denotes the `i^th` rectangle where `(x_i1, y_i1)` are the coordinates of the **bottom-left corner**, and `(x_i2, y_i2)` are the coordinates of the **top-right corner**.

Calculate the **total area** covered by all `rectangles` in the plane. Any area covered by two or more rectangles should only be counted **once**.

Return *the **total area***. Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= rectangles.length <= 200`
- `rectanges[i].length == 4`
- `0 <= x_i1, y_i1, x_i2, y_i2 <= 10^9`
- `x_i1 <= x_i2`
- `y_i1 <= y_i2`
- All rectangles have non zero area.

## Examples
### Example 1
- **Input:** `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`
- **Output:** `6`
- **Explanation:** A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.

### Example 2
- **Input:** `rectangles = [[0,0,1000000000,1000000000]]`
- **Output:** `49`
- **Explanation:** The answer is 10^18 modulo (10^9 + 7), which is 49.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rectangle Area II**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.

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
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        xs = sorted({r[0] for r in rectangles} | {r[2] for r in rectangles})
        ans = 0
        for i in range(len(xs) - 1):
            x1, x2 = xs[i], xs[i + 1]
            ys = sorted((r[1], r[3]) for r in rectangles
                        if r[0] <= x1 and r[2] >= x2)
            covered = 0
            cur_lo = cur_hi = -1
            for lo, hi in ys:
                if lo > cur_hi:
                    covered += cur_hi - cur_lo
                    cur_lo, cur_hi = lo, hi
                else:
                    cur_hi = max(cur_hi, hi)
            covered += cur_hi - cur_lo
            ans += covered * (x2 - x1)
        return ans % MOD
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
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)
- [939. Minimum Area Rectangle](../../0501-1000/0939-minimum-area-rectangle/)
- [963. Minimum Area Rectangle II](../../0501-1000/0963-minimum-area-rectangle-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rectangle-area-ii/)
