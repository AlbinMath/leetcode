# LeetCode 2014: Longest Subsequence Repeated k Times

**LeetCode Problem #2014 — Longest Subsequence Repeated k Times**
Solve LeetCode Longest Subsequence Repeated k Times using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subsequence Repeated k Times |
| LeetCode | #2014 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  of length  n , and an integer  k . You are tasked to find the  longest subsequence repeated   k  times in string  s .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Subsequence Repeated k Times**. Applying **Memoization & State Transition** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1566. Detect Pattern of Length M Repeated K or More Times](../../1501-2000/1689-detect-pattern-of-length-m-repeated-k-or-more-times/)
- [2311. Longest Binary Subsequence Less Than or Equal to K](../../2001-2500/2395-longest-binary-subsequence-less-than-or-equal-to-k/)
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../3001-3500/3213-count-subarrays-where-max-element-appears-at-least-k-times/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)
