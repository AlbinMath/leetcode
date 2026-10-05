# LeetCode 2859: Sum of Values at Indices With K Set Bits

**LeetCode Problem #2859 — Sum of Values at Indices With K Set Bits**
Solve LeetCode Sum of Values at Indices With K Set Bits using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Values at Indices With K Set Bits |
| LeetCode | #2859 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two promises  promise1  and  promise2 , return a new promise.  promise1  and  promise2  will both resolve with a number. The returned promise should resolve with the sum of the two numbers.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
`const [a, b] = await Promise.all([promise1, promise2]); return a + b;` — waits for both promises in parallel and returns their sum.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sum of Values at Indices With K Set Bits**. Applying **Iterative Traversal** yields the target result step by step.

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
- [2. Add Two Numbers](../0002-add-two-numbers/)
- [1. Two Sum](../0001-two-sum/)
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-two-promises/)
