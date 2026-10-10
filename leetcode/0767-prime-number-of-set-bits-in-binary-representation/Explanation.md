# LeetCode 762: Prime Number of Set Bits in Binary Representation

**LeetCode Problem #762 — Prime Number of Set Bits in Binary Representation**
Solve LeetCode Prime Number of Set Bits in Binary Representation using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prime Number of Set Bits in Binary Representation |
| LeetCode | #762 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given two integers  left  and  right , return  the  count  of numbers in the  inclusive  range   [left, right]   having a  prime number of set bits  in their binary representation .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Prime Number of Set Bits in Binary Representation**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [693. Binary Number with Alternating Bits](../0693-binary-number-with-alternating-bits/)
- [1290. Convert Binary Number in a Linked List to Integer](../1411-convert-binary-number-in-a-linked-list-to-integer/)
- [1356. Sort Integers by The Number of 1 Bits](../1458-sort-integers-by-the-number-of-1-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)
