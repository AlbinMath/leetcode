# LeetCode 3755: Find Maximum Balanced XOR Subarray Length

**LeetCode Problem #3755 — Find Maximum Balanced XOR Subarray Length**
Solve LeetCode Find Maximum Balanced XOR Subarray Length using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Balanced XOR Subarray Length |
| LeetCode | #3755 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums , return the  length  of the  longest  subarray   that has a bitwise XOR of zero and contains an  equal  number of  even  and  odd  numbers. If no such subarray exists, return 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Maximum Balanced XOR Subarray Length**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [718. Maximum Length of Repeated Subarray](../../0501-1000/0718-maximum-length-of-repeated-subarray/)
- [2945. Find Maximum Non-decreasing Array Length](../../3001-3500/3211-find-maximum-non-decreasing-array-length/)
- [3845. Maximum Subarray XOR with Bounded Range](../../4001-4500/4204-maximum-subarray-xor-with-bounded-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/)
