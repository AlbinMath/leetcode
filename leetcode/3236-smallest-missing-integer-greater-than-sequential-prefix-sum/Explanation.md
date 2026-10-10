# LeetCode 2996: Smallest Missing Integer Greater Than Sequential Prefix Sum

**LeetCode Problem #2996 — Smallest Missing Integer Greater Than Sequential Prefix Sum**
Solve LeetCode Smallest Missing Integer Greater Than Sequential Prefix Sum using Rust and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Integer Greater Than Sequential Prefix Sum |
| LeetCode | #2996 |
| Difficulty | Easy |
| Language | Rust |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Note:  The updated title is  "Smallest Missing Integer Greater Than or Equal to Sequential Prefix Sum".

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Missing Integer Greater Than Sequential Prefix Sum**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Rust

## Source Code
- [solution.rs](./solution.rs)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [744. Find Smallest Letter Greater Than Target](../0745-find-smallest-letter-greater-than-target/)
- [3720. Lexicographically Smallest Permutation Greater Than Target](../4020-lexicographically-smallest-permutation-greater-than-target/)
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../4037-lexicographically-smallest-palindromic-permutation-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/)
