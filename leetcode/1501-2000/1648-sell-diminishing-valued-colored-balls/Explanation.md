# LeetCode 1648: Sell Diminishing-Valued Colored Balls

**LeetCode Problem #1648 — Sell Diminishing-Valued Colored Balls**
Solve LeetCode Sell Diminishing-Valued Colored Balls using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sell Diminishing-Valued Colored Balls |
| LeetCode | #1648 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have an `inventory` of different colored balls, and there is a customer that wants `orders` balls of **any** color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls **of that color **you currently have in your `inventory`. For example, if you own `6` yellow balls, the customer would pay `6` for the first yellow ball. After the transaction, there are only `5` yellow balls left, so the next yellow ball is then valued at `5` (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, `inventory`, where `inventory[i]` represents the number of balls of the `i^th` color that you initially own. You are also given an integer `orders`, which represents the total number of balls that the customer wants. You can sell the balls **in any order**.

Return *the **maximum** total value that you can attain after selling *`orders`* colored balls*. As the answer may be too large, return it **modulo **`10^9 + 7`.

## Constraints
- `1 <= inventory.length <= 10^5`
- `1 <= inventory[i] <= 10^9`
- `1 <= orders <= min(sum(inventory[i]), 10^9)`

## Examples
### Example 1
- **Input:** `inventory = [2,5], orders = 4`
- **Output:** `14`
- **Explanation:** Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.

### Example 2
- **Input:** `inventory = [3,5], orders = 6`
- **Output:** `19`
- **Explanation:** Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sell Diminishing-Valued Colored Balls**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `inventory = [2,5], orders = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.

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
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        def cnt(T: int) -> int:
            return sum(x - T for x in inventory if x > T)

        lo, hi = 0, max(inventory)
        while lo < hi:
            mid = (lo + hi) // 2
            if cnt(mid) <= orders:
                hi = mid
            else:
                lo = mid + 1

        T = lo
        total = 0
        sold = 0
        for x in inventory:
            if x > T:
                k = x - T
                total += (x + T + 1) * k // 2
                sold += k

        total += (orders - sold) * T
        return total % MOD
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
- [2038. Remove Colored Pieces if Both Neighbors are the Same Color](../../2001-2500/2038-remove-colored-pieces-if-both-neighbors-are-the-same-color/)
- [1315. Sum of Nodes with Even-Valued Grandparent](../../1001-1500/1315-sum-of-nodes-with-even-valued-grandparent/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1001-1500/1467-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sell-diminishing-valued-colored-balls/)
