# LeetCode 350: Intersection of Two Arrays II

**LeetCode Problem #350 — Intersection of Two Arrays II**
Solve LeetCode Intersection of Two Arrays II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Intersection of Two Arrays II |
| LeetCode | #350 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two integer arrays  nums1  and  nums2 , return  an array of their intersection . Each element in the result must appear as many times as it shows in both arrays and you may return the result in  any order .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Intersection of Two Arrays II**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [349. Intersection of Two Arrays](../0349-intersection-of-two-arrays/)
- [4. Median of Two Sorted Arrays](../0004-median-of-two-sorted-arrays/)
- [160. Intersection of Two Linked Lists](../0160-intersection-of-two-linked-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
