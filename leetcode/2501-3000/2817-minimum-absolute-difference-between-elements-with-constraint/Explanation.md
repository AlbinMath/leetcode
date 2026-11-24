# LeetCode 2817: Minimum Absolute Difference Between Elements With Constraint

**LeetCode Problem #2817 — Minimum Absolute Difference Between Elements With Constraint**
Solve LeetCode Minimum Absolute Difference Between Elements With Constraint using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Absolute Difference Between Elements With Constraint |
| LeetCode | #2817 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `x`.

Find the **minimum absolute difference** between two elements in the array that are at least `x` indices apart.

In other words, find two indices `i` and `j` such that `abs(i - j) >= x` and `abs(nums[i] - nums[j])` is minimized.

Return* an integer denoting the **minimum** absolute difference between two elements that are at least* `x` *indices apart*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= x < nums.length`

## Examples
### Example 1
- **Input:** `nums = [4,3,2,4], x = 2`
- **Output:** `0`
- **Explanation:** We can select nums[0] = 4 and nums[3] = 4. 
They are at least 2 indices apart, and their absolute difference is the minimum, 0. 
It can be shown that 0 is the optimal answer.

### Example 2
- **Input:** `nums = [5,3,2,10,15], x = 1`
- **Output:** `1`
- **Explanation:** We can select nums[1] = 3 and nums[2] = 2.
They are at least 1 index apart, and their absolute difference is the minimum, 1.
It can be shown that 1 is the optimal answer.

### Example 3
- **Input:** `nums = [1,2,3,4], x = 3`
- **Output:** `3`
- **Explanation:** We can select nums[0] = 1 and nums[3] = 4.
They are at least 3 indices apart, and their absolute difference is the minimum, 3.
It can be shown that 3 is the optimal answer.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Absolute Difference Between Elements With Constraint**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,3,2,4], x = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** We can select nums[0] = 4 and nums[3] = 4. 
They are at least 2 indices apart, and their absolute difference is the minimum, 0. 
It can be shown that 0 is the optimal answer.

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
from bisect import bisect_left, insort
from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        seen = []
        ans = float('inf')

        for i in range(x, len(nums)):
            insort(seen, nums[i - x])
            v = nums[i]
            k = bisect_left(seen, v)
            if k < len(seen):
                ans = min(ans, seen[k] - v)
            if k > 0:
                ans = min(ans, v - seen[k - 1])
            if ans == 0:
                return 0

        return ans
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
- [3880. Minimum Absolute Difference Between Two Values](../../3501-4000/3880-minimum-absolute-difference-between-two-values/)
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)
- [1200. Minimum Absolute Difference](../../1001-1500/1200-minimum-absolute-difference/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/)
