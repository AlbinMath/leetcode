# LeetCode 3321: Find X-Sum of All K-Long Subarrays II

**LeetCode Problem #3321 — Find X-Sum of All K-Long Subarrays II**
Solve LeetCode Find X-Sum of All K-Long Subarrays II using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find X-Sum of All K-Long Subarrays II |
| LeetCode | #3321 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  nums  of  n  integers and two integers  k  and  x .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find X-Sum of All K-Long Subarrays II**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1588. Sum of All Odd Length Subarrays](../../1501-2000/1693-sum-of-all-odd-length-subarrays/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1963-find-xor-sum-of-all-pairs-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/)
