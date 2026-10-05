# LeetCode 3349: Adjacent Increasing Subarrays Detection I

**LeetCode Problem #3349 — Adjacent Increasing Subarrays Detection I**
Solve LeetCode Adjacent Increasing Subarrays Detection I using Swift and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Adjacent Increasing Subarrays Detection I |
| LeetCode | #3349 |
| Difficulty | Easy |
| Language | Swift |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string  s , return the  maximum  length of a  substring  such that it contains  at most two occurrences  of each character.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Adjacent Increasing Subarrays Detection I**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Swift

## Source Code
- [solution.swift](./solution.swift)

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
- [1208. Get Equal Substrings Within Budget](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../1574-maximum-product-of-two-elements-in-an-array/)
- [3859. Count Subarrays With K Distinct Integers](../3859-maximum-product-of-two-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)
