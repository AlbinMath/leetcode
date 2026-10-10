# LeetCode 1356: Sort Integers by The Number of 1 Bits

**LeetCode Problem #1356 — Sort Integers by The Number of 1 Bits**
Solve LeetCode Sort Integers by The Number of 1 Bits using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Integers by The Number of 1 Bits |
| LeetCode | #1356 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer array  arr . Sort the integers in the array in ascending order by the number of  1 &#39;s in their binary representation and in case of two or more integers have the same number of  1 &#39;s you have to sort them in ascending order.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sort Integers by The Number of 1 Bits**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [762. Prime Number of Set Bits in Binary Representation](../0767-prime-number-of-set-bits-in-binary-representation/)
- [1805. Number of Different Integers in a String](../1933-number-of-different-integers-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)
