# LeetCode 1018: Binary Prefix Divisible By 5

**LeetCode Problem #1018 — Binary Prefix Divisible By 5**
Solve LeetCode Binary Prefix Divisible By 5 using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Prefix Divisible By 5 |
| LeetCode | #1018 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a binary array  nums  ( 0-indexed ).

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Prefix Sum Precomputation**. By maintaining state efficiently in a **Prefix Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Binary Prefix Divisible By 5**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [1015. Smallest Integer Divisible by K](../1064-smallest-integer-divisible-by-k/)
- [1590. Make Sum Divisible by P](../1694-make-sum-divisible-by-p/)
- [2183. Count Array Pairs Divisible by K](../2301-count-array-pairs-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-prefix-divisible-by-5/)
