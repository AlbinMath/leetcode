# LeetCode 486: Predict the Winner

**LeetCode Problem #486 — Predict the Winner**
Solve LeetCode Predict the Winner using C++ and Dynamic Programming. This solution finds the optimal result using Memoization / Bottom-Up State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Predict the Winner |
| LeetCode | #486 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Memoization / Bottom-Up State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer array  nums .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **Interval DP** where `dp[i][j]` represents the maximum score advantage the current player can achieve from the subarray `nums[i..j]`.

1. **Base Case:** `dp[i][i] = nums[i]` — if only one number is left, the current player takes it.
2. **Transition:** For each subarray of length `len` from `2` to `n`:
   - `dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])`
   - The current player picks either the left (`nums[i]`) or right (`nums[j]`) element. After picking, the opponent becomes the "current player" for the remaining subarray, so we subtract `dp` of the remaining range (since that represents the opponent's advantage).
3. **Result:** `dp[0][n-1] >= 0` means Player 1's advantage over the entire array is non-negative, so Player 1 wins or ties.

Time complexity is $O(N^2)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization / Bottom-Up State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Predict the Winner**. Applying **Memoization / Bottom-Up State Transition** yields the target result step by step.

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
- [10. Regular Expression Matching](../0010-regular-expression-matching/)
- [115. Distinct Subsequences](../0115-distinct-subsequences/)
- [977. Squares of a Sorted Array](../0977-distinct-subsequences-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/predict-the-winner/)
