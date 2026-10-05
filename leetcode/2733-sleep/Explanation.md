# LeetCode 2733: Neither Minimum nor Maximum

**LeetCode Problem #2733 — Neither Minimum nor Maximum**
Solve LeetCode Neither Minimum nor Maximum using JavaScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Neither Minimum nor Maximum |
| LeetCode | #2733 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a positive integer  millis , write an asynchronous function that sleeps for  millis  milliseconds. It can resolve any value.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Returns `new Promise(resolve => setTimeout(resolve, millis))`. The `setTimeout` schedules the `resolve` callback after the specified delay, making the promise resolve after that time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Neither Minimum nor Maximum**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)
- [14. Longest Common Prefix](../0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sleep/)
