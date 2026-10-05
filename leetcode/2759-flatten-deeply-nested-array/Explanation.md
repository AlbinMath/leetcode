# LeetCode 2759: Convert JSON String to Object

**LeetCode Problem #2759 — Convert JSON String to Object**
Solve LeetCode Convert JSON String to Object using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert JSON String to Object |
| LeetCode | #2759 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  multi-dimensional  array  arr  and a depth  n , return a  flattened  version of that array.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Uses recursion: if depth > 0, iterate through elements. If an element is an array, recursively flatten it with `depth - 1`. Otherwise, add the element directly to the result.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Convert JSON String to Object**. Applying **Iterative Traversal** yields the target result step by step.

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
- [2783. Flight Occupancy and Waitlist Analysis](../2783-nested-array-generator/)
- [33. Search in Rotated Sorted Array](../0033-search-in-rotated-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-deeply-nested-array/)
