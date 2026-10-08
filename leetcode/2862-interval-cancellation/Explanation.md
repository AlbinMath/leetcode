# LeetCode 2725: Interval Cancellation

**LeetCode Problem #2725 — Interval Cancellation**
Solve LeetCode Interval Cancellation using TypeScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Interval Cancellation |
| LeetCode | #2725 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a function  fn , an array of arguments  args , and an interval time  t , return a cancel function  cancelFn .

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Calls `fn(...args)` immediately, then starts `setInterval(fn, t, ...args)`. Returns a function that calls `clearInterval` to cancel the repeating execution.

## Algorithm
1. Initialize state variables / data structure (**Heap / Priority Queue**).
2. Process elements sequentially using **Min/Max Heap Priority Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Interval Cancellation**. Applying **Min/Max Heap Priority Selection** yields the target result step by step.

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
- [57. Insert Interval](../0057-insert-interval/)
- [12. Integer to Roman](../0012-integer-to-roman/)
- [56. Merge Intervals](../0056-merge-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/interval-cancellation/)
