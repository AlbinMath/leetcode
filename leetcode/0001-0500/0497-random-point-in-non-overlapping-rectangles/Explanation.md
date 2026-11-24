# LeetCode 497: Random Point in Non-overlapping Rectangles

**LeetCode Problem #497 — Random Point in Non-overlapping Rectangles**
Solve LeetCode Random Point in Non-overlapping Rectangles using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Random Point in Non-overlapping Rectangles |
| LeetCode | #497 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of non-overlapping axis-aligned rectangles `rects` where `rects[i] = [a_i, b_i, x_i, y_i]` indicates that `(a_i, b_i)` is the bottom-left corner point of the `i^th` rectangle and `(x_i, y_i)` is the top-right corner point of the `i^th` rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

**Note** that an integer point is a point that has integer coordinates.

Implement the `Solution` class:

`Solution(int[][] rects)` Initializes the object with the given rectangles `rects`. 
 `int[] pick()` Returns a random integer point `[u, v]` inside the space covered by one of the given rectangles.

## Constraints
- `1 <= rects.length <= 100`
- `rects[i].length == 4`
- `-10^9 <= a_i < x_i <= 10^9`
- `-10^9 <= b_i < y_i <= 10^9`
- `x_i - a_i <= 2000`
- `y_i - b_i <= 2000`
- All the rectangles do not overlap.
- At most `10^4` calls will be made to `pick`.

## Examples
### Example 1
- **Input:** `["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]`
- **Output:** `[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]`
- **Explanation:** Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // return [1, -2]
solution.pick(); // return [1, -1]
solution.pick(); // return [-1, -2]
solution.pick(); // return [-2, -2]
solution.pick(); // return [0, 0]

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Random Point in Non-overlapping Rectangles**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]`.
4. **Verification:** Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // return [1, -2]
solution.pick(); // return [1, -1]
solution.pick(); // return [-1, -2]
solution.pick(); // return [-2, -2]
solution.pick(); // return [0, 0]

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
import bisect
import random

class Solution(object):

    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        total = 0
        for a, b, x, y in rects:
            total += (x - a + 1) * (y - b + 1)
            self.prefix.append(total)

    def pick(self):
        target = random.randint(1, self.prefix[-1])
        idx = bisect.bisect_left(self.prefix, target)
        a, b, x, y = self.rects[idx]
        return [random.randint(a, x), random.randint(b, y)]
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
- [2250. Count Number of Rectangles Containing Each Point](../../2001-2500/2250-count-number-of-rectangles-containing-each-point/)
- [478. Generate Random Point in a Circle](../../0001-0500/0478-generate-random-point-in-a-circle/)
- [435. Non-overlapping Intervals](../../0001-0500/0435-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/)
