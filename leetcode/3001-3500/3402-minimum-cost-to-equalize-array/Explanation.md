# LeetCode 3139: Minimum Cost to Equalize Array

**LeetCode Problem #3139 — Minimum Cost to Equalize Array**
Solve LeetCode Minimum Cost to Equalize Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Equalize Array |
| LeetCode | #3139 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers `cost1` and `cost2`. You are allowed to perform **either** of the following operations **any** number of times:

Choose an index `i` from `nums` and **increase** `nums[i]` by `1` for a cost of `cost1`. 
 Choose two **different** indices `i`, `j`, from `nums` and **increase** `nums[i]` and `nums[j]` by `1` for a cost of `cost2`.

Return the **minimum** **cost** required to make all elements in the array **equal***. *

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`
- `1 <= cost1 <= 10^6`
- `1 <= cost2 <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [4,1], cost1 = 5, cost2 = 2`
- **Output:** `15`
- **Explanation:** The following operations can be performed to make the values equal: 

 
 Increase `nums[1]` by 1 for a cost of 5. `nums` becomes `[4,2]`. 
 Increase `nums[1]` by 1 for a cost of 5. `nums` becomes `[4,3]`. 
 Increase `nums[1]` by 1 for a cost of 5. `nums` becomes `[4,4]`. 
 

 The total cost is 15.

### Example 2
- **Input:** `nums = [2,3,3,3,5], cost1 = 2, cost2 = 1`
- **Output:** `6`
- **Explanation:** The following operations can be performed to make the values equal: 

 
 Increase `nums[0]` and `nums[1]` by 1 for a cost of 1. `nums` becomes `[3,4,3,3,5]`. 
 Increase `nums[0]` and `nums[2]` by 1 for a cost of 1. `nums` becomes `[4,4,4,3,5]`. 
 Increase `nums[0]` and `nums[3]` by 1 for a cost of 1. `nums` becomes `[5,4,4,4,5]`. 
 Increase `nums[1]` and `nums[2]` by 1 for a cost of 1. `nums` becomes `[5,5,5,4,5]`. 
 Increase `nums[3]` by 1 for a cost of 2. `nums` becomes `[5,5,5,5,5]`. 
 

 The total cost is 6.

### Example 3
- **Input:** `nums = [3,5,3], cost1 = 1, cost2 = 3`
- **Output:** `4`
- **Explanation:** The following operations can be performed to make the values equal: 

 
 Increase `nums[0]` by 1 for a cost of 1. `nums` becomes `[4,5,3]`. 
 Increase `nums[0]` by 1 for a cost of 1. `nums` becomes `[5,5,3]`. 
 Increase `nums[2]` by 1 for a cost of 1. `nums` becomes `[5,5,4]`. 
 Increase `nums[2]` by 1 for a cost of 1. `nums` becomes `[5,5,5]`. 
 

 The total cost is 4.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Equalize Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,1], cost1 = 5, cost2 = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** The following operations can be performed to make the values equal: 

 
 Increase `nums[1]` by 1 for a cost of 5. `nums` becomes `[4,2]`. 
 Increase `nums[1]` by 1 for a cost of 5. `nums` becomes `[4,3]`. 
 Increase `nums[1]` by 1 for a cost of 5. `nums` becomes `[4,4]`. 
 

 The total cost is 15.

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
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        S = sum(nums)
        lo = min(nums)
        hi = max(nums)

        if n == 1:
            return 0

        # pairing is useless
        if cost2 >= 2 * cost1:
            return (n * hi - S) * cost1 % MOD

        best = None
        for T in range(hi, 2 * hi + 1):
            total = n * T - S
            mx = T - lo
            if mx <= total - mx:
                cost = (total // 2) * cost2 + (total % 2) * cost1
            else:
                pairs = total - mx
                cost = pairs * cost2 + (mx - pairs) * cost1
            if best is None or cost < best:
                best = cost
        return best % MOD
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
- [3010. Divide an Array Into Subarrays With Minimum Cost I](../../3001-3500/3263-divide-an-array-into-subarrays-with-minimum-cost-i/)
- [3013. Divide an Array Into Subarrays With Minimum Cost II](../../3001-3500/3260-divide-an-array-into-subarrays-with-minimum-cost-ii/)
- [3149. Find the Minimum Cost Array Permutation](../../3001-3500/3431-find-the-minimum-cost-array-permutation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-equalize-array/)
