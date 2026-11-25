# LeetCode 3872: Longest Arithmetic Sequence After Changing At Most One Element

**LeetCode Problem #3872 — Longest Arithmetic Sequence After Changing At Most One Element**
Solve LeetCode Longest Arithmetic Sequence After Changing At Most One Element using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Arithmetic Sequence After Changing At Most One Element |
| LeetCode | #3872 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A subarray is **arithmetic** if the difference between consecutive elements in the subarray is constant.

You can replace **at most one** element in `nums` with any **integer**. Then, you select an arithmetic subarray from `nums`.

Return an integer denoting the **maximum** length of the arithmetic subarray you can select.

## Constraints
- `4 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [9,7,5,10,1]`
- **Output:** `5`
- **Explanation:** Replace `nums[3] = 10` with 3. The array becomes `[9, 7, 5, 3, 1]`. 
 Select the subarray [

### Example 2
- **Input:** `nums = [1,2,6,7]`
- **Output:** `3`
- **Explanation:** Replace `nums[0] = 1` with -2. The array becomes `[-2, 2, 6, 7]`. 
 Select the subarray [

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Arithmetic Sequence After Changing At Most One Element**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [9,7,5,10,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Replace `nums[3] = 10` with 3. The array becomes `[9, 7, 5, 3, 1]`. 
 Select the subarray [

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
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        L = [1] * n
        R = [1] * n
        L[1] = 2
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                L[i] = L[i - 1] + 1
            else:
                L[i] = 2
        R[n - 2] = 2
        for i in range(n - 3, -1, -1):
            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
                R[i] = R[i + 1] + 1
            else:
                R[i] = 2

        ans = max(L)
        for k in range(n):
            if k >= 1:
                ans = max(ans, L[k - 1] + 1)
            if k + 1 < n:
                ans = max(ans, R[k + 1] + 1)
            if 1 <= k <= n - 2:
                diff = nums[k + 1] - nums[k - 1]
                if diff % 2 == 0:
                    d = diff // 2
                    left = L[k - 1] if k >= 2 and nums[k - 1] - nums[k - 2] == d else 1
                    right = R[k + 1] if k + 2 < n and nums[k + 2] - nums[k + 1] == d else 1
                    ans = max(ans, left + 1 + right)
        return ans
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
- [3830. Longest Alternating Subarray After Removing At Most One Element](../../3501-4000/3830-longest-alternating-subarray-after-removing-at-most-one-element/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1001-1500/1493-longest-subarray-of-1s-after-deleting-one-element/)
- [4064. Longest Subarray Divisible by K with At Most One Negation II](../../4001-4500/4064-longest-subarray-divisible-by-k-with-at-most-one-negation-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/)
