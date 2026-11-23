# LeetCode 2312: Selling Pieces of Wood

**LeetCode Problem #2312 — Selling Pieces of Wood**
Solve LeetCode Selling Pieces of Wood using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Selling Pieces of Wood |
| LeetCode | #2312 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `m` and `n` that represent the height and width of a rectangular piece of wood. You are also given a 2D integer array `prices`, where `prices[i] = [h_i, w_i, price_i]` indicates you can sell a rectangular piece of wood of height `h_i` and width `w_i` for `price_i` dollars.

To cut a piece of wood, you must make a vertical or horizontal cut across the **entire** height or width of the piece to split it into two smaller pieces. After cutting a piece of wood into some number of smaller pieces, you can sell pieces according to `prices`. You may sell multiple pieces of the same shape, and you do not have to sell all the shapes. The grain of the wood makes a difference, so you **cannot** rotate a piece to swap its height and width.

Return *the **maximum** money you can earn after cutting an *`m x n`* piece of wood*.

Note that you can cut the piece of wood as many times as you want.

## Constraints
- `1 <= m, n <= 200`
- `1 <= prices.length <= 2 * 10^4`
- `prices[i].length == 3`
- `1 <= h_i <= m`
- `1 <= w_i <= n`
- `1 <= price_i <= 10^6`
- All the shapes of wood `(h_i, w_i)` are pairwise **distinct**.

## Examples
### Example 1
- **Input:** `m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]`
- **Output:** `19`
- **Explanation:** The diagram above shows a possible scenario. It consists of:
- 2 pieces of wood shaped 2 x 2, selling for a price of 2 * 7 = 14.
- 1 piece of wood shaped 2 x 1, selling for a price of 1 * 3 = 3.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 14 + 3 + 2 = 19 money earned.
It can be shown that 19 is the maximum amount of money that can be earned.

### Example 2
- **Input:** `m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]`
- **Output:** `32`
- **Explanation:** The diagram above shows a possible scenario. It consists of:
- 3 pieces of wood shaped 3 x 2, selling for a price of 3 * 10 = 30.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 30 + 2 = 32 money earned.
It can be shown that 32 is the maximum amount of money that can be earned.
Notice that we cannot rotate the 1 x 4 piece of wood to obtain a 4 x 1 piece of wood.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Selling Pieces of Wood**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `19`.
4. **Verification:** The diagram above shows a possible scenario. It consists of:
- 2 pieces of wood shaped 2 x 2, selling for a price of 2 * 7 = 14.
- 1 piece of wood shaped 2 x 1, selling for a price of 1 * 3 = 3.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 14 + 3 + 2 = 19 money earned.
It can be shown that 19 is the maximum amount of money that can be earned.

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
from typing import List

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p

        for h in range(1, m + 1):
            for w in range(1, n + 1):
                best = dp[h][w]
                for i in range(1, h // 2 + 1):
                    v = dp[i][w] + dp[h - i][w]
                    if v > best:
                        best = v
                for j in range(1, w // 2 + 1):
                    v = dp[h][j] + dp[h][w - j]
                    if v > best:
                        best = v
                dp[h][w] = best
        return dp[m][n]
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
- [2038. Remove Colored Pieces if Both Neighbors are the Same Color](../../2001-2500/2149-remove-colored-pieces-if-both-neighbors-are-the-same-color/)
- [3426. Manhattan Distances of All Arrangements of Pieces](../../3501-4000/3739-manhattan-distances-of-all-arrangements-of-pieces/)
- [1251. Average Selling Price](../../1001-1500/1390-average-selling-price/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/selling-pieces-of-wood/)
