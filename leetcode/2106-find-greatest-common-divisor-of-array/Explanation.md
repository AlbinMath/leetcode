# LeetCode 2106: Maximum Fruits Harvested After at Most K Steps

**LeetCode Problem #2106 — Maximum Fruits Harvested After at Most K Steps**
Solve LeetCode Maximum Fruits Harvested After at Most K Steps using Kotlin and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Fruits Harvested After at Most K Steps |
| LeetCode | #2106 |
| Difficulty | Hard |
| Language | Kotlin |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums , return    the  greatest common divisor  of the smallest number and largest number in   nums .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. Find the minimum and maximum of the array.
2. Compute the GCD of those two values using the Euclidean algorithm.

Time complexity is $O(N + \log(\min))$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Fruits Harvested After at Most K Steps**. Applying **Iterative Traversal** yields the target result step by step.

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
- [2766. Relocate Marbles](../2766-find-the-prefix-common-array-of-two-arrays/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)
