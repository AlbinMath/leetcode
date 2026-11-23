# LeetCode 2044: Count Number of Maximum Bitwise-OR Subsets

**LeetCode Problem #2044 — Count Number of Maximum Bitwise-OR Subsets**
Solve LeetCode Count Number of Maximum Bitwise-OR Subsets using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Maximum Bitwise-OR Subsets |
| LeetCode | #2044 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer array  nums , find the  maximum  possible  bitwise OR  of a subset of  nums  and return  the  number of different non-empty subsets  with the maximum bitwise OR .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Number of Maximum Bitwise-OR Subsets**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [2572. Count the Number of Square-Free Subsets](../../2501-3000/2709-count-the-number-of-square-free-subsets/)
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [414. Third Maximum Number](../../0001-0500/0414-third-maximum-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)
