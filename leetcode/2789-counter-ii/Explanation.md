# LeetCode 2789: Largest Element in an Array after Merge Operations

**LeetCode Problem #2789 — Largest Element in an Array after Merge Operations**
Solve LeetCode Largest Element in an Array after Merge Operations using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Element in an Array after Merge Operations |
| LeetCode | #2789 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write a function  createCounter . It should accept an initial integer  init . It should return an object with three functions.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses a closure to capture `init` and a mutable `count` variable. `increment` returns `++count`, `decrement` returns `--count`, and `reset` sets `count = init` and returns it.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Element in an Array after Merge Operations**. Applying **Iterative Traversal** yields the target result step by step.

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
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [602. Friend Requests II: Who Has the Most Friends](../0602-friend-requests-ii-who-has-the-most-friends/)
- [977. Squares of a Sorted Array](../0977-distinct-subsequences-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/counter-ii/)
