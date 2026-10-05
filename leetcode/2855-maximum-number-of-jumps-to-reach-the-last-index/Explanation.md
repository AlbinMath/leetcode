# LeetCode 2855: Minimum Right Shifts to Sort the Array

**LeetCode Problem #2855 — Minimum Right Shifts to Sort the Array**
Solve LeetCode Minimum Right Shifts to Sort the Array using C++ and Dynamic Programming. This solution finds the optimal result using Memoization / Bottom-Up State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Right Shifts to Sort the Array |
| LeetCode | #2855 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Memoization / Bottom-Up State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  array  nums  of  n  integers and an integer  target .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
Uses **DP** where `dp[i]` = max jumps to reach index `i`. For each `i`, check all `j < i` where the jump is valid and update `dp[i] = max(dp[i], dp[j] + 1)`. Return `dp[n-1]` or -1 if unreachable.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization / Bottom-Up State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Right Shifts to Sort the Array**. Applying **Memoization / Bottom-Up State Transition** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1297. Maximum Number of Occurrences of a Substring](../1297-maximum-number-of-balloons/)
- [1644. Lowest Common Ancestor of a Binary Tree II](../1644-maximum-number-of-non-overlapping-substrings/)
- [2182. Construct String With Repeat Limit](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/)
