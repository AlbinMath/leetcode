# LeetCode 2842: Count K-Subsequences of a String With Maximum Beauty

**LeetCode Problem #2842 — Count K-Subsequences of a String With Maximum Beauty**
Solve LeetCode Count K-Subsequences of a String With Maximum Beauty using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count K-Subsequences of a String With Maximum Beauty |
| LeetCode | #2842 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  and an integer  k .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
We iterate through the input using **Memoization & State Transition**. By maintaining state efficiently in a **DP Table / Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count K-Subsequences of a String With Maximum Beauty**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../../3501-4000/3714-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1299-k-concatenation-maximum-sum/)
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1501-2000/1516-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/)
