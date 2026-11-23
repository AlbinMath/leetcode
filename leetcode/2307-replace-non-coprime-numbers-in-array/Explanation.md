# LeetCode 2197: Replace Non-Coprime Numbers in Array

**LeetCode Problem #2197 — Replace Non-Coprime Numbers in Array**
Solve LeetCode Replace Non-Coprime Numbers in Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace Non-Coprime Numbers in Array |
| LeetCode | #2197 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of integers  nums . Perform the following steps:

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Replace Non-Coprime Numbers in Array**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1969. Minimum Non-Zero Product of the Array Elements](../2100-minimum-non-zero-product-of-the-array-elements/)
- [2289. Steps to Make Array Non-decreasing](../2374-steps-to-make-array-non-decreasing/)
- [2945. Find Maximum Non-decreasing Array Length](../3211-find-maximum-non-decreasing-array-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)
