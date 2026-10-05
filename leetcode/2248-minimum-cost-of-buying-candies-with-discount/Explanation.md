# LeetCode 2248: Intersection of Multiple Arrays

**LeetCode Problem #2248 — Intersection of Multiple Arrays**
Solve LeetCode Intersection of Multiple Arrays using Kotlin and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Intersection of Multiple Arrays |
| LeetCode | #2248 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
A shop is selling candies at a discount. For  every two  candies sold, the shop gives a  third  candy for  free .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Sort costs in descending order. Every third candy (index 2, 5, 8, ...) is free. Sum all costs except every third one.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Intersection of Multiple Arrays**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)

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
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)
- [1570. Dot Product of Two Sparse Vectors](../1570-final-prices-with-a-special-discount-in-a-shop/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)
