# LeetCode 1856: Maximum Subarray Min-Product

**LeetCode Problem #1856 — Maximum Subarray Min-Product**
Solve LeetCode Maximum Subarray Min-Product using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray Min-Product |
| LeetCode | #1856 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **min-product** of an array is equal to the **minimum value** in the array **multiplied by** the array's **sum**.

For example, the array `[3,2,5]` (minimum value is `2`) has a min-product of `2 * (3+2+5) = 2 * 10 = 20`.

Given an array of integers `nums`, return *the **maximum min-product** of any **non-empty subarray** of *`nums`. Since the answer may be large, return it **modulo** `10^9 + 7`.

Note that the min-product should be maximized **before** performing the modulo operation. Testcases are generated such that the maximum min-product **without** modulo will fit in a **64-bit signed integer**.

A **subarray** is a **contiguous** part of an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^7`

## Examples
### Example 1
- **Input:** `nums = [1, 2,3,2 ]`
- **Output:** `14`
- **Explanation:** The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

### Example 2
- **Input:** `nums = [2, 3,3 ,1,2]`
- **Output:** `18`
- **Explanation:** The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.

### Example 3
- **Input:** `nums = [3,1, 5,6,4 ,2]`
- **Output:** `60`
- **Explanation:** The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Subarray Min-Product**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1, 2,3,2 ]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + x

        stack = []
        best = 0
        for j in range(n + 1):
            cur = nums[j] if j < n else 0
            while stack and nums[stack[-1]] >= cur:
                i = stack.pop()
                left = stack[-1] + 1 if stack else 0
                best = max(best, nums[i] * (pre[j] - pre[left]))
            stack.append(j)

        return best % (10**9 + 7)
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [152. Maximum Product Subarray](../../0001-0500/0152-maximum-product-subarray/)
- [1567. Maximum Length of Subarray With Positive Product](../../1501-2000/1567-maximum-length-of-subarray-with-positive-product/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-subarray-min-product/)
