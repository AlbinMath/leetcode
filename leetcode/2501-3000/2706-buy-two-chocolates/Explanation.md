# LeetCode 2706: Buy Two Chocolates

**LeetCode Problem #2706 — Buy Two Chocolates**
Solve LeetCode Buy Two Chocolates using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Buy Two Chocolates |
| LeetCode | #2706 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `prices` representing the prices of various chocolates in a store. You are also given a single integer `money`, which represents your initial amount of money.

You must buy **exactly** two chocolates in such a way that you still have some **non-negative** leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return *the amount of money you will have leftover after buying the two chocolates*. If there is no way for you to buy two chocolates without ending up in debt, return `money`. Note that the leftover must be non-negative.

## Constraints
- `2 <= prices.length <= 50`
- `1 <= prices[i] <= 100`
- `1 <= money <= 100`

## Examples
### Example 1
- **Input:** `prices = [1,2,2], money = 3`
- **Output:** `0`
- **Explanation:** Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

### Example 2
- **Input:** `prices = [3,2,3], money = 3`
- **Output:** `3`
- **Explanation:** You cannot buy 2 chocolates without going in debt, so we return 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Buy Two Chocolates**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `prices = [1,2,2], money = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

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
    def buyChoco(self, prices: List[int], money: int) -> int:
        a = b = float('inf')  # smallest and second smallest
        for p in prices:
            if p < a:
                a, b = p, a
            elif p < b:
                b = p
        cost = a + b
        return money - cost if cost <= money else money
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
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/buy-two-chocolates/)
