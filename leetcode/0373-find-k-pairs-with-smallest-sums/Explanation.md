# LeetCode 373: Find K Pairs with Smallest Sums

**LeetCode Problem #373 — Find K Pairs with Smallest Sums**
Solve LeetCode Find K Pairs with Smallest Sums using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find K Pairs with Smallest Sums |
| LeetCode | #373 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two integer arrays  nums1  and  nums2  sorted in  non-decreasing order  and an integer  k .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find K Pairs with Smallest Sums**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [658. Find K Closest Elements](../0658-find-k-closest-elements/)
- [744. Find Smallest Letter Greater Than Target](../0745-find-smallest-letter-greater-than-target/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
