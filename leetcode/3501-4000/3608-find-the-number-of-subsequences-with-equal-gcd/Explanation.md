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
- [2447. Number of Subarrays With GCD Equal to K](../../2501-3000/2546-number-of-subarrays-with-gcd-equal-to-k/)
- [287. Find the Duplicate Number](../../0001-0500/0287-find-the-duplicate-number/)
- [792. Number of Matching Subsequences](../../0501-1000/0808-number-of-matching-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/)
