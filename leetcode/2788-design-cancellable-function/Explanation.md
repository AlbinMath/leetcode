# LeetCode 2788: Split Strings by Separator

**LeetCode Problem #2788 — Split Strings by Separator**
Solve LeetCode Split Strings by Separator using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Strings by Separator |
| LeetCode | #2788 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Sometimes you have a long running task, and you may wish to cancel it before it completes. To help with this goal, write a function  cancellable  that accepts a generator object and returns an array of two values: a  cancel function  and a  promise .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Wraps the generator execution in a promise. Maintains a reference to allow cancellation. When `cancel()` is called, it throws an error into the generator via `generator.throw()`, causing the generator to reject.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Split Strings by Separator**. Applying **Iterative Traversal** yields the target result step by step.

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
- [2741. Special Permutations](../2741-function-composition/)
- [2790. Maximum Number of Groups With Increasing Length](../2790-call-function-with-custom-context/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-cancellable-function/)
