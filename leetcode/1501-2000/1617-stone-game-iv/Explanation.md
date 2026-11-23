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

## Problem Statement
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile. On each player's turn, that player makes a *move* consisting of removing **any** non-zero **square number** of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer `n`, return `true` if and only if Alice wins the game otherwise return `false`, assuming both players play optimally.

## Constraints
- `1 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `true`
- **Explanation:** Alice can remove 1 stone winning the game because Bob doesn't have any moves.

### Example 2
- **Input:** `n = 2`
- **Output:** `false`
- **Explanation:** Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

### Example 3
- **Input:** `n = 4`
- **Output:** `true`
- **Explanation:** n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

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

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Alice can remove 1 stone winning the game because Bob doesn't have any moves.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

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


```typescript
function winnerSquareGame(n: number): boolean {
    const dp: boolean[] = new Array(n + 1).fill(false);

    // dp[i] = true means the current player can win with i stones

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j * j <= i; j++) {
            // If we can move to a losing state,
            // the current state is winning.
            if (!dp[i - j * j]) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
}
```

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
- [877. Stone Game](../../0501-1000/0909-stone-game/)
- [1140. Stone Game II](../../1001-1500/1240-stone-game-ii/)
- [1406. Stone Game III](../../1501-2000/1522-stone-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-iv/)
