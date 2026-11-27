# LeetCode 2412: Minimum Money Required Before Transactions

**LeetCode Problem #2412 — Minimum Money Required Before Transactions**
Solve LeetCode Minimum Money Required Before Transactions using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Money Required Before Transactions |
| LeetCode | #2412 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array ` transactions `, where `transactions[i] = [cost_i, cashback_i]`.

The array describes transactions, where each transaction must be completed exactly once in **some order**. At any given moment, you have a certain amount of `money`. In order to complete transaction `i`, `money >= cost_i` must hold true. After performing a transaction, `money` becomes `money - cost_i + cashback_i`.

Return* the minimum amount of *`money`* required before any transaction so that all of the transactions can be completed **regardless of the order** of the transactions.*

## Constraints
- `1 <= transactions.length <= 10^5`
- `transactions[i].length == 2`
- `0 <= cost_i, cashback_i <= 10^9`

## Examples
### Example 1
- **Input:** `transactions = [[2,1],[5,0],[4,2]]`
- **Output:** `10`
- **Explanation:** Starting with money = 10, the transactions can be performed in any order.
It can be shown that starting with money < 10 will fail to complete all transactions in some order.

### Example 2
- **Input:** `transactions = [[3,0],[0,3]]`
- **Output:** `3`
- **Explanation:** - If transactions are in the order [[3,0],[0,3]], the minimum money required to complete the transactions is 3.
- If transactions are in the order [[0,3],[3,0]], the minimum money required to complete the transactions is 0.
Thus, starting with money = 3, the transactions can be performed in any order.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Money Required Before Transactions**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `transactions = [[2,1],[5,0],[4,2]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** Starting with money = 10, the transactions can be performed in any order.
It can be shown that starting with money < 10 will fail to complete all transactions in some order.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        loss = 0
        extra = 0
        for cost, cashback in transactions:
            if cost > cashback:
                loss += cost - cashback
                extra = max(extra, cashback)
            else:
                extra = max(extra, cost)
        return loss + extra
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2203. Minimum Weighted Subgraph With the Required Paths](../../2001-2500/2203-minimum-weighted-subgraph-with-the-required-paths/)
- [3553. Minimum Weighted Subgraph With the Required Paths II](../../3501-4000/3553-minimum-weighted-subgraph-with-the-required-paths-ii/)
- [3789. Minimum Cost to Acquire Required Items](../../3501-4000/3789-minimum-cost-to-acquire-required-items/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-money-required-before-transactions/)
