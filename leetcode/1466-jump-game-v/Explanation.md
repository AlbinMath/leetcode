# LeetCode 1340: Jump Game V

**LeetCode Problem #1340 — Jump Game V**
Solve LeetCode Jump Game V using C++ and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game V |
| LeetCode | #1340 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of integers  arr  and an integer  d . In one step you can jump from index  i  to index:

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **DFS with Memoization**.

1. **DP Array:** `dp[i]` stores the maximum number of indices reachable from index `i`. Initialized to `1` (the index itself).
2. **DFS Function:** For each index `i`:
   - Try jumping right: iterate `j` from `i+1` up to `min(n-1, i+d)`. If `arr[j] >= arr[i]`, stop (blocked). Otherwise, `dp[i] = max(dp[i], 1 + dfs(j))`.
   - Try jumping left: iterate `j` from `i-1` down to `max(0, i-d)`. Same blocking rule.
3. **Answer:** The maximum of `dfs(i)` over all starting indices.

Time complexity is $O(N \times D)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Jump Game V**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [45. Jump Game II](../0045-jump-game-ii/)
- [55. Jump Game](../0055-jump-game/)
- [1306. Jump Game III](../1428-jump-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-v/)
