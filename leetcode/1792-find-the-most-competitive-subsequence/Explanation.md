# LeetCode 1673: Find the Most Competitive Subsequence

**LeetCode Problem #1673 — Find the Most Competitive Subsequence**
Solve LeetCode Find the Most Competitive Subsequence using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Most Competitive Subsequence |
| LeetCode | #1673 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an integer array  nums  and a positive integer  k , return  the most  competitive  subsequence of   nums   of size   k .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Most Competitive Subsequence**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [2099. Find Subsequence of Length K With the Largest Sum](../2204-find-subsequence-of-length-k-with-the-largest-sum/)
- [1606. Find Servers That Handled Most Number of Requests](../1710-find-servers-that-handled-most-number-of-requests/)
- [300. Longest Increasing Subsequence](../0300-longest-increasing-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-most-competitive-subsequence/)
