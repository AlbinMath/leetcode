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

## Problem
You are given a circle represented as  (radius, xCenter, yCenter)  and an axis-aligned rectangle represented as  (x1, y1, x2, y2) , where  (x1, y1)  are the coordinates of the bottom-left corner, and  (x2, y2)  are the coordinates of the top-right corner of the rectangle.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code finds the closest point on the rectangle to the circle's center and checks if it's within the radius. The closest point is found by clamping the center's coordinates to the rectangle's bounds. If the distance from the center to this closest point is ≤ radius, they overlap.

Time and space complexity are both $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Circle and Rectangle Overlapping**. Applying **Mathematical Simulation & Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [84. Largest Rectangle in Histogram](../0084-largest-rectangle-in-histogram/)
- [836. Rectangle Overlap](../0866-rectangle-overlap/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/circle-and-rectangle-overlapping/)
