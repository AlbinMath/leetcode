# LeetCode 3336: Find the Number of Subsequences With Equal GCD

**LeetCode Problem #3336 — Find the Number of Subsequences With Equal GCD**
Solve LeetCode Find the Number of Subsequences With Equal GCD using PHP and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Number of Subsequences With Equal GCD |
| LeetCode | #3336 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization / Bottom-Up State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Number of Subsequences With Equal GCD**. Applying **Memoization & State Transition** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [1295. Find Numbers with Even Number of Digits](../1421-find-numbers-with-even-number-of-digits/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../2053-check-if-all-characters-have-equal-number-of-occurrences/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/)
