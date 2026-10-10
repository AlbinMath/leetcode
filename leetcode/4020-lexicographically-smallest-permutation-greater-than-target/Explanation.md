# LeetCode 3720: Lexicographically Smallest Permutation Greater Than Target

**LeetCode Problem #3720 — Lexicographically Smallest Permutation Greater Than Target**
Solve LeetCode Lexicographically Smallest Permutation Greater Than Target using C++ and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest Permutation Greater Than Target |
| LeetCode | #3720 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two strings  s  and  target , both having length  n , consisting of lowercase English letters.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Lexicographically Smallest Permutation Greater Than Target**. Applying **Backtracking Recursive Search** yields the target result step by step.

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
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../4037-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [744. Find Smallest Letter Greater Than Target](../0745-find-smallest-letter-greater-than-target/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)
