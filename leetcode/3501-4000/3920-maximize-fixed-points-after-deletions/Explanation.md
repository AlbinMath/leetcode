# LeetCode 3920: Maximize Fixed Points After Deletions

**LeetCode Problem #3920 — Maximize Fixed Points After Deletions**
Solve LeetCode Maximize Fixed Points After Deletions using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Fixed Points After Deletions |
| LeetCode | #3920 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A position `i` is called a **fixed point** if `nums[i] == i`.

You are allowed to delete **any** number of elements (including zero) from the array. After each deletion, the remaining elements **shift left**, and indices are reassigned starting from 0.

Return an integer denoting the **maximum** number of fixed points that can be achieved after performing any number of deletions.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [0,2,1]`
- **Output:** `2`
- **Explanation:** Delete `nums[1] = 2`. The array becomes `[0, 1]`. 
 Now, `nums[0] = 0` and `nums[1] = 1`, so both indices are fixed points. 
 Thus, the answer is 2.

### Example 2
- **Input:** `nums = [3,1,2]`
- **Output:** `2`
- **Explanation:** Do not delete any elements. The array remains `[3, 1, 2]`. 
 Here, `nums[1] = 1` and `nums[2] = 2`, so these indices are fixed points. 
 Thus, the answer is 2.

### Example 3
- **Input:** `nums = [1,0,1,2]`
- **Output:** `3`
- **Explanation:** Delete `nums[0] = 1`. The array becomes `[0, 1, 2]`. 
 Now, `nums[0] = 0`, `nums[1] = 1`, and `nums[2] = 2`, so all indices are fixed points. 
 Thus, the answer is 3.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize Fixed Points After Deletions**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,2,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Delete `nums[1] = 2`. The array becomes `[0, 1]`. 
 Now, `nums[0] = 0` and `nums[1] = 1`, so both indices are fixed points. 
 Thus, the answer is 2.

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
from bisect import bisect_left
from typing import List

class Solution:
    def maxFixedPoints(self, nums: List[int]) -> int:
        items = [(i - x, x) for i, x in enumerate(nums) if x <= i]
        items.sort()                       # b ascending, then a ascending
        tails = []
        for _, a in items:
            pos = bisect_left(tails, a)    # strictly increasing in a
            if pos == len(tails):
                tails.append(a)
            else:
                tails[pos] = a
        return len(tails)
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
- [3767. Maximize Points After Choosing K Tasks](../../3501-4000/3767-maximize-points-after-choosing-k-tasks/)
- [3654. Minimum Sum After Divisible Sum Deletions](../../3501-4000/3654-minimum-sum-after-divisible-sum-deletions/)
- [3828. Final Element After Subarray Deletions](../../3501-4000/3828-final-element-after-subarray-deletions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-fixed-points-after-deletions/)
