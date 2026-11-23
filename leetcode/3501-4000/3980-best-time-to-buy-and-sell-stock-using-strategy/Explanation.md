# LeetCode 3652: Best Time to Buy and Sell Stock using Strategy

**LeetCode Problem #3652 — Best Time to Buy and Sell Stock using Strategy**
Solve LeetCode Best Time to Buy and Sell Stock using Strategy using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Best Time to Buy and Sell Stock using Strategy |
| LeetCode | #3652 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `prices` and `strategy`, where:

`prices[i]` is the price of a given stock on the `i^th` day. 
 `strategy[i]` represents a trading action on the `i^th` day, where:
 
 `-1` indicates buying one unit of the stock. 
 `0` indicates holding the stock. 
 `1` indicates selling one unit of the stock.

You are also given an **even** integer `k`, and may perform **at most one** modification to `strategy`. A modification consists of:

Selecting exactly `k` **consecutive** elements in `strategy`. 
 Set the **first** `k / 2` elements to `0` (hold). 
 Set the **last** `k / 2` elements to `1` (sell).

The **profit** is defined as the **sum** of `strategy[i] * prices[i]` across all days.

Return the **maximum** possible profit you can achieve.

**Note:** There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.

## Constraints
- `2 <= prices.length == strategy.length <= 10^5`
- `1 <= prices[i] <= 10^5`
- `-1 <= strategy[i] <= 1`
- `2 <= k <= prices.length`
- `k` is even

## Examples
### Example 1
- **Input:** `prices = [4,2,8], strategy = [-1,0,1], k = 2`
- **Output:** `10`
- **Explanation:** Modification 
 Strategy 
 Profit Calculation 
 Profit 
 
 
 
 
 Original 
 [-1, 0, 1] 
 (-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8 
 4 
 
 
 Modify [0, 1] 
 [0, 1, 1] 
 (0 &times; 4) + (1 &times; 2) + (1 &times; 8) = 0 + 2 + 8 
 10 
 
 
 Modify [1, 2] 
 [-1, 0, 1] 
 (-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8 
 4 
 
 
 

 Thus, the maximum possible profit is 10, which is achieved by modifying the subarray `[0, 1]`​​​​​​​.

### Example 2
- **Input:** `prices = [5,4,3], strategy = [1,1,0], k = 2`
- **Output:** `9`
- **Explanation:** Modification 
 Strategy 
 Profit Calculation 
 Profit 
 
 
 
 
 Original 
 [1, 1, 0] 
 (1 &times; 5) + (1 &times; 4) + (0 &times; 3) = 5 + 4 + 0 
 9 
 
 
 Modify [0, 1] 
 [0, 1, 0] 
 (0 &times; 5) + (1 &times; 4) + (0 &times; 3) = 0 + 4 + 0 
 4 
 
 
 Modify [1, 2] 
 [1, 0, 1] 
 (1 &times; 5) + (0 &times; 4) + (1 &times; 3) = 5 + 0 + 3 
 8 
 
 
 

 Thus, the maximum possible profit is 9, which is achieved without any modification.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Best Time to Buy and Sell Stock using Strategy**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `prices = [4,2,8], strategy = [-1,0,1], k = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** Modification 
 Strategy 
 Profit Calculation 
 Profit 
 
 
 
 
 Original 
 [-1, 0, 1] 
 (-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8 
 4 
 
 
 Modify [0, 1] 
 [0, 1, 1] 
 (0 &times; 4) + (1 &times; 2) + (1 &times; 8) = 0 + 2 + 8 
 10 
 
 
 Modify [1, 2] 
 [-1, 0, 1] 
 (-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8 
 4 
 
 
 

 Thus, the maximum possible profit is 10, which is achieved by modifying the subarray `[0, 1]`​​​​​​​.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        P = [0] * (n + 1)   # prefix sums of prices
        S = [0] * (n + 1)   # prefix sums of strategy[i] * prices[i]
        for i in range(n):
            P[i + 1] = P[i] + prices[i]
            S[i + 1] = S[i] + strategy[i] * prices[i]

        h = k // 2
        best = 0
        for i in range(n - k + 1):
            new = P[i + k] - P[i + h]        # second half sells
            old = S[i + k] - S[i]            # original contribution of the window
            best = max(best, new - old)
        return S[n] + best
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [121. Best Time to Buy and Sell Stock](../../0001-0500/0121-best-time-to-buy-and-sell-stock/)
- [122. Best Time to Buy and Sell Stock II](../../0001-0500/0122-best-time-to-buy-and-sell-stock-ii/)
- [123. Best Time to Buy and Sell Stock III](../../0001-0500/0123-best-time-to-buy-and-sell-stock-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/)
