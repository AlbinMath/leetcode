# LeetCode 2760: Longest Even Odd Subarray With Threshold

**LeetCode Problem #2760 — Longest Even Odd Subarray With Threshold**
Solve LeetCode Longest Even Odd Subarray With Threshold using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Even Odd Subarray With Threshold |
| LeetCode | #2760 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Write code that enhances all arrays such that you can call the  snail(rowsCount, colsCount)  method that transforms the 1D array into a 2D array organised in the pattern known as  snail traversal order . Invalid input values should output an empty array. If  rowsCount * colsCount !== nums.length , the input is considered invalid.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Fills the matrix column by column. Even-indexed columns fill top-to-bottom; odd-indexed columns fill bottom-to-top, creating the snail pattern.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Even Odd Subarray With Threshold**. Applying **Iterative Traversal** yields the target result step by step.

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
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)
- [193. Valid Phone Numbers](../0193-valid-phone-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/snail-traversal/)
