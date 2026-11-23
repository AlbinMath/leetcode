# LeetCode 808: Soup Servings

**LeetCode Problem #808 — Soup Servings**
Solve LeetCode Soup Servings using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Soup Servings |
| LeetCode | #808 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have two soups, **A** and **B**, each starting with `n` mL. On every turn, one of the following four serving operations is chosen *at random*, each with probability `0.25` **independent** of all previous turns:

pour 100 mL from type A and 0 mL from type B 
 pour 75 mL from type A and 25 mL from type B 
 pour 50 mL from type A and 50 mL from type B 
 pour 25 mL from type A and 75 mL from type B

**Note:**

There is no operation that pours 0 mL from A and 100 mL from B. 
 The amounts from A and B are poured *simultaneously* during the turn. 
 If an operation asks you to pour **more than** you have left of a soup, pour all that remains of that soup.

The process stops immediately after any turn in which *one of the soups* is used up.

Return the probability that A is used up *before* B, plus half the probability that both soups are used up in the** same turn**. Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `0 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 50`
- **Output:** `0.62500`
- **Explanation:** If we perform either of the first two serving operations, soup A will become empty first.
If we perform the third operation, A and B will become empty at the same time.
If we perform the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

### Example 2
- **Input:** `n = 100`
- **Output:** `0.71875`
- **Explanation:** If we perform the first serving operation, soup A will become empty first.
If we perform the second serving operations, A will become empty on performing operation [1, 2, 3], and both A and B become empty on performing operation 4.
If we perform the third operation, A will become empty on performing operation [1, 2], and both A and B become empty on performing operation 3.
If we perform the fourth operation, A will become empty on performing operation 1, and both A and B become empty on performing operation 2.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.71875.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Soup Servings**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 50`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0.62500`.
4. **Verification:** If we perform either of the first two serving operations, soup A will become empty first.
If we perform the third operation, A and B will become empty at the same time.
If we perform the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

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
/**
 * @param {number} n
 * @return {number}
 */
var soupServings = function(n) {
    if (n >= 4800) return 1;

    const m = Math.ceil(n / 25);
    const dp = Array.from({ length: m + 1 }, () =>
        Array(m + 1).fill(0)
    );

    dp[0][0] = 0.5;

    for (let i = 1; i <= m; i++) {
        dp[0][i] = 1;
        dp[i][0] = 0;
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= m; j++) {
            dp[i][j] = 0.25 * (
                dp[Math.max(0, i - 4)][j] +
                dp[Math.max(0, i - 3)][Math.max(0, j - 1)] +
                dp[Math.max(0, i - 2)][Math.max(0, j - 2)] +
                dp[Math.max(0, i - 1)][Math.max(0, j - 3)]
            );
        }
    }

    return dp[m][m];
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
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)
- [72. Edit Distance](../../0001-0500/0072-edit-distance/)
- [91. Decode Ways](../../0001-0500/0091-decode-ways/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/soup-servings/)
