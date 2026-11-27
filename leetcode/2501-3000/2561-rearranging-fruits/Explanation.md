# LeetCode 2561: Rearranging Fruits

**LeetCode Problem #2561 — Rearranging Fruits**
Solve LeetCode Rearranging Fruits using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearranging Fruits |
| LeetCode | #2561 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have two fruit baskets containing `n` fruits each. You are given two **0-indexed** integer arrays `basket1` and `basket2` representing the cost of fruit in each basket. You want to make both baskets **equal**. To do so, you can use the following operation as many times as you want:

Choose two indices `i` and `j`, and swap the `i^ th ` fruit of `basket1` with the `j^ th ` fruit of `basket2`. 
 The cost of the swap is `min(basket1[i], basket2[j])`.

Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return *the minimum cost to make both the baskets equal or *`-1`* if impossible.*

## Constraints
- `basket1.length == basket2.length`
- `1 <= basket1.length <= 10^5`
- `1 <= basket1[i], basket2[i] <= 10^9`

## Examples
### Example 1
- **Input:** `basket1 = [4,2,2,2], basket2 = [1,4,1,2]`
- **Output:** `1`
- **Explanation:** Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

### Example 2
- **Input:** `basket1 = [2,3,4,1], basket2 = [3,2,5,1]`
- **Output:** `-1`
- **Explanation:** It can be shown that it is impossible to make both the baskets equal.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearranging Fruits**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `basket1 = [4,2,2,2], basket2 = [1,4,1,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

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
from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1, c2 = Counter(basket1), Counter(basket2)
        total = c1 + c2
        for v, c in total.items():
            if c % 2:
                return -1
        m = min(total)
        extra = []
        for v in total:
            d = c1[v] - c2[v]
            extra.extend([v] * (abs(d) // 2))
        extra.sort()
        k = len(extra) // 2
        return sum(min(x, 2 * m) for x in extra[:k])
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
- [1846. Maximum Element After Decreasing and Rearranging](../../1501-2000/1846-maximum-element-after-decreasing-and-rearranging/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2106-maximum-fruits-harvested-after-at-most-k-steps/)
- [2944. Minimum Number of Coins for Fruits](../../2501-3000/2944-minimum-number-of-coins-for-fruits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearranging-fruits/)
