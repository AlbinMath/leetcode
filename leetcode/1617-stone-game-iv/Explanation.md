# LeetCode 1510: Stone Game IV

**LeetCode Problem #1510 — Stone Game IV**
Solve LeetCode Stone Game IV using TypeScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game IV |
| LeetCode | #1510 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob take turns playing a game, with Alice starting first.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **Dynamic Programming** where `dp[i]` = whether the current player wins with `i` stones.

1. `dp[0] = false` (no stones = current player loses).
2. For each `i` from 1 to n: try removing every perfect square `k*k <= i`. If any `dp[i - k*k]` is `false` (meaning the opponent would lose), then `dp[i] = true`.
3. Return `dp[n]`.

Time complexity is $O(N\sqrt{N})$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Stone Game IV**. Applying **Memoization & State Transition** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [550. Game Play Analysis IV](../1182-game-play-analysis-iv/)
- [877. Stone Game](../0909-stone-game/)
- [1140. Stone Game II](../1240-stone-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-iv/)
