# LeetCode 790: Domino and Tromino Tiling

**LeetCode Problem #790 — Domino and Tromino Tiling**
Solve LeetCode Domino and Tromino Tiling using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Domino and Tromino Tiling |
| LeetCode | #790 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have two types of tiles: a `2 x 1` domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return *the number of ways to tile an* `2 x n` *board*. Since the answer may be very large, return it **modulo** `10^9 + 7`.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 3`
- **Output:** `5`
- **Explanation:** The five different ways are shown above.

### Example 2
- **Input:** `n = 1`
- **Output:** `1`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Domino and Tromino Tiling**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The five different ways are shown above.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numTilings = function(n) {
    const MOD = 1000000007;

    if (n === 1) return 1;
    if (n === 2) return 2;

    const dp = new Array(n + 1).fill(0);

    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;

    for (let i = 3; i <= n; i++) {
        dp[i] = (
            2 * dp[i - 1] + dp[i - 3]
        ) % MOD;
    }

    return dp[n];
};
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
- [1240. Tiling a Rectangle with the Fewest Squares](../../1001-1500/1240-tiling-a-rectangle-with-the-fewest-squares/)
- [1007. Minimum Domino Rotations For Equal Row](../../1001-1500/1007-minimum-domino-rotations-for-equal-row/)
- [1128. Number of Equivalent Domino Pairs](../../1001-1500/1128-number-of-equivalent-domino-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/domino-and-tromino-tiling/)
