# LeetCode 1498: Number of Subsequences That Satisfy the Given Sum Condition

**LeetCode Problem #1498 — Number of Subsequences That Satisfy the Given Sum Condition**
Solve LeetCode Number of Subsequences That Satisfy the Given Sum Condition using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Subsequences That Satisfy the Given Sum Condition |
| LeetCode | #1498 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of integers  nums  and an integer  target .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Subsequences That Satisfy the Given Sum Condition**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1450. Number of Students Doing Homework at a Given Time](../1560-number-of-students-doing-homework-at-a-given-time/)
- [1456. Maximum Number of Vowels in a Substring of Given Length](../1567-maximum-number-of-vowels-in-a-substring-of-given-length/)
- [1679. Max Number of K-Sum Pairs](../1798-max-number-of-k-sum-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)
