# LeetCode 491: Non-decreasing Subsequences

**LeetCode Problem #491 — Non-decreasing Subsequences**
Solve LeetCode Non-decreasing Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Non-decreasing Subsequences |
| LeetCode | #491 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an integer array  nums , return  all the different possible non-decreasing subsequences of the given array with at least two elements . You may return the answer in  any order .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Non-decreasing Subsequences**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [2289. Steps to Make Array Non-decreasing](../2374-steps-to-make-array-non-decreasing/)
- [2945. Find Maximum Non-decreasing Array Length](../3211-find-maximum-non-decreasing-array-length/)
- [3326. Minimum Division Operations to Make Array Non Decreasing](../3607-minimum-division-operations-to-make-array-non-decreasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/non-decreasing-subsequences/)
