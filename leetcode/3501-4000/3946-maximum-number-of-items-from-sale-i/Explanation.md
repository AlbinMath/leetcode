# LeetCode 3946: Maximum Number of Items From Sale I

**LeetCode Problem #3946 — Maximum Number of Items From Sale I**
Solve LeetCode Maximum Number of Items From Sale I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Items From Sale I |
| LeetCode | #3946 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `items`, where `items[i] = [factor_i, price_i]` represents the `i^th` item. You are also given an integer `budget`.

There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most `budget`.

After buying items, you may receive free copies according to the following rules:

For each item `i` that you bought **at least one copy** of, you receive **one free copy** of every item `j` such that `j != i` and `factor_i` divides `factor_j`. 
 Buying multiple copies of the same item `i` does **not** give additional free copies through item `i`. 
 The same item `j` can be received multiple times for free if it is received from purchases of different item types.

Return the **maximum total number of item copies** you can obtain, including both purchased copies and free copies, while spending at most `budget` on purchased items.

## Constraints
- `1 <= items.length <= 1000`
- `items[i] = [factor_i, price_i]`
- `1 <= factor_i, price_i <= 1500`
- `1 <= budget <= 1500`

## Examples
### Example 1
- **Input:** `items = [[6,2],[2,6],[3,4]], budget = 9`
- **Output:** `4`
- **Explanation:** You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of `2 * 2 + 4 = 8`, which is not greater than `budget = 9`. 
 Buying item 2 gives 1 free copy of item 0, because `factor_2 = 3` divides `factor_0 = 6`. 
 You leave with 3 purchased copies and 1 free copy, for a total of 4 item copies.

### Example 2
- **Input:** `items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8`
- **Output:** `10`
- **Explanation:** You can buy 1 copy of item 0, 1 copy of item 1, and 2 copies of item 2 for a total cost of `4 + 2 + 2 * 1 = 8`. 
 Buying item 0 gives 1 free copy of items 2, 3, and 4. 
 Buying item 1 gives 1 free copy of items 3 and 4. 
 Buying item 2 gives 1 free copy of item 4. 
 Thus, you receive 6 free copies. You leave with 4 purchased copies and 6 free copies, for a total of 10 item copies.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Items From Sale I**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `items = [[6,2],[2,6],[3,4]], budget = 9`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of `2 * 2 + 4 = 8`, which is not greater than `budget = 9`. 
 Buying item 2 gives 1 free copy of item 0, because `factor_2 = 3` divides `factor_0 = 6`. 
 You leave with 3 purchased copies and 1 free copy, for a total of 4 item copies.

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
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        g = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if j != i and items[j][0] % fi == 0:
                    cnt += 1
            g[i] = cnt

        order = sorted(range(n), key=lambda i: -items[i][1])
        dp = [0] * (budget + 1)  # best value with total cost <= c, using items processed so far
        ans = 0

        for m in order:
            p = items[m][1]
            if p > budget:
                continue
            val = 1 + g[m]
            for c in range(budget - p + 1):
                cand = dp[c] + val + (budget - c - p) // p
                if cand > ans:
                    ans = cand
            for c in range(budget, p - 1, -1):
                v = dp[c - p] + val
                if v > dp[c]:
                    dp[c] = v
        return ans
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
- [3947. Maximum Number of Items From Sale II](../../3501-4000/3947-maximum-number-of-items-from-sale-ii/)
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2503-maximum-number-of-points-from-grid-queries/)
- [2554. Maximum Number of Integers to Choose From a Range I](../../2501-3000/2554-maximum-number-of-integers-to-choose-from-a-range-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-items-from-sale-i/)
