# LeetCode 982: Triples with Bitwise AND Equal To Zero

**LeetCode Problem #982 — Triples with Bitwise AND Equal To Zero**
Solve LeetCode Triples with Bitwise AND Equal To Zero using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Triples with Bitwise AND Equal To Zero |
| LeetCode | #982 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array nums, return  the number of  AND triples  .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Triples with Bitwise AND Equal To Zero**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1787. Make the XOR of All Segments Equal to Zero](../1913-make-the-xor-of-all-segments-equal-to-zero/)
- [2275. Largest Combination With Bitwise AND Greater Than Zero](../2356-largest-combination-with-bitwise-and-greater-than-zero/)
- [2357. Make Array Zero by Subtracting Equal Amounts](../2436-make-array-zero-by-subtracting-equal-amounts/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/)
