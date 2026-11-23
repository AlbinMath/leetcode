# LeetCode 1738: Find Kth Largest XOR Coordinate Value

**LeetCode Problem #1738 — Find Kth Largest XOR Coordinate Value**
Solve LeetCode Find Kth Largest XOR Coordinate Value using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Kth Largest XOR Coordinate Value |
| LeetCode | #1738 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a 2D  matrix  of size  m x n , consisting of non-negative integers. You are also given an integer  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Kth Largest XOR Coordinate Value**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [515. Find Largest Value in Each Tree Row](../0515-find-largest-value-in-each-tree-row/)
- [1985. Find the Kth Largest Integer in the Array](../2113-find-the-kth-largest-integer-in-the-array/)
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](../1888-find-nearest-point-that-has-the-same-x-or-y-coordinate/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/)
