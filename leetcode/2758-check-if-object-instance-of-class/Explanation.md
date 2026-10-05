# LeetCode 2758: Next Day

**LeetCode Problem #2758 — Next Day**
Solve LeetCode Next Day using JavaScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Day |
| LeetCode | #2758 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class&#39;s methods.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Walk up the prototype chain of `obj` using `Object.getPrototypeOf()`. At each step, check if the prototype matches `classFunction.prototype`. Return true if found, false if the chain ends (null).

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Next Day**. Applying **Iterative Traversal** yields the target result step by step.

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
- [1878. Get Biggest Three Rhombus Sums in a Grid](../1878-check-if-array-is-sorted-and-rotated/)
- [2349. Design a Number Container System](../2349-check-if-there-is-a-valid-parentheses-string-path/)
- [2892. Minimizing Array After Replacing Pairs With Their Product](../2892-check-if-array-is-good/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-object-instance-of-class/)
