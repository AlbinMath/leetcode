# LeetCode 3211: Generate Binary Strings Without Adjacent Zeros

**LeetCode Problem #3211 — Generate Binary Strings Without Adjacent Zeros**
Solve LeetCode Generate Binary Strings Without Adjacent Zeros using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Binary Strings Without Adjacent Zeros |
| LeetCode | #3211 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a positive integer  n .

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Generate Binary Strings Without Adjacent Zeros**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

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
- [3955. Valid Binary Strings With Cost Limit](../../4001-4500/4289-valid-binary-strings-with-cost-limit/)
- [777. Swap Adjacent in LR String](../../0501-1000/0793-swap-adjacent-in-lr-string/)
- [1042. Flower Planting With No Adjacent](../../1001-1500/1120-flower-planting-with-no-adjacent/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/)
