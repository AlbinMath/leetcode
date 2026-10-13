# LeetCode 334: Increasing Triplet Subsequence

**LeetCode Problem #334 — Increasing Triplet Subsequence**
Solve LeetCode Increasing Triplet Subsequence using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Increasing Triplet Subsequence |
| LeetCode | #334 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an integer array  nums , return  true   if there exists a triple of indices   (i, j, k)   such that   i < j < k   and   nums[i] < nums[j] < nums[k] . If no such indices exists, return  false .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Increasing Triplet Subsequence**. Applying **Memoization & State Transition** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [674. Longest Continuous Increasing Subsequence](../0674-longest-continuous-increasing-subsequence/)
- [1403. Minimum Subsequence in Non-Increasing Order](../1519-minimum-subsequence-in-non-increasing-order/)
- [392. Is Subsequence](../0392-is-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/increasing-triplet-subsequence/)
