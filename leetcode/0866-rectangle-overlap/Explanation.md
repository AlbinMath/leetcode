# LeetCode 836: Rectangle Overlap

**LeetCode Problem #836 — Rectangle Overlap**
Solve LeetCode Rectangle Overlap using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rectangle Overlap |
| LeetCode | #836 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
An axis-aligned rectangle is represented as a list  [x1, y1, x2, y2] , where  (x1, y1)  is the coordinate of its bottom-left corner, and  (x2, y2)  is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code checks for overlap by verifying that neither rectangle is entirely to the left, right, above, or below the other. This is equivalent to checking that the intervals overlap in both dimensions:

- `rec1[0] < rec2[2]`: rec1's left edge is to the left of rec2's right edge.
- `rec2[0] < rec1[2]`: rec2's left edge is to the left of rec1's right edge.
- `rec1[1] < rec2[3]`: rec1's bottom edge is below rec2's top edge.
- `rec2[1] < rec1[3]`: rec2's bottom edge is below rec1's top edge.

If all four conditions are true, the rectangles overlap. Time and space complexity are both $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Rectangle Overlap**. Applying **Mathematical Simulation & Modular Arithmetic** yields the target result step by step.

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
- [85. Maximal Rectangle](../0085-maximal-rectangle/)
- [492. Construct the Rectangle](../0492-construct-the-rectangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rectangle-overlap/)
