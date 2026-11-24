# LeetCode 2289: Steps to Make Array Non-decreasing

**LeetCode Problem #2289 — Steps to Make Array Non-decreasing**
Solve LeetCode Steps to Make Array Non-decreasing using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Steps to Make Array Non-decreasing |
| LeetCode | #2289 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. In one step, **remove** all elements `nums[i]` where `nums[i - 1] > nums[i]` for all `0 < i < nums.length`.

Return *the number of steps performed until *`nums`* becomes a **non-decreasing** array*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [5,3,4,4,7,3,6,11,8,5,11]`
- **Output:** `3`
- **Explanation:** The following are the steps performed:
- Step 1: [5,

### Example 2
- **Input:** `nums = [4,5,7,7,13]`
- **Output:** `0`
- **Explanation:** nums is already a non-decreasing array. Therefore, we return 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Steps to Make Array Non-decreasing**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,3,4,4,7,3,6,11,8,5,11]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The following are the steps performed:
- Step 1: [5,

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
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # (value, steps until removed)
        ans = 0
        for x in nums:
            cur = 0
            while stack and stack[-1][0] <= x:
                cur = max(cur, stack.pop()[1])
            cur = cur + 1 if stack else 0
            ans = max(ans, cur)
            stack.append((x, cur))
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
- [3326. Minimum Division Operations to Make Array Non Decreasing](../../3001-3500/3326-minimum-division-operations-to-make-array-non-decreasing/)
- [3523. Make Array Non-decreasing](../../3501-4000/3523-make-array-non-decreasing/)
- [2945. Find Maximum Non-decreasing Array Length](../../2501-3000/2945-find-maximum-non-decreasing-array-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/steps-to-make-array-non-decreasing/)
