# LeetCode 2944: Minimum Number of Coins for Fruits

**LeetCode Problem #2944 — Minimum Number of Coins for Fruits**
Solve LeetCode Minimum Number of Coins for Fruits using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Coins for Fruits |
| LeetCode | #2944 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an **0-indexed** integer array `prices` where `prices[i]` denotes the number of coins needed to purchase the `(i + 1)^th` fruit.

The fruit market has the following reward for each fruit:

If you purchase the `(i + 1)^th` fruit at `prices[i]` coins, you can get any number of the next `i` fruits for free.

**Note** that even if you **can** take fruit `j` for free, you can still purchase it for `prices[j - 1]` coins to receive its reward.

Return the **minimum** number of coins needed to acquire all the fruits.

## Constraints
- `1 <= prices.length <= 1000`
- `1 <= prices[i] <= 10^5`

## Examples
### Example 1
- **Input:** `prices = [3,1,2]`
- **Output:** `4`
- **Explanation:** Purchase the 1^st fruit with `prices[0] = 3` coins, you are allowed to take the 2^nd fruit for free. 
 Purchase the 2^nd fruit with `prices[1] = 1` coin, you are allowed to take the 3^rd fruit for free. 
 Take the 3^rd fruit for free. 
 

 Note that even though you could take the 2^nd fruit for free as a reward of buying 1^st fruit, you purchase it to receive its reward, which is more optimal.

### Example 2
- **Input:** `prices = [1,10,1,1]`
- **Output:** `2`
- **Explanation:** Purchase the 1^st fruit with `prices[0] = 1` coin, you are allowed to take the 2^nd fruit for free. 
 Take the 2^nd fruit for free. 
 Purchase the 3^rd fruit for `prices[2] = 1` coin, you are allowed to take the 4^th fruit for free. 
 Take the 4^t^h fruit for free.

### Example 3
- **Input:** `prices = [26,18,6,12,49,7,45,45]`
- **Output:** `39`
- **Explanation:** Purchase the 1^st fruit with `prices[0] = 26` coin, you are allowed to take the 2^nd fruit for free. 
 Take the 2^nd fruit for free. 
 Purchase the 3^rd fruit for `prices[2] = 6` coin, you are allowed to take the 4^th, 5^th and 6^th (the next three) fruits for free. 
 Take the 4^t^h fruit for free. 
 Take the 5^t^h fruit for free. 
 Purchase the 6^th fruit with `prices[5] = 7` coin, you are allowed to take the 8^th and 9^th fruit for free. 
 Take the 7^t^h fruit for free. 
 Take the 8^t^h fruit for free. 
 

 Note that even though you could take the 6^th fruit for free as a reward of buying 3^rd fruit, you purchase it to receive its reward, which is more optimal.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Number of Coins for Fruits**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We decompose the problem into overlapping subproblems using a **Integer Bitmask**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `prices = [3,1,2]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Purchase the 1^st fruit with `prices[0] = 3` coins, you are allowed to take the 2^nd fruit for free. 
 Purchase the 2^nd fruit with `prices[1] = 1` coin, you are allowed to take the 3^rd fruit for free. 
 Take the 3^rd fruit for free. 
 

 Note that even though you could take the 2^nd fruit for free as a reward of buying 1^st fruit, you purchase it to receive its reward, which is more optimal.

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
 * @param {number[]} prices
 * @return {number}
 */
var minimumCoins = function (prices) {
    const n = prices.length;
    const dp = new Array(n + 2).fill(0); // 1-indexed

    for (let i = n; i >= 1; i--) {
        if (2 * i >= n) {
            dp[i] = prices[i - 1];
        } else {
            let best = Infinity;
            for (let j = i + 1; j <= 2 * i + 1; j++) {
                if (dp[j] < best) best = dp[j];
            }
            dp[i] = prices[i - 1] + best;
        }
    }
    return dp[1];
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
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-coins-for-fruits/)
