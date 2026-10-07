# LeetCode 2648: Generate Fibonacci Sequence

**LeetCode Problem #2648 — Generate Fibonacci Sequence**
Solve LeetCode Generate Fibonacci Sequence using TypeScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Fibonacci Sequence |
| LeetCode | #2648 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
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
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Generate Fibonacci Sequence**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [22. Generate Parentheses](../0022-generate-parentheses/)
- [60. Permutation Sequence](../0060-permutation-sequence/)
- [3302. Find the Lexicographically Smallest Valid Sequence](../3584-find-the-lexicographically-smallest-valid-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-fibonacci-sequence/)
