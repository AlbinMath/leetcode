# LeetCode 2311: Longest Binary Subsequence Less Than or Equal to K

**LeetCode Problem #2311 — Longest Binary Subsequence Less Than or Equal to K**
Solve LeetCode Longest Binary Subsequence Less Than or Equal to K using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Binary Subsequence Less Than or Equal to K |
| LeetCode | #2311 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a binary string  s  and a positive integer  k .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Binary Subsequence Less Than or Equal to K**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../1549-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../3240-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [3835. Count Subarrays With Cost Less Than or Equal to K](../4211-count-subarrays-with-cost-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/)
