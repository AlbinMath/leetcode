# LeetCode 2275: Largest Combination With Bitwise AND Greater Than Zero

**LeetCode Problem #2275 — Largest Combination With Bitwise AND Greater Than Zero**
Solve LeetCode Largest Combination With Bitwise AND Greater Than Zero using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Combination With Bitwise AND Greater Than Zero |
| LeetCode | #2275 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
The  bitwise AND  of an array  nums  is the bitwise AND of all integers in  nums .

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Backtracking Recursive Search**. By maintaining state efficiently in a **Recursion Tree**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Combination With Bitwise AND Greater Than Zero**. Applying **Backtracking Recursive Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [982. Triples with Bitwise AND Equal To Zero](../../1001-1500/1024-triples-with-bitwise-and-equal-to-zero/)
- [3702. Longest Subsequence With Non-Zero Bitwise XOR](../../4001-4500/4033-longest-subsequence-with-non-zero-bitwise-xor/)
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../../4001-4500/4032-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/)
