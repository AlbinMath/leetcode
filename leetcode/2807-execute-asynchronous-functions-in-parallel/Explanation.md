# LeetCode 2721: Execute Asynchronous Functions in Parallel

**LeetCode Problem #2721 — Execute Asynchronous Functions in Parallel**
Solve LeetCode Execute Asynchronous Functions in Parallel using TypeScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Execute Asynchronous Functions in Parallel |
| LeetCode | #2721 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of asynchronous functions  functions , return a new promise  promise . Each function in the array accepts no arguments and returns a promise. All the promises should be executed in parallel.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Implements `Promise.all` from scratch. Creates a promise that tracks completed count. Each function's result is stored at its index. When all complete, resolve with the results array. If any rejects, immediately reject the outer promise.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Execute Asynchronous Functions in Parallel**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [636. Exclusive Time of Functions](../0636-exclusive-time-of-functions/)
- [2. Add Two Numbers](../0002-add-two-numbers/)
- [9. Palindrome Number](../0009-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/)
