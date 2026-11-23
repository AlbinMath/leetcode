# LeetCode 2354: Number of Excellent Pairs

**LeetCode Problem #2354 — Number of Excellent Pairs**
Solve LeetCode Number of Excellent Pairs using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Excellent Pairs |
| LeetCode | #2354 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  positive integer array  nums  and a positive integer  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Excellent Pairs**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1128. Number of Equivalent Domino Pairs](../1227-number-of-equivalent-domino-pairs/)
- [1512. Number of Good Pairs](../1635-number-of-good-pairs/)
- [1530. Number of Good Leaf Nodes Pairs](../1653-number-of-good-leaf-nodes-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-excellent-pairs/)
