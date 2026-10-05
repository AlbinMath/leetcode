# LeetCode 4020: Elevator Requests I

**LeetCode Problem #4020 — Elevator Requests I**
Solve LeetCode Elevator Requests I using C++ and Array / General. This solution finds the optimal result using Iterative Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Elevator Requests I |
| LeetCode | #4020 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Iterative Traversal |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings  s  and  target , both having length  n , consisting of lowercase English letters.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Iterative Traversal**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Elevator Requests I**. Applying **Iterative Traversal** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [4037. Maximum Valid Split Positions II](../4037-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [3236. CEO Subordinate Hierarchy](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)
- [3150. Invalid Tweets II](../3150-shortest-and-lexicographically-smallest-beautiful-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)
