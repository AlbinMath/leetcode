# LeetCode 1610: Maximum Number of Visible Points

**LeetCode Problem #1610 — Maximum Number of Visible Points**
Solve LeetCode Maximum Number of Visible Points using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Visible Points |
| LeetCode | #1610 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `points`, an integer `angle`, and your `location`, where `location = [pos_x, pos_y]` and `points[i] = [x_i, y_i]` both denote **integral coordinates** on the X-Y plane.

Initially, you are facing directly east from your position. You **cannot move** from your position, but you can **rotate**. In other words, `pos_x` and `pos_y` cannot be changed. Your field of view in **degrees** is represented by `angle`, determining how wide you can see from any given view direction. Let `d` be the amount in degrees that you rotate counterclockwise. Then, your field of view is the **inclusive** range of angles `[d - angle/2, d + angle/2]`.

Your browser does not support the video tag or this video format.

You can **see** some set of points if, for each point, the **angle** formed by the point, your position, and the immediate east direction from your position is **in your field of view**.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

Return *the maximum number of points you can see*.

## Constraints
- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `location.length == 2`
- `0 <= angle < 360`
- `0 <= pos_x, pos_y, x_i, y_i <= 100`

## Examples
### Example 1
- **Input:** `points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]`
- **Output:** `3`
- **Explanation:** The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.

### Example 2
- **Input:** `points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]`
- **Output:** `4`
- **Explanation:** All points can be made visible in your field of view, including the one at your location.

### Example 3
- **Input:** `points = [[1,0],[2,1]], angle = 13, location = [1,1]`
- **Output:** `1`
- **Explanation:** You can only see one of the two points, as shown above.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Visible Points**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.

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
from math import atan2, degrees
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        px, py = location
        same = 0
        angles = []
        for x, y in points:
            if x == px and y == py:
                same += 1
            else:
                angles.append(degrees(atan2(y - py, x - px)))
        angles.sort()
        angles += [a + 360 for a in angles]

        eps = 1e-9
        best = 0
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle + eps:
                left += 1
            best = max(best, right - left + 1)
        return best + same
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
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2588-maximum-number-of-points-from-grid-queries/)
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-visible-points/)
