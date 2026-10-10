# LeetCode 1460: Make Two Arrays Equal by Reversing Subarrays

**LeetCode Problem #1460 — Make Two Arrays Equal by Reversing Subarrays**
Solve LeetCode Make Two Arrays Equal by Reversing Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Two Arrays Equal by Reversing Subarrays |
| LeetCode | #1460 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two integer arrays of equal length  target  and  arr . In one step, you can select any  non-empty subarray  of  arr  and reverse it. You are allowed to make any number of steps.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Make Two Arrays Equal by Reversing Subarrays**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)
- [349. Intersection of Two Arrays](../0349-intersection-of-two-arrays/)
- [350. Intersection of Two Arrays II](../0350-intersection-of-two-arrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/)
