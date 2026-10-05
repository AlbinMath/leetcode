# LeetCode 1406: Stone Game III

**LeetCode Problem #1406 — Stone Game III**
Solve LeetCode Stone Game III using PHP and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game III |
| LeetCode | #1406 |
| Difficulty | Hard |
| Language | PHP |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Alice and Bob continue their games with piles of stones. There are several stones  arranged in a row , and each stone has an associated value which is an integer given in the array  stoneValue .

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
The code uses **Dynamic Programming** where `dp[i]` = max stones the current player can score from piles `i` onward.

1. Process from the last pile backwards.
2. For each position `i`, try taking 1, 2, or 3 piles. The current player gets `suffix[i] - dp[i + take]` (total remaining minus what the opponent gets).
3. Compare `dp[0]` (Alice's score) with `suffix[0] - dp[0]` (Bob's score).

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**DP Table / Array**).
2. Process elements sequentially using **Memoization & State Transition**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Stone Game III**. Applying **Memoization & State Transition** yields the target result step by step.

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
- [877. Stone Game](../0909-stone-game/)
- [1140. Stone Game II](../1240-stone-game-ii/)
- [1306. Jump Game III](../1428-jump-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-iii/)
