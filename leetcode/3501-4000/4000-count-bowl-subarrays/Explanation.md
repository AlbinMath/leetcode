# LeetCode 3676: Count Bowl Subarrays

**LeetCode Problem #3676 — Count Bowl Subarrays**
Solve LeetCode Count Bowl Subarrays using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Bowl Subarrays |
| LeetCode | #3676 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` with **distinct** elements.

A subarray `nums[l...r]` of `nums` is called a **bowl** if:

The subarray has length at least 3. That is, `r - l + 1 >= 3`. 
 The **minimum** of its two ends is **strictly greater** than the **maximum** of all elements in between. That is, `min(nums[l], nums[r]) > max(nums[l + 1], ..., nums[r - 1])`.

Return the number of **bowl** subarrays in `nums`.

## Constraints
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `nums` consists of distinct elements.

## Examples
### Example 1
- **Input:** `nums = [2,5,3,1,4]`
- **Output:** `2`
- **Explanation:** The bowl subarrays are `[3, 1, 4]` and `[5, 3, 1, 4]`. 

 
 `[3, 1, 4]` is a bowl because `min(3, 4) = 3 > max(1) = 1`. 
 `[5, 3, 1, 4]` is a bowl because `min(5, 4) = 4 > max(3, 1) = 3`.

### Example 2
- **Input:** `nums = [5,1,2,3,4]`
- **Output:** `3`
- **Explanation:** The bowl subarrays are `[5, 1, 2]`, `[5, 1, 2, 3]` and `[5, 1, 2, 3, 4]`.

### Example 3
- **Input:** `nums = [1000000000,999999999,999999998]`
- **Output:** `0`
- **Explanation:** No subarray is a bowl.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Bowl Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,3,1,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The bowl subarrays are `[3, 1, 4]` and `[5, 3, 1, 4]`. 

 
 `[3, 1, 4]` is a bowl because `min(3, 4) = 3 > max(1) = 1`. 
 `[5, 3, 1, 4]` is a bowl because `min(5, 4) = 4 > max(3, 1) = 3`.

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
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for r, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                l = stack.pop()
                if r - l >= 2:
                    ans += 1
            if stack and r - stack[-1] >= 2:
                ans += 1
            stack.append(r)
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
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2394-count-subarrays-with-score-less-than-k/)
- [2444. Count Subarrays With Fixed Bounds](../../2501-3000/2527-count-subarrays-with-fixed-bounds/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-bowl-subarrays/)
