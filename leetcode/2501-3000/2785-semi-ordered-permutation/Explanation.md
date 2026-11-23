# LeetCode 2717: Semi-Ordered Permutation

**LeetCode Problem #2717 — Semi-Ordered Permutation**
Solve LeetCode Semi-Ordered Permutation using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Semi-Ordered Permutation |
| LeetCode | #2717 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a  0-indexed  permutation of  n  integers  nums .

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Backtracking Recursive Search**. By maintaining state efficiently in a **Recursion Tree**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree**).
2. Process elements sequentially using **Backtracking Recursive Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Semi-Ordered Permutation**. Applying **Backtracking Recursive Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [31. Next Permutation](../../0001-0500/0031-next-permutation/)
- [60. Permutation Sequence](../../0001-0500/0060-permutation-sequence/)
- [567. Permutation in String](../../0501-1000/0567-permutation-in-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/semi-ordered-permutation/)
