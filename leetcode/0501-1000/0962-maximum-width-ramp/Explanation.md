# LeetCode 962: Maximum Width Ramp

**LeetCode Problem #962 — Maximum Width Ramp**
Solve LeetCode Maximum Width Ramp using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Width Ramp |
| LeetCode | #962 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **ramp** in an integer array `nums` is a pair `(i, j)` for which `i < j` and `nums[i] <= nums[j]`. The **width** of such a ramp is `j - i`.

Given an integer array `nums`, return *the maximum width of a **ramp** in *`nums`. If there is no **ramp** in `nums`, return `0`.

## Constraints
- `2 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5 * 10^4`

## Examples
### Example 1
- **Input:** `nums = [6,0,8,2,1,5]`
- **Output:** `4`
- **Explanation:** The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

### Example 2
- **Input:** `nums = [9,8,1,0,1,9,4,0,4,1]`
- **Output:** `7`
- **Explanation:** The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Width Ramp**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [6,0,8,2,1,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

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
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, x in enumerate(nums):
            if not stack or x < nums[stack[-1]]:
                stack.append(i)

        ans = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans, j - stack.pop())
            if not stack:
                break
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
- [662. Maximum Width of Binary Tree](../../0501-1000/0662-maximum-width-of-binary-tree/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-width-ramp/)
