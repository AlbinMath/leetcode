# LeetCode 1401: Circle and Rectangle Overlapping

**LeetCode Problem #1401 — Circle and Rectangle Overlapping**
Solve LeetCode Circle and Rectangle Overlapping using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Circle and Rectangle Overlapping |
| LeetCode | #1401 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a circle represented as `(radius, xCenter, yCenter)` and an axis-aligned rectangle represented as `(x1, y1, x2, y2)`, where `(x1, y1)` are the coordinates of the bottom-left corner, and `(x2, y2)` are the coordinates of the top-right corner of the rectangle.

Return `true`* if the circle and rectangle are overlapped otherwise return *`false`. In other words, check if there is **any** point `(x_i, y_i)` that belongs to the circle and the rectangle at the same time.

## Constraints
- `1 <= radius <= 2000`
- `-10^4 <= xCenter, yCenter <= 10^4`
- `-10^4 <= x1 < x2 <= 10^4`
- `-10^4 <= y1 < y2 <= 10^4`

## Examples
### Example 1
- **Input:** `radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1`
- **Output:** `true`
- **Explanation:** Circle and rectangle share the point (1,0).

### Example 2
- **Input:** `radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1`
- **Output:** `false`

### Example 3
- **Input:** `radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1`
- **Output:** `true`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code finds the closest point on the rectangle to the circle's center and checks if it's within the radius. The closest point is found by clamping the center's coordinates to the rectangle's bounds. If the distance from the center to this closest point is ≤ radius, they overlap.

Time and space complexity are both $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Circle and rectangle share the point (1,0).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} radius
 * @param {number} xCenter
 * @param {number} yCenter
 * @param {number} x1
 * @param {number} y1
 * @param {number} x2
 * @param {number} y2
 * @return {boolean}
 */
var checkOverlap = function(radius, xCenter, yCenter, x1, y1, x2, y2) {
    // Find the closest point in the rectangle to the circle's center
    const closestX = Math.max(x1, Math.min(xCenter, x2));
    const closestY = Math.max(y1, Math.min(yCenter, y2));

    // Distance from circle center to closest point
    const dx = xCenter - closestX;
    const dy = yCenter - closestY;

    // Check if the point is inside or on the circle
    return dx * dx + dy * dy <= radius * radius;
};
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
- [478. Generate Random Point in a Circle](../../0001-0500/0478-generate-random-point-in-a-circle/)
- [1041. Robot Bounded In Circle](../../1001-1500/1041-robot-bounded-in-circle/)
- [1828. Queries on Number of Points Inside a Circle](../../1501-2000/1828-queries-on-number-of-points-inside-a-circle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/circle-and-rectangle-overlapping/)
