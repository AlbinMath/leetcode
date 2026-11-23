# LeetCode 2002: Maximum Product of the Length of Two Palindromic Subsequences

**LeetCode Problem #2002 — Maximum Product of the Length of Two Palindromic Subsequences**
Solve LeetCode Maximum Product of the Length of Two Palindromic Subsequences using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of the Length of Two Palindromic Subsequences |
| LeetCode | #2002 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s , find two  disjoint palindromic subsequences  of  s  such that the  product  of their lengths is  maximized . The two subsequences are  disjoint  if they do not both pick a character at the same index.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Product of the Length of Two Palindromic Subsequences**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1001-1500/1336-maximum-product-of-the-length-of-two-palindromic-substrings/)
- [1930. Unique Length-3 Palindromic Subsequences](../../2001-2500/2059-unique-length-3-palindromic-subsequences/)
- [1464. Maximum Product of Two Elements in an Array](../../1501-2000/1574-maximum-product-of-two-elements-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/)
