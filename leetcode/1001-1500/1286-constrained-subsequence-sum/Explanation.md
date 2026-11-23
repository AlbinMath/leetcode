# LeetCode 1425: Constrained Subsequence Sum

**LeetCode Problem #1425 — Constrained Subsequence Sum**
Solve LeetCode Constrained Subsequence Sum using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Constrained Subsequence Sum |
| LeetCode | #1425 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an integer array  nums  and an integer  k , return the maximum sum of a  non-empty  subsequence of that array such that for every two  consecutive  integers in the subsequence,  nums[i]  and  nums[j] , where  i < j , the condition  j - i <= k  is satisfied.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Constrained Subsequence Sum**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1755. Closest Subsequence Sum](../../1501-2000/1881-closest-subsequence-sum/)
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2204-find-subsequence-of-length-k-with-the-largest-sum/)
- [2835. Minimum Operations to Form Subsequence With Target Sum](../../3001-3500/3025-minimum-operations-to-form-subsequence-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/constrained-subsequence-sum/)
