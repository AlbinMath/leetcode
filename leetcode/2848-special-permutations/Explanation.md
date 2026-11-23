# LeetCode 2741: Special Permutations

**LeetCode Problem #2741 — Special Permutations**
Solve LeetCode Special Permutations using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Special Permutations |
| LeetCode | #2741 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  integer array  nums  containing  n   distinct  positive integers. A permutation of  nums  is called special if:

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Backtracking Recursive Search**. By maintaining state efficiently in a **Recursion Tree**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Special Permutations**. Applying **Backtracking Recursive Search** yields the target result step by step.

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
- [46. Permutations](../0046-permutations/)
- [47. Permutations II](../0047-permutations-ii/)
- [903. Valid Permutations for DI Sequence](../0939-valid-permutations-for-di-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/special-permutations/)
