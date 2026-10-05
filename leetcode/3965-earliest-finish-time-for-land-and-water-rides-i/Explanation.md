# LeetCode 3965: Finish Time of Tasks I

**LeetCode Problem #3965 — Finish Time of Tasks I**
Solve LeetCode Finish Time of Tasks I using Kotlin and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Finish Time of Tasks I |
| LeetCode | #3965 |
| Difficulty | Medium |
| Language | Kotlin |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two categories of theme park attractions:  land rides  and  water rides .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Finish Time of Tasks I**. Applying **Iterative Traversal** yields the target result step by step.

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
- [3967. Finish Time of Tasks II](../3967-earliest-finish-time-for-land-and-water-rides-ii/)
- [11. Container With Most Water](../0011-container-with-most-water/)
- [636. Exclusive Time of Functions](../0636-exclusive-time-of-functions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/)
