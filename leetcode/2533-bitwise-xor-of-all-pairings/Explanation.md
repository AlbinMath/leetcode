# LeetCode 2425: Bitwise XOR of All Pairings

**LeetCode Problem #2425 — Bitwise XOR of All Pairings**
Solve LeetCode Bitwise XOR of All Pairings using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bitwise XOR of All Pairings |
| LeetCode | #2425 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two  0-indexed  arrays,  nums1  and  nums2 , consisting of non-negative integers. Let there be another array,  nums3 , which contains the bitwise XOR of  all pairings  of integers between  nums1  and  nums2  (every integer in  nums1  is paired with every integer in  nums2   exactly once ).

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Bitwise XOR of All Pairings**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1863. Sum of All Subset XOR Totals](../1993-sum-of-all-subset-xor-totals/)
- [3702. Longest Subsequence With Non-Zero Bitwise XOR](../4033-longest-subsequence-with-non-zero-bitwise-xor/)
- [30. Substring with Concatenation of All Words](../0030-substring-with-concatenation-of-all-words/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bitwise-xor-of-all-pairings/)
