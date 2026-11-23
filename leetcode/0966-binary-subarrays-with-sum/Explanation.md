# LeetCode 930: Binary Subarrays With Sum

**LeetCode Problem #930 — Binary Subarrays With Sum**
Solve LeetCode Binary Subarrays With Sum using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Subarrays With Sum |
| LeetCode | #930 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a binary array  nums  and an integer  goal , return  the number of non-empty  subarrays  with a sum   goal .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Binary Subarrays With Sum**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [124. Binary Tree Maximum Path Sum](../0124-binary-tree-maximum-path-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1022. Sum of Root To Leaf Binary Numbers](../1079-sum-of-root-to-leaf-binary-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/)
