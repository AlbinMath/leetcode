# LeetCode 1819: Number of Different Subsequences GCDs

**LeetCode Problem #1819 — Number of Different Subsequences GCDs**
Solve LeetCode Number of Different Subsequences GCDs using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Different Subsequences GCDs |
| LeetCode | #1819 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array  nums  that consists of positive integers.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Different Subsequences GCDs**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [730. Count Different Palindromic Subsequences](../../0501-1000/0730-count-different-palindromic-subsequences/)
- [792. Number of Matching Subsequences](../../0501-1000/0808-number-of-matching-subsequences/)
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1501-2000/1621-number-of-subsequences-that-satisfy-the-given-sum-condition/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/)
