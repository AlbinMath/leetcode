# LeetCode 3105: Longest Strictly Increasing or Strictly Decreasing Subarray

**LeetCode Problem #3105 — Longest Strictly Increasing or Strictly Decreasing Subarray**
Solve LeetCode Longest Strictly Increasing or Strictly Decreasing Subarray using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Strictly Increasing or Strictly Decreasing Subarray |
| LeetCode | #3105 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of integers  nums . Return  the length of the  longest   subarray  of   nums   which is either   strictly increasing   or   strictly decreasing   .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Strictly Increasing or Strictly Decreasing Subarray**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../../4001-4500/4032-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)
- [1370. Increasing Decreasing String](../../1001-1500/1472-increasing-decreasing-string/)
- [1909. Remove One Element to Make the Array Strictly Increasing](../../2001-2500/2020-remove-one-element-to-make-the-array-strictly-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)
