# LeetCode 2411: Smallest Subarrays With Maximum Bitwise OR

**LeetCode Problem #2411 — Smallest Subarrays With Maximum Bitwise OR**
Solve LeetCode Smallest Subarrays With Maximum Bitwise OR using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Subarrays With Maximum Bitwise OR |
| LeetCode | #2411 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  array  nums  of length  n , consisting of non-negative integers. For each index  i  from  0  to  n - 1 , you must determine the size of the  minimum sized  non-empty subarray of  nums  starting at  i  ( inclusive ) that has the  maximum  possible  bitwise OR .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Subarrays With Maximum Bitwise OR**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [898. Bitwise ORs of Subarrays](../../0501-1000/0934-bitwise-ors-of-subarrays/)
- [2044. Count Number of Maximum Bitwise-OR Subsets](../../2001-2500/2170-count-number-of-maximum-bitwise-or-subsets/)
- [2419. Longest Subarray With Maximum Bitwise AND](../../2501-3000/2503-longest-subarray-with-maximum-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/)
