# LeetCode 3849: Maximum Bitwise XOR After Rearrangement

**LeetCode Problem #3849 — Maximum Bitwise XOR After Rearrangement**
Solve LeetCode Maximum Bitwise XOR After Rearrangement using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Bitwise XOR After Rearrangement |
| LeetCode | #3849 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two binary strings  s  and  t ​​​​​​​, each of length  n .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Bitwise XOR After Rearrangement**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [2317. Maximum XOR After Operations ](../2402-maximum-xor-after-operations-/)
- [3806. Maximum Bitwise AND After Increment Operations](../4154-maximum-bitwise-and-after-increment-operations/)
- [421. Maximum XOR of Two Numbers in an Array](../0421-maximum-xor-of-two-numbers-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/)
