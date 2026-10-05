# LeetCode 2796: Repeat String

**LeetCode Problem #2796 — Repeat String**
Solve LeetCode Repeat String using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Repeat String |
| LeetCode | #2796 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a function  fn , return a new function that is identical to the original function except that it ensures  fn  is called at most once.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a boolean flag `called` in a closure. On the first call, sets `called = true` and returns the function's result. On subsequent calls, returns `undefined`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Repeat String**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [2790. Maximum Number of Groups With Increasing Length](../2790-call-function-with-custom-context/)
- [396. Rotate Function](../0396-rotate-function/)
- [2319. Check if Matrix Is X-Matrix](../2319-longest-substring-of-one-repeating-character/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/allow-one-function-call/)
