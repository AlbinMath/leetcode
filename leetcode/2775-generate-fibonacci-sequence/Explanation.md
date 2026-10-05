# LeetCode 2775: Undefined to Null

**LeetCode Problem #2775 — Undefined to Null**
Solve LeetCode Undefined to Null using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Undefined to Null |
| LeetCode | #2775 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write a generator function that returns a generator object which yields the  fibonacci sequence .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a generator function (`function*`) that maintains two variables `a` and `b`. In an infinite loop, it `yield`s `a`, then updates: `[a, b] = [b, a + b]`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Undefined to Null**. Applying **Iterative Traversal** yields the target result step by step.

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
- [3584. Maximum Product of First and Last Elements of a Subsequence](../3584-find-the-lexicographically-smallest-valid-sequence/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-fibonacci-sequence/)
