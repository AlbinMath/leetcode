# LeetCode 2862: Maximum Element-Sum of a Complete Subset of Indices

**LeetCode Problem #2862 — Maximum Element-Sum of a Complete Subset of Indices**
Solve LeetCode Maximum Element-Sum of a Complete Subset of Indices using TypeScript and Heap. This solution finds the optimal result using Priority Queue Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Element-Sum of a Complete Subset of Indices |
| LeetCode | #2862 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | Priority Queue Selection |
| Data Structure | Min/Max Heap |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a function  fn , an array of arguments  args , and an interval time  t , return a cancel function  cancelFn .

## Key Insight
Leverage **Heap** with **Min/Max Heap** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Calls `fn(...args)` immediately, then starts `setInterval(fn, t, ...args)`. Returns a function that calls `clearInterval` to cancel the repeating execution.

## Algorithm
1. Initialize state variables / data structure (**Min/Max Heap**).
2. Process elements sequentially using **Priority Queue Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Element-Sum of a Complete Subset of Indices**. Applying **Priority Queue Selection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [12. Integer to Roman](../0012-integer-to-roman/)
- [1644. Lowest Common Ancestor of a Binary Tree II](../1644-maximum-number-of-non-overlapping-substrings/)
- [3562. Maximum Profit from Trading Stocks with Discounts](../3562-maximum-score-of-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/interval-cancellation/)
