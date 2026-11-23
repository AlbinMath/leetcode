# LeetCode 3681: Maximum XOR of Subsequences

**LeetCode Problem #3681 — Maximum XOR of Subsequences**
Solve LeetCode Maximum XOR of Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum XOR of Subsequences |
| LeetCode | #3681 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums  of length  n  where each element is a non-negative integer.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum XOR of Subsequences**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [2002. Maximum Product of the Length of Two Palindromic Subsequences](../2130-maximum-product-of-the-length-of-two-palindromic-subsequences/)
- [2842. Count K-Subsequences of a String With Maximum Beauty](../3057-count-k-subsequences-of-a-string-with-maximum-beauty/)
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../3714-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-xor-of-subsequences/)
