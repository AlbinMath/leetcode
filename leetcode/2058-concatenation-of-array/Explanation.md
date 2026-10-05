# LeetCode 2058: Find the Minimum and Maximum Number of Nodes Between Critical Points

**LeetCode Problem #2058 — Find the Minimum and Maximum Number of Nodes Between Critical Points**
Solve LeetCode Find the Minimum and Maximum Number of Nodes Between Critical Points using TypeScript and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Minimum and Maximum Number of Nodes Between Critical Points |
| LeetCode | #2058 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums  of length  n , you want to create an array  ans  of length  2n  where  ans[i] == nums[i]  and  ans[i + n] == nums[i]  for  0 <= i < n  ( 0-indexed ).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code creates a new array of size `2n` and copies `nums` twice — once at the beginning and once starting at index `n`. Alternatively, it simply concatenates the array with itself using spread/concat.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Minimum and Maximum Number of Nodes Between Critical Points**. Applying **Iterative Traversal** yields the target result step by step.

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
- [33. Search in Rotated Sorted Array](../0033-search-in-rotated-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenation-of-array/)
