# LeetCode 3670: Maximum Product of Two Integers With No Common Bits

**LeetCode Problem #3670 — Maximum Product of Two Integers With No Common Bits**
Solve LeetCode Maximum Product of Two Integers With No Common Bits using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Two Integers With No Common Bits |
| LeetCode | #3670 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  nums .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product of Two Integers With No Common Bits**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1440-convert-integer-to-the-sum-of-two-no-zero-integers/)
- [1464. Maximum Product of Two Elements in an Array](../../1501-2000/1574-maximum-product-of-two-elements-in-an-array/)
- [1913. Maximum Product Difference Between Two Pairs](../../2001-2500/2042-maximum-product-difference-between-two-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/)
