# LeetCode 1139: Largest 1-Bordered Square

**LeetCode Problem #1139 — Largest 1-Bordered Square**
Solve LeetCode Largest 1-Bordered Square using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest 1-Bordered Square |
| LeetCode | #1139 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a 2D  grid  of  0 s and  1 s, return the number of elements in the largest  square  subgrid that has all  1 s on its  border , or  0  if such a subgrid doesn&#39;t exist in the  grid .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest 1-Bordered Square**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1725. Number Of Rectangles That Can Form The Largest Square](../1843-number-of-rectangles-that-can-form-the-largest-square/)
- [3047. Find the Largest Area of Square Inside Two Rectangles](../3325-find-the-largest-area-of-square-inside-two-rectangles/)
- [191. Number of 1 Bits](../0191-number-of-1-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-1-bordered-square/)
