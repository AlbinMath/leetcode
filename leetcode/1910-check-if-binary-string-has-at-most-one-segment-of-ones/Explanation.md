# LeetCode 1784: Check if Binary String Has at Most One Segment of Ones

**LeetCode Problem #1784 — Check if Binary String Has at Most One Segment of Ones**
Solve LeetCode Check if Binary String Has at Most One Segment of Ones using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Binary String Has at Most One Segment of Ones |
| LeetCode | #1784 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a binary string  s   ​​​​​without leading zeros , return  true ​​​  if   s   contains  at most one contiguous segment of ones  . Otherwise, return  false .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Check if Binary String Has at Most One Segment of Ones**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1790. Check if One String Swap Can Make Strings Equal](../1915-check-if-one-string-swap-can-make-strings-equal/)
- [1662. Check If Two String Arrays are Equivalent](../1781-check-if-two-string-arrays-are-equivalent/)
- [1961. Check If String Is a Prefix of Array](../2093-check-if-string-is-a-prefix-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)
