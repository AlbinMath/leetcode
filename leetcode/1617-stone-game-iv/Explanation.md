# LeetCode 1617: Count Subtrees With Max Distance Between Cities

**LeetCode Problem #1617 — Count Subtrees With Max Distance Between Cities**
Solve LeetCode Count Subtrees With Max Distance Between Cities using TypeScript and Dynamic Programming. This solution finds the optimal result using Memoization / Bottom-Up State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subtrees With Max Distance Between Cities |
| LeetCode | #1617 |
| Difficulty | Hard |
| Language | TypeScript |
| Algorithm | Memoization / Bottom-Up State Transition |
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
2. Process elements sequentially using **Memoization / Bottom-Up State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Subtrees With Max Distance Between Cities**. Applying **Memoization / Bottom-Up State Transition** yields the target result step by step.

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
- [909. Snakes and Ladders](../0909-stone-game/)
- [1182. Shortest Distance to Target Color](../1182-game-play-analysis-iv/)
- [1240. Tiling a Rectangle with the Fewest Squares](../1240-stone-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-iv/)
