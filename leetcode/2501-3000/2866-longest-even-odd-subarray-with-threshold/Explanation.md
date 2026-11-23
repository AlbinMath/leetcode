# LeetCode 2760: Longest Even Odd Subarray With Threshold

**LeetCode Problem #2760 — Longest Even Odd Subarray With Threshold**
Solve LeetCode Longest Even Odd Subarray With Threshold using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Even Odd Subarray With Threshold |
| LeetCode | #2760 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `threshold`.

Find the length of the **longest subarray** of `nums` starting at index `l` and ending at index `r` `(0 <= l <= r < nums.length)` that satisfies the following conditions:

`nums[l] % 2 == 0` 
 For all indices `i` in the range `[l, r - 1]`, `nums[i] % 2 != nums[i + 1] % 2` 
 For all indices `i` in the range `[l, r]`, `nums[i] <= threshold`

Return *an integer denoting the length of the longest such subarray.*

**Note:** A **subarray** is a contiguous non-empty sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 100 `
- `1 <= nums[i] <= 100 `
- `1 <= threshold <= 100`

## Examples
### Example 1
- **Input:** `nums = [3,2,5,4], threshold = 5`
- **Output:** `3`
- **Explanation:** In this example, we can select the subarray that starts at l = 1 and ends at r = 3 => [2,5,4]. This subarray satisfies the conditions.
Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.

### Example 2
- **Input:** `nums = [1,2], threshold = 2`
- **Output:** `1`
- **Explanation:** In this example, we can select the subarray that starts at l = 1 and ends at r = 1 => [2]. 
It satisfies all the conditions and we can show that 1 is the maximum possible achievable length.

### Example 3
- **Input:** `nums = [2,3,4,5], threshold = 4`
- **Output:** `3`
- **Explanation:** In this example, we can select the subarray that starts at l = 0 and ends at r = 2 => [2,3,4]. 
It satisfies all the conditions.
Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Even Odd Subarray With Threshold**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,5,4], threshold = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In this example, we can select the subarray that starts at l = 1 and ends at r = 3 => [2,5,4]. This subarray satisfies the conditions.
Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.

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
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        curr_len = 0
        max_len = 0
        
        for i, val in enumerate(nums):
            if val > threshold:
                curr_len = 0
            elif curr_len > 0 and (val & 1) != (nums[i - 1] & 1):
                curr_len += 1
            else:
                curr_len = 1 if (val & 1) == 0 else 0
                
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len
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
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)
- [975. Odd Even Jump](../../1001-1500/1017-odd-even-jump/)
- [1116. Print Zero Even Odd](../../1001-1500/1216-print-zero-even-odd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/)
