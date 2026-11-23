# LeetCode 2419: Longest Subarray With Maximum Bitwise AND

**LeetCode Problem #2419 — Longest Subarray With Maximum Bitwise AND**
Solve LeetCode Longest Subarray With Maximum Bitwise AND using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subarray With Maximum Bitwise AND |
| LeetCode | #2419 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums  of size  n .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Subarray With Maximum Bitwise AND**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [2044. Count Number of Maximum Bitwise-OR Subsets](../../2001-2500/2170-count-number-of-maximum-bitwise-or-subsets/)
- [2411. Smallest Subarrays With Maximum Bitwise OR](../../2001-2500/2498-smallest-subarrays-with-maximum-bitwise-or/)
- [3171. Find Subarray With Bitwise OR Closest to K](../../3001-3500/3436-find-subarray-with-bitwise-or-closest-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/)
