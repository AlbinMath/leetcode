# LeetCode 1758: Minimum Changes To Make Alternating Binary String

**LeetCode Problem #1758 — Minimum Changes To Make Alternating Binary String**
Solve LeetCode Minimum Changes To Make Alternating Binary String using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Changes To Make Alternating Binary String |
| LeetCode | #1758 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a string  s  consisting only of the characters  &#39;0&#39;  and  &#39;1&#39; . In one operation, you can change any  &#39;0&#39;  to  &#39;1&#39;  or vice versa.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Changes To Make Alternating Binary String**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [111. Minimum Depth of Binary Tree](../0111-minimum-depth-of-binary-tree/)
- [671. Second Minimum Node In a Binary Tree](../0671-second-minimum-node-in-a-binary-tree/)
- [693. Binary Number with Alternating Bits](../0693-binary-number-with-alternating-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/)
