# LeetCode 1460: Make Two Arrays Equal by Reversing Subarrays

**LeetCode Problem #1460 — Make Two Arrays Equal by Reversing Subarrays**
Solve LeetCode Make Two Arrays Equal by Reversing Subarrays using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Two Arrays Equal by Reversing Subarrays |
| LeetCode | #1460 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two integer arrays of equal length  target  and  arr . In one step, you can select any  non-empty subarray  of  arr  and reverse it. You are allowed to make any number of steps.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Make Two Arrays Equal by Reversing Subarrays**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../3717-minimum-operations-to-make-elements-within-k-subarrays-equal/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [3226. Number of Bit Changes to Make Two Integers Equal](../3508-number-of-bit-changes-to-make-two-integers-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/)
