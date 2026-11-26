# LeetCode 2218: Maximum Value of K Coins From Piles

**LeetCode Problem #2218 — Maximum Value of K Coins From Piles**
Solve LeetCode Maximum Value of K Coins From Piles using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value of K Coins From Piles |
| LeetCode | #2218 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` **piles** of coins on a table. Each pile consists of a **positive number** of coins of assorted denominations.

In one move, you can choose any coin on **top** of any pile, remove it, and add it to your wallet.

Given a list `piles`, where `piles[i]` is a list of integers denoting the composition of the `i^th` pile from **top to bottom**, and a positive integer `k`, return *the **maximum total value** of coins you can have in your wallet if you choose **exactly*** `k` *coins optimally*.

## Constraints
- `n == piles.length`
- `1 <= n <= 1000`
- `1 <= piles[i][j] <= 10^5`
- `1 <= k <= sum(piles[i].length) <= 2000`

## Examples
### Example 1
- **Input:** `piles = [[1,100,3],[7,8,9]], k = 2`
- **Output:** `101`
- **Explanation:** The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.

### Example 2
- **Input:** `piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7`
- **Output:** `706`
- **Explanation:** The maximum total can be obtained if we choose all coins from the last pile.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Value of K Coins From Piles**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `piles = [[1,100,3],[7,8,9]], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `101`.
4. **Verification:** The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.

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
var maxValueOfCoins = function(piles, k) {
    let dp = Array(k + 1).fill(-Infinity);
    dp[0] = 0;
    for (let pile of piles) {
        let prefix = [0];
        for (let coin of pile) {
            prefix.push(prefix[prefix.length - 1] + coin);
        }
        let newDp = Array(k + 1).fill(-Infinity);
        for (let j = 0; j <= k; j++) {
            for (let x = 0; x <= Math.min(j, pile.length); x++) {
                if (dp[j - x] !== -Infinity) {
                    newDp[j] = Math.max(
                        newDp[j],
                        dp[j - x] + prefix[x]
                    );
                }
            }
        }
        dp = newDp;
    }
    return dp[k];
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
- [3413. Maximum Coins From K Consecutive Bags](../../3001-3500/3413-maximum-coins-from-k-consecutive-bags/)
- [2920. Maximum Points After Collecting Coins From All Nodes](../../2501-3000/2920-maximum-points-after-collecting-coins-from-all-nodes/)
- [632. Smallest Range Covering Elements from K Lists](../../0501-1000/0632-smallest-range-covering-elements-from-k-lists/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/)
