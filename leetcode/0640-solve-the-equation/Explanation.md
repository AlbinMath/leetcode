# LeetCode 640: Solve the Equation

**LeetCode Problem #640 — Solve the Equation**
Solve LeetCode Solve the Equation using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Solve the Equation |
| LeetCode | #640 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Solve a given equation and return the value of  &#39;x&#39;  in the form of a string  "x=#value" . The equation contains only  &#39;+&#39; ,  &#39;-&#39;  operation, the variable  &#39;x&#39;  and its coefficient. You should return  "No solution"  if there is no solution for the equation, or  "Infinite solutions"  if there are infinite solutions for the equation.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Solve the Equation**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1237. Find Positive Integer Solution for a Given Equation](../1358-find-positive-integer-solution-for-a-given-equation/)
- [1499. Max Value of Equation](../1622-max-value-of-equation/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/solve-the-equation/)
