# LeetCode 3666: Minimum Operations to Equalize Binary String

**LeetCode Problem #3666 — Minimum Operations to Equalize Binary String**
Solve LeetCode Minimum Operations to Equalize Binary String using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Equalize Binary String |
| LeetCode | #3666 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a binary string  s , and an integer  k .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Operations to Equalize Binary String**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1830. Minimum Number of Operations to Make String Sorted](../1941-minimum-number-of-operations-to-make-string-sorted/)
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../2558-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../3475-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/)
