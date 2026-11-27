# LeetCode 713: Subarray Product Less Than K

**LeetCode Problem #713 — Subarray Product Less Than K**
Solve LeetCode Subarray Product Less Than K using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subarray Product Less Than K |
| LeetCode | #713 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums` and an integer `k`.

Return the number of contiguous subarrays where the **product** of all the elements in the **subarray** is **strictly less** than `k`.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [10,5,2,6], k = 100`
- **Output:** `8`
- **Explanation:** The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

### Example 2
- **Input:** `nums = [1,2,3], k = 0`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Subarray Product Less Than K**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,5,2,6], k = 100`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

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
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
            
        count = 0
        prod = 1
        left = 0
        
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1
            
        return count
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
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)
- [2311. Longest Binary Subsequence Less Than or Equal to K](../../2001-2500/2311-longest-binary-subsequence-less-than-or-equal-to-k/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3007-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/)
