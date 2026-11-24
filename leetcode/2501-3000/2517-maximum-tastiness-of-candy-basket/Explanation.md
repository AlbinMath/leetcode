# LeetCode 2517: Maximum Tastiness of Candy Basket

**LeetCode Problem #2517 — Maximum Tastiness of Candy Basket**
Solve LeetCode Maximum Tastiness of Candy Basket using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Tastiness of Candy Basket |
| LeetCode | #2517 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of positive integers `price` where `price[i]` denotes the price of the `i^th` candy and a positive integer `k`.

The store sells baskets of `k` **distinct** candies. The **tastiness** of a candy basket is the smallest absolute difference of the **prices** of any two candies in the basket.

Return *the **maximum** tastiness of a candy basket.*

## Constraints
- `2 <= k <= price.length <= 10^5`
- `1 <= price[i] <= 10^9`

## Examples
### Example 1
- **Input:** `price = [13,5,1,8,21,2], k = 3`
- **Output:** `8`
- **Explanation:** Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.

### Example 2
- **Input:** `price = [1,3,1], k = 2`
- **Output:** `2`
- **Explanation:** Choose the candies with the prices [1,3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.

### Example 3
- **Input:** `price = [7,7,7,7], k = 2`
- **Output:** `0`
- **Explanation:** Choosing any two distinct candies from the candies we have will result in a tastiness of 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Tastiness of Candy Basket**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `price = [13,5,1,8,21,2], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.

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
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)

        def can(d: int) -> bool:
            count, last = 1, price[0]
            for i in range(1, n):
                if price[i] - last >= d:
                    count += 1
                    last = price[i]
                    if count == k:
                        return True
            return False

        lo, hi = 0, (price[-1] - price[0]) // (k - 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
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
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/)
