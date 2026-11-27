# LeetCode 2070: Most Beautiful Item for Each Query

**LeetCode Problem #2070 — Most Beautiful Item for Each Query**
Solve LeetCode Most Beautiful Item for Each Query using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Beautiful Item for Each Query |
| LeetCode | #2070 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `items` where `items[i] = [price_i, beauty_i]` denotes the **price** and **beauty** of an item respectively.

You are also given a **0-indexed** integer array `queries`. For each `queries[j]`, you want to determine the **maximum beauty** of an item whose **price** is **less than or equal** to `queries[j]`. If no such item exists, then the answer to this query is `0`.

Return *an array *`answer`* of the same length as *`queries`* where *`answer[j]`* is the answer to the *`j^th`* query*.

## Constraints
- `1 <= items.length, queries.length <= 10^5`
- `items[i].length == 2`
- `1 <= price_i, beauty_i, queries[j] <= 10^9`

## Examples
### Example 1
- **Input:** `items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]`
- **Output:** `[2,4,5,5,6,6]`
- **Explanation:** - For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
 The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
 The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
 Hence, the answer for them is the maximum beauty of all items, i.e., 6.

### Example 2
- **Input:** `items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]`
- **Output:** `[4]`
- **Explanation:** The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty.

### Example 3
- **Input:** `items = [[10,1000]], queries = [5]`
- **Output:** `[0]`
- **Explanation:** No item has a price less than or equal to 5, so no item can be chosen.
Hence, the answer to the query is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Most Beautiful Item for Each Query**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,4,5,5,6,6]`.
4. **Verification:** - For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
 The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
 The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
 Hence, the answer for them is the maximum beauty of all items, i.e., 6.

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
from bisect import bisect_right
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices = [p for p, _ in items]

        best = []
        cur = 0
        for _, b in items:
            cur = max(cur, b)
            best.append(cur)

        ans = []
        for q in queries:
            idx = bisect_right(prices, q) - 1
            ans.append(best[idx] if idx >= 0 else 0)
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
- [1829. Maximum XOR for Each Query](../../1501-2000/1829-maximum-xor-for-each-query/)
- [1851. Minimum Interval to Include Each Query](../../1501-2000/1851-minimum-interval-to-include-each-query/)
- [116. Populating Next Right Pointers in Each Node](../../0001-0500/0116-populating-next-right-pointers-in-each-node/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-beautiful-item-for-each-query/)
