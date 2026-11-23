# LeetCode 3007: Maximum Number That Sum of the Prices Is Less Than or Equal to K

**LeetCode Problem #3007 — Maximum Number That Sum of the Prices Is Less Than or Equal to K**
Solve LeetCode Maximum Number That Sum of the Prices Is Less Than or Equal to K using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number That Sum of the Prices Is Less Than or Equal to K |
| LeetCode | #3007 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  k  and an integer  x . The price of a number  num  is calculated by the count of  set bits  at positions  x ,  2x ,  3x , etc., in its binary representation, starting from the least significant bit. The following table contains examples of how price is calculated.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Number That Sum of the Prices Is Less Than or Equal to K**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../1413-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
- [2311. Longest Binary Subsequence Less Than or Equal to K](../2395-longest-binary-subsequence-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
