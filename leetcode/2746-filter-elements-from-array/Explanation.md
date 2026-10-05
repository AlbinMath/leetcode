# LeetCode 2746: Decremental String Concatenation

**LeetCode Problem #2746 — Decremental String Concatenation**
Solve LeetCode Decremental String Concatenation using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decremental String Concatenation |
| LeetCode | #2746 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  arr  and a filtering function  fn , return a filtered array  filteredArr .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Iterates through the array, calls `fn(arr[i], i)` for each element, and pushes elements to the result array when the callback returns a truthy value.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Decremental String Concatenation**. Applying **Iterative Traversal** yields the target result step by step.

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
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../1574-maximum-product-of-two-elements-in-an-array/)
- [2212. Maximum Points in an Archery Competition](../2212-removing-minimum-and-maximum-from-array/)
- [3219. Minimum Cost for Cutting Cake II](../3219-make-lexicographically-smallest-array-by-swapping-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/filter-elements-from-array/)
