# LeetCode 446: Arithmetic Slices II - Subsequence

**LeetCode Problem #446 — Arithmetic Slices II - Subsequence**
Solve LeetCode Arithmetic Slices II - Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Arithmetic Slices II - Subsequence |
| LeetCode | #446 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an integer array  nums , return  the number of all the  arithmetic subsequences  of   nums .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Arithmetic Slices II - Subsequence**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [413. Arithmetic Slices](../0413-arithmetic-slices/)
- [300. Longest Increasing Subsequence](../0300-longest-increasing-subsequence/)
- [334. Increasing Triplet Subsequence](../0334-increasing-triplet-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)
