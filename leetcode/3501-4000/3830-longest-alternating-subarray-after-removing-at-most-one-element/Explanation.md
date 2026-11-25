# LeetCode 3830: Longest Alternating Subarray After Removing At Most One Element

**LeetCode Problem #3830 — Longest Alternating Subarray After Removing At Most One Element**
Solve LeetCode Longest Alternating Subarray After Removing At Most One Element using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Alternating Subarray After Removing At Most One Element |
| LeetCode | #3830 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A subarray `nums[l..r]` is **alternating** if one of the following holds:

`nums[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...` 
 `nums[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...`

In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between **strictly** greater and **strictly** smaller.

You can remove **at most one** element from `nums`. Then, you select an alternating subarray from `nums`.

Return an integer denoting the **maximum** **length** of the alternating subarray you can select.

A subarray of length 1 is considered alternating.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,2]`
- **Output:** `4`
- **Explanation:** Choose not to remove elements. 
 Select the entire array [

### Example 2
- **Input:** `nums = [3,2,1,2,3,2,1]`
- **Output:** `4`
- **Explanation:** Choose to remove `nums[3]` i.e., [3, 2, 1,

### Example 3
- **Input:** `nums = [100000,100000]`
- **Output:** `1`
- **Explanation:** Choose not to remove elements. 
 Select the subarray [100000,

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Alternating Subarray After Removing At Most One Element**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Choose not to remove elements. 
 Select the entire array [

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
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        end_hi = [1] * n
        end_lo = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                end_hi[i] = end_lo[i - 1] + 1
            elif nums[i - 1] > nums[i]:
                end_lo[i] = end_hi[i - 1] + 1

        start_hi = [1] * n
        start_lo = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                start_hi[i] = start_lo[i + 1] + 1
            elif nums[i] < nums[i + 1]:
                start_lo[i] = start_hi[i + 1] + 1

        ans = max(max(end_hi), max(end_lo))
        for k in range(1, n - 1):
            a, b = nums[k - 1], nums[k + 1]
            if a < b:
                ans = max(ans, end_lo[k - 1] + start_hi[k + 1])
            elif a > b:
                ans = max(ans, end_hi[k - 1] + start_lo[k + 1])
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
- [3872. Longest Arithmetic Sequence After Changing At Most One Element](../../3501-4000/3872-longest-arithmetic-sequence-after-changing-at-most-one-element/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1001-1500/1493-longest-subarray-of-1s-after-deleting-one-element/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3001-3500/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/)
