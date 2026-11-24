# LeetCode 741: Cherry Pickup

**LeetCode Problem #741 — Cherry Pickup**
Solve LeetCode Cherry Pickup using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cherry Pickup |
| LeetCode | #741 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `n x n` `grid` representing a field of cherries, each cell is one of three possible integers.

`0` means the cell is empty, so you can pass through, 
 `1` means the cell contains a cherry that you can pick up and pass through, or 
 `-1` means the cell contains a thorn that blocks your way.

Return *the maximum number of cherries you can collect by following the rules below*:

Starting at the position `(0, 0)` and reaching `(n - 1, n - 1)` by moving right or down through valid path cells (cells with value `0` or `1`). 
 After reaching `(n - 1, n - 1)`, returning to `(0, 0)` by moving left or up through valid path cells. 
 When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell `0`. 
 If there is no valid path between `(0, 0)` and `(n - 1, n - 1)`, then no cherries can be collected.

## Constraints
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `grid[i][j]` is `-1`, `0`, or `1`.
- `grid[0][0] != -1`
- `grid[n - 1][n - 1] != -1`

## Examples
### Example 1
- **Input:** `grid = [[0,1,-1],[1,0,-1],[1,1,1]]`
- **Output:** `5`
- **Explanation:** The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

### Example 2
- **Input:** `grid = [[1,1,-1],[1,-1,1],[-1,1,1]]`
- **Output:** `0`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Cherry Pickup**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1,-1],[1,0,-1],[1,1,1]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

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
var cherryPickup = function(grid) {
    const n = grid.length;
    const NEG_INF = -1e9;
    // 3D memo table initialized to null: memo[r1][c1][r2]
    const memo = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => new Array(n).fill(null))
    );

    const dp = (r1, c1, r2) => {
        const c2 = r1 + c1 - r2;
        if (
            r1 >= n || c1 >= n || r2 >= n || c2 >= n ||
            grid[r1][c1] === -1 || grid[r2][c2] === -1
        ) {
            return NEG_INF;
        }

        if (r1 === n - 1 && c1 === n - 1) {
            return grid[r1][c1];
        }

        if (memo[r1][c1][r2] !== null) {
            return memo[r1][c1][r2];
        }

        let cherries = grid[r1][c1];
        if (r1 !== r2 || c1 !== c2) {
            cherries += grid[r2][c2];
        }

        const bestNext = Math.max(
            dp(r1 + 1, c1, r2 + 1), // Both Down
            dp(r1 + 1, c1, r2),     // W1 Down, W2 Right
            dp(r1, c1 + 1, r2 + 1), // W1 Right, W2 Down
            dp(r1, c1 + 1, r2)      // Both Right
        );

        memo[r1][c1][r2] = cherries + bestNext;
        return memo[r1][c1][r2];
    };

    return Math.max(0, dp(0, 0, 0));
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
- [1463. Cherry Pickup II](../../1001-1500/1463-cherry-pickup-ii/)
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1359-count-all-valid-pickup-and-delivery-options/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cherry-pickup/)
