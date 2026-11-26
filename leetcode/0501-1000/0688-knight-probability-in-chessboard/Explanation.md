# LeetCode 688: Knight Probability in Chessboard

**LeetCode Problem #688 — Knight Probability in Chessboard**
Solve LeetCode Knight Probability in Chessboard using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Knight Probability in Chessboard |
| LeetCode | #688 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
On an `n x n` chessboard, a knight starts at the cell `(row, column)` and attempts to make exactly `k` moves. The rows and columns are **0-indexed**, so the top-left cell is `(0, 0)`, and the bottom-right cell is `(n - 1, n - 1)`.

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly `k` moves or has moved off the chessboard.

Return *the probability that the knight remains on the board after it has stopped moving*.

## Constraints
- `1 <= n <= 25`
- `0 <= k <= 100`
- `0 <= row, column <= n - 1`

## Examples
### Example 1
- **Input:** `n = 3, k = 2, row = 0, column = 0`
- **Output:** `0.06250`
- **Explanation:** There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

### Example 2
- **Input:** `n = 1, k = 0, row = 0, column = 0`
- **Output:** `1.00000`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Knight Probability in Chessboard**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 2, row = 0, column = 0`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0.06250`.
4. **Verification:** There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            ndp = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            ndp[x][y] += dp[i][j] / 8
            dp = ndp

        return sum(map(sum, dp))
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
- [2596. Check Knight Tour Configuration](../../2501-3000/2596-check-knight-tour-configuration/)
- [782. Transform to Chessboard](../../0501-1000/0782-transform-to-chessboard/)
- [1812. Determine Color of a Chessboard Square](../../1501-2000/1812-determine-color-of-a-chessboard-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/knight-probability-in-chessboard/)
