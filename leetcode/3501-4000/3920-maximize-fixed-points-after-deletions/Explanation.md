# LeetCode 3920: Maximize Fixed Points After Deletions

**LeetCode Problem #3920 — Maximize Fixed Points After Deletions**
Solve LeetCode Maximize Fixed Points After Deletions using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Fixed Points After Deletions |
| LeetCode | #3920 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
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
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Fixed Points After Deletions**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
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
**Array / General**

## Topics
- Array

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
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [1799. Maximize Score After N Operations](../../1501-2000/1799-maximize-score-after-n-operations/)
- [2920. Maximum Points After Collecting Coins From All Nodes](../../2501-3000/2920-maximum-points-after-collecting-coins-from-all-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-fixed-points-after-deletions/)
