# LeetCode 1864: Minimum Number of Swaps to Make the Binary String Alternating

**LeetCode Problem #1864 — Minimum Number of Swaps to Make the Binary String Alternating**
Solve LeetCode Minimum Number of Swaps to Make the Binary String Alternating using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Swaps to Make the Binary String Alternating |
| LeetCode | #1864 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a binary string  s , return  the  minimum  number of character swaps to make it  alternating , or   -1   if it is impossible.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Number of Swaps to Make the Binary String Alternating**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../2017-minimum-number-of-flips-to-make-the-binary-string-alternating/)
- [1758. Minimum Changes To Make Alternating Binary String](../1884-minimum-changes-to-make-alternating-binary-string/)
- [1963. Minimum Number of Swaps to Make the String Balanced](../2095-minimum-number-of-swaps-to-make-the-string-balanced/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/)
