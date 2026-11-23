# LeetCode 1310: XOR Queries of a Subarray

**LeetCode Problem #1310 — XOR Queries of a Subarray**
Solve LeetCode XOR Queries of a Subarray using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | XOR Queries of a Subarray |
| LeetCode | #1310 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array  arr  of positive integers. You are also given the array  queries  where  queries[i] = [left i,  right i ] .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **XOR Queries of a Subarray**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [2564. Substring XOR Queries](../../2501-3000/2700-substring-xor-queries/)
- [3653. XOR After Range Multiplication Queries I](../../3501-4000/3974-xor-after-range-multiplication-queries-i/)
- [3655. XOR After Range Multiplication Queries II](../../3501-4000/3975-xor-after-range-multiplication-queries-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/xor-queries-of-a-subarray/)
