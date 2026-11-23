# LeetCode 1835: Find XOR Sum of All Pairs Bitwise AND

**LeetCode Problem #1835 — Find XOR Sum of All Pairs Bitwise AND**
Solve LeetCode Find XOR Sum of All Pairs Bitwise AND using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find XOR Sum of All Pairs Bitwise AND |
| LeetCode | #1835 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
The  XOR sum  of a list is the bitwise  XOR  of all its elements. If the list only contains one element, then its  XOR sum  will be equal to this element.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find XOR Sum of All Pairs Bitwise AND**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [3318. Find X-Sum of All K-Long Subarrays I](../../3501-4000/3610-find-x-sum-of-all-k-long-subarrays-i/)
- [3321. Find X-Sum of All K-Long Subarrays II](../../3501-4000/3592-find-x-sum-of-all-k-long-subarrays-ii/)
- [1863. Sum of All Subset XOR Totals](../../1501-2000/1993-sum-of-all-subset-xor-totals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/)
