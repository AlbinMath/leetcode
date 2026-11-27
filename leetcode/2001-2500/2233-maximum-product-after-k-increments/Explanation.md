# LeetCode 2233: Maximum Product After K Increments

**LeetCode Problem #2233 — Maximum Product After K Increments**
Solve LeetCode Maximum Product After K Increments using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product After K Increments |
| LeetCode | #2233 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of non-negative integers `nums` and an integer `k`. In one operation, you may choose **any** element from `nums` and **increment** it by `1`.

Return* the **maximum** **product** of *`nums`* after **at most** *`k`* operations. *Since the answer may be very large, return it modulo `10^9 + 7`. Note that you should maximize the product before taking the modulo.

## Constraints
- `1 <= nums.length, k <= 10^5`
- `0 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [0,4], k = 5`
- **Output:** `20`
- **Explanation:** Increment the first number 5 times.
Now nums = [5, 4], with a product of 5 * 4 = 20.
It can be shown that 20 is maximum product possible, so we return 20.
Note that there may be other ways to increment nums to have the maximum product.

### Example 2
- **Input:** `nums = [6,3,3,2], k = 2`
- **Output:** `216`
- **Explanation:** Increment the second number 1 time and increment the fourth number 1 time.
Now nums = [6, 4, 3, 3], with a product of 6 * 4 * 3 * 3 = 216.
It can be shown that 216 is maximum product possible, so we return 216.
Note that there may be other ways to increment nums to have the maximum product.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Product After K Increments**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,4], k = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** Increment the first number 5 times.
Now nums = [5, 4], with a product of 5 * 4 = 20.
It can be shown that 20 is maximum product possible, so we return 20.
Note that there may be other ways to increment nums to have the maximum product.

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
import heapq
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heapreplace(nums, nums[0] + 1)
        ans = 1
        for x in nums:
            ans = ans * x % MOD
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
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2106-maximum-fruits-harvested-after-at-most-k-steps/)
- [3443. Maximum Manhattan Distance After K Changes](../../3001-3500/3443-maximum-manhattan-distance-after-k-changes/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-after-k-increments/)
