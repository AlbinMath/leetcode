# LeetCode 2144: Minimum Cost of Buying Candies With Discount

**LeetCode Problem #2144 — Minimum Cost of Buying Candies With Discount**
Solve LeetCode Minimum Cost of Buying Candies With Discount using Kotlin and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost of Buying Candies With Discount |
| LeetCode | #2144 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | In-Place Array Traversal & Index Mapping |
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
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost of Buying Candies With Discount**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1475. Final Prices With a Special Discount in a Shop](../1570-final-prices-with-a-special-discount-in-a-shop/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)
