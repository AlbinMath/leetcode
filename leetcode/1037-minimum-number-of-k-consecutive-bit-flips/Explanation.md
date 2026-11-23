# LeetCode 995: Minimum Number of K Consecutive Bit Flips

**LeetCode Problem #995 — Minimum Number of K Consecutive Bit Flips**
Solve LeetCode Minimum Number of K Consecutive Bit Flips using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of K Consecutive Bit Flips |
| LeetCode | #995 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a binary array  nums  and an integer  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Number of K Consecutive Bit Flips**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [2220. Minimum Bit Flips to Convert Number](../2323-minimum-bit-flips-to-convert-number/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../1409-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../2017-minimum-number-of-flips-to-make-the-binary-string-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)
