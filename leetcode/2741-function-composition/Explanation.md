# LeetCode 2741: Special Permutations

**LeetCode Problem #2741 — Special Permutations**
Solve LeetCode Special Permutations using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Special Permutations |
| LeetCode | #2741 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of functions  [f 1 , f 2 , f 3 , ..., f n ] , return a new function  fn  that is the  function composition  of the array of functions.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses `Array.reduceRight` to apply functions from right to left. The composed function takes input `x`, passes it through the last function first, then feeds each result to the previous function.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Special Permutations**. Applying **Iterative Traversal** yields the target result step by step.

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
- [396. Rotate Function](../0396-rotate-function/)
- [2788. Split Strings by Separator](../2788-design-cancellable-function/)
- [2790. Maximum Number of Groups With Increasing Length](../2790-call-function-with-custom-context/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/function-composition/)
