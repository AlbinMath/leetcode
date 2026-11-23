# LeetCode 1463: Cherry Pickup II

**LeetCode Problem #1463 — Cherry Pickup II**
Solve LeetCode Cherry Pickup II using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cherry Pickup II |
| LeetCode | #1463 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a `rows x cols` matrix `grid` representing a field of cherries where `grid[i][j]` represents the number of cherries that you can collect from the `(i, j)` cell.

You have two robots that can collect cherries for you:

**Robot #1** is located at the **top-left corner** `(0, 0)`, and 
 **Robot #2** is located at the **top-right corner** `(0, cols - 1)`.

Return *the maximum number of cherries collection using both robots by following the rules below*:

From a cell `(i, j)`, robots can move to cell `(i + 1, j - 1)`, `(i + 1, j)`, or `(i + 1, j + 1)`. 
 When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell. 
 When both robots stay in the same cell, only one takes the cherries. 
 Both robots cannot move outside of the grid at any moment. 
 Both robots should reach the bottom row in `grid`.

## Constraints
- `rows == grid.length`
- `cols == grid[i].length`
- `2 <= rows, cols <= 70`
- `0 <= grid[i][j] <= 100`

## Examples
### Example 1
- **Input:** `grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]`
- **Output:** `24`
- **Explanation:** Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

### Example 2
- **Input:** `grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]`
- **Output:** `28`
- **Explanation:** Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Cherry Pickup II**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `24`.
4. **Verification:** Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

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
    const rows = grid.length;
    const cols = grid[0].length;
    let dp = Array.from({ length: cols }, () => new Int32Array(cols));

    for (let r = rows - 1; r >= 0; r--) {
        const nextDp = Array.from({ length: cols }, () => new Int32Array(cols));
        for (let c1 = 0; c1 < cols; c1++) {
            for (let c2 = 0; c2 < cols; c2++) {
                const cherries = grid[r][c1] + (c1 === c2 ? 0 : grid[r][c2]);
                let bestNext = 0;

                if (r < rows - 1) {
                    for (let d1 = -1; d1 <= 1; d1++) {
                        const nc1 = c1 + d1;
                        if (nc1 < 0 || nc1 >= cols) continue;
                        for (let d2 = -1; d2 <= 1; d2++) {
                            const nc2 = c2 + d2;
                            if (nc2 < 0 || nc2 >= cols) continue;
                            if (dp[nc1][nc2] > bestNext) {
                                bestNext = dp[nc1][nc2];
                            }
                        }
                    }
                }

                nextDp[c1][c2] = cherries + bestNext;
            }
        }
        dp = nextDp;
    }

    return dp[0][cols - 1];
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
- [741. Cherry Pickup](../../0501-1000/0741-cherry-pickup/)
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1461-count-all-valid-pickup-and-delivery-options/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cherry-pickup-ii/)
