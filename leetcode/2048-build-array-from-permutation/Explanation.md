# LeetCode 1920: Build Array from Permutation

**LeetCode Problem #1920 — Build Array from Permutation**
Solve LeetCode Build Array from Permutation using C++ and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Build Array from Permutation |
| LeetCode | #1920 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a  zero-based permutation   nums  ( 0-indexed ), build an array  ans  of the  same length  where  ans[i] = nums[nums[i]]  for each  0 <= i < nums.length  and return it.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Backtracking Recursive Search**. By maintaining state efficiently in a **Recursion Tree**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Build Array from Permutation**. Applying **Backtracking Recursive Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [26. Remove Duplicates from Sorted Array](../0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../0080-remove-duplicates-from-sorted-array-ii/)
- [1441. Build an Array With Stack Operations](../1552-build-an-array-with-stack-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/build-array-from-permutation/)
