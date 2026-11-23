# LeetCode 393: UTF-8 Validation

**LeetCode Problem #393 — UTF-8 Validation**
Solve LeetCode UTF-8 Validation using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | UTF-8 Validation |
| LeetCode | #393 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  data  representing the data, return whether it is a valid  UTF-8  encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **UTF-8 Validation**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [7. Reverse Integer](../0007-reverse-integer/)
- [8. String to Integer (atoi)](../0008-string-to-integer-atoi/)
- [29. Divide Two Integers](../0029-divide-two-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/utf-8-validation/)
