# LeetCode 3891: Minimum Increase to Maximize Special Indices

**LeetCode Problem #3891 — Minimum Increase to Maximize Special Indices**
Solve LeetCode Minimum Increase to Maximize Special Indices using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Increase to Maximize Special Indices |
| LeetCode | #3891 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

An index `i` (`0 < i < n - 1`) is **special** if `nums[i] > nums[i - 1]` and `nums[i] > nums[i + 1]`.

You may perform operations where you choose **any** index `i` and **increase** `nums[i]` by 1.

Your goal is to:

**Maximize** the number of **special** indices. 
 **Minimize** the total number of **operations** required to achieve that **maximum**.

Return an integer denoting the **minimum** total number of operations required.

## Constraints
- `3 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,2]`
- **Output:** `1`
- **Explanation:** ​​​​​​​ 

 
 Start with `nums = [1, 2, 2]`. 
 Increase `nums[1]` by 1, array becomes `[1, 3, 2]`. 
 The final array is `[1, 3, 2]` has 1 special index, which is the maximum achievable. 
 It is impossible to achieve this number of special indices with fewer operations. Thus, the answer is 1.

### Example 2
- **Input:** `nums = [2,1,1,3]`
- **Output:** `2`
- **Explanation:** ​​​​​​​ 

 
 Start with `nums = [2, 1, 1, 3]`. 
 Perform 2 operations at index 1, array becomes `[2, 3, 1, 3]`. 
 The final array is `[2, 3, 1, 3]` has 1 special index, which is the maximum achievable. Thus, the answer is 2.

### Example 3
- **Input:** `nums = [5,2,1,4,3]`
- **Output:** `4`
- **Explanation:** ​​​​​​​​​​​​​​​​​​​​​ 

 
 Start with `nums = [5, 2, 1, 4, 3]`. 
 Perform 4 operations at index 1, array becomes `[5, 6, 1, 4, 3]`. 
 The final array is `[5, 6, 1, 4, 3]` has 2 special indices, which is the maximum achievable. Thus, the answer is 4.​​​​​​​

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Increase to Maximize Special Indices**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** ​​​​​​​ 

 
 Start with `nums = [1, 2, 2]`. 
 Increase `nums[1]` by 1, array becomes `[1, 3, 2]`. 
 The final array is `[1, 3, 2]` has 1 special index, which is the maximum achievable. 
 It is impossible to achieve this number of special indices with fewer operations. Thus, the answer is 1.

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
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        c = [0] * n
        for i in range(1, n - 1):
            c[i] = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])

        if n % 2 == 1:
            return sum(c[i] for i in range(1, n - 1, 2))

        k = (n - 2) // 2
        # pre[t] = c[1] + c[3] + ... + c[2t-1]
        pre = [0] * (k + 1)
        for t in range(1, k + 1):
            pre[t] = pre[t - 1] + c[2 * t - 1]
        # suf[t] = c[2t+2] + c[2t+4] + ... + c[n-2]
        suf = [0] * (k + 2)
        for t in range(k - 1, -1, -1):
            suf[t] = suf[t + 1] + c[2 * t + 2]

        return min(pre[t] + suf[t] for t in range(k + 1))
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
- [3919. Minimum Cost to Move Between Indices](../../3501-4000/3919-minimum-cost-to-move-between-indices/)
- [4099. Minimum Operations to Sort With Locked Indices](../../4001-4500/4099-minimum-operations-to-sort-with-locked-indices/)
- [1974. Minimum Time to Type Word Using Special Typewriter](../../1501-2000/1974-minimum-time-to-type-word-using-special-typewriter/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/)
