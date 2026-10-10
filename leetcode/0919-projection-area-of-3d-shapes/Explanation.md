# LeetCode 883: Projection Area of 3D Shapes

**LeetCode Problem #883 — Projection Area of 3D Shapes**
Solve LeetCode Projection Area of 3D Shapes using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Projection Area of 3D Shapes |
| LeetCode | #883 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an  n x n   grid  where we place some  1 x 1 x 1  cubes that are axis-aligned with the  x ,  y , and  z  axes.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Projection Area of 3D Shapes**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [892. Surface Area of 3D Shapes](../0928-surface-area-of-3d-shapes/)
- [812. Largest Triangle Area](../0830-largest-triangle-area/)
- [1637. Widest Vertical Area Between Two Points Containing No Points](../1742-widest-vertical-area-between-two-points-containing-no-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/projection-area-of-3d-shapes/)
