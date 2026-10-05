# LeetCode 115: Distinct Subsequences

**LeetCode Problem #115 — Distinct Subsequences**
Solve LeetCode Distinct Subsequences using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Subsequences |
| LeetCode | #115 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given two strings s and t, return  the number of distinct    subsequences    of  s  which equals  t.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **1D Dynamic Programming** with space optimization.

1. **DP Definition:** `dp[j]` represents the number of distinct subsequences of `s[0..i-1]` that equal `t[0..j-1]`.
2. **Base Case:** `dp[0] = 1` because the empty string `""` is always a subsequence of any string (by deleting all characters).
3. **Iteration:** For each character `s[i-1]` (outer loop over `s`):
   - It iterates **backwards** over `j` (from `n` down to `1`) to avoid overwriting values that are still needed.
   - If `s[i-1] === t[j-1]`, then `dp[j] += dp[j-1]`. This means: the number of ways to form `t[0..j-1]` includes both (a) the ways without using `s[i-1]` (existing `dp[j]`) and (b) the ways that use `s[i-1]` to match `t[j-1]` (which is `dp[j-1]`).
4. The answer is `dp[n]` — the number of ways to form the entire string `t`.

Time complexity is $O(M \times N)$ where $M$ and $N$ are the lengths of `s` and `t`. Space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Distinct Subsequences**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [940. Distinct Subsequences II](../0977-distinct-subsequences-ii/)
- [1081. Smallest Subsequence of Distinct Characters](../1159-smallest-subsequence-of-distinct-characters/)
- [3336. Find the Number of Subsequences With Equal GCD](../3608-find-the-number-of-subsequences-with-equal-gcd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-subsequences/)
