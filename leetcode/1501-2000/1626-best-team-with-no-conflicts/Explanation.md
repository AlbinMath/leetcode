# LeetCode 1626: Best Team With No Conflicts

**LeetCode Problem #1626 — Best Team With No Conflicts**
Solve LeetCode Best Team With No Conflicts using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Best Team With No Conflicts |
| LeetCode | #1626 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the **sum** of scores of all the players in the team.

However, the basketball team is not allowed to have **conflicts**. A **conflict** exists if a younger player has a **strictly higher** score than an older player. A conflict does **not** occur between players of the same age.

Given two lists, `scores` and `ages`, where each `scores[i]` and `ages[i]` represents the score and age of the `i^th` player, respectively, return *the highest overall score of all possible basketball teams*.

## Constraints
- `1 <= scores.length, ages.length <= 1000`
- `scores.length == ages.length`
- `1 <= scores[i] <= 10^6`
- `1 <= ages[i] <= 1000`

## Examples
### Example 1
- **Input:** `scores = [1,3,5,10,15], ages = [1,2,3,4,5]`
- **Output:** `34`
- **Explanation:** You can choose all the players.

### Example 2
- **Input:** `scores = [4,5,6,5], ages = [2,1,2,1]`
- **Output:** `16`
- **Explanation:** It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

### Example 3
- **Input:** `scores = [1,2,3,5], ages = [8,9,10,1]`
- **Output:** `6`
- **Explanation:** It is best to choose the first 3 players.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Best Team With No Conflicts**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `scores = [1,3,5,10,15], ages = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `34`.
4. **Verification:** You can choose all the players.

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
var bestTeamScore = function(scores, ages) {
    const n = scores.length;
    const players = [];
    for (let i = 0; i < n; i++) {
        players.push([ages[i], scores[i]]);
    }
    players.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    });
    const dp = new Array(n);
    let result = 0;
    for (let i = 0; i < n; i++) {
        dp[i] = players[i][1];
        for (let j = 0; j < i; j++) {
            if (players[j][1] <= players[i][1]) {
                dp[i] = Math.max(
                    dp[i],
                    dp[j] + players[i][1]
                );
            }
        }
        result = Math.max(result, dp[i]);
    }
    return result;
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
- [1125. Smallest Sufficient Team](../../1001-1500/1125-smallest-sufficient-team/)
- [1383. Maximum Performance of a Team](../../1001-1500/1383-maximum-performance-of-a-team/)
- [121. Best Time to Buy and Sell Stock](../../0001-0500/0121-best-time-to-buy-and-sell-stock/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/best-team-with-no-conflicts/)
