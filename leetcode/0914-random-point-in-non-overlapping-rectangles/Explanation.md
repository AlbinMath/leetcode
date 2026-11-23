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

## Problem
You are given an array of non-overlapping axis-aligned rectangles  rects  where  rects[i] = [a i , b i , x i , y i ]  indicates that  (a i , b i )  is the bottom-left corner point of the  i th   rectangle and  (x i , y i )  is the top-right corner point of the  i th   rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Mathematical Simulation & Modular Arithmetic**. By maintaining state efficiently in a **Primitive Types**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Random Point in Non-overlapping Rectangles**. Applying **Mathematical Simulation & Modular Arithmetic** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [435. Non-overlapping Intervals](../0435-non-overlapping-intervals/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../1096-maximum-sum-of-two-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/)
