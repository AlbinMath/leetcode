# LeetCode 581: Shortest Unsorted Continuous Subarray

**LeetCode Problem #581 — Shortest Unsorted Continuous Subarray**
Solve LeetCode Shortest Unsorted Continuous Subarray using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Unsorted Continuous Subarray |
| LeetCode | #581 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return *the shortest such subarray and output its length*.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,6,4,8,10,9,15]`
- **Output:** `5`
- **Explanation:** You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

### Example 2
- **Input:** `nums = [1,2,3,4]`
- **Output:** `0`

### Example 3
- **Input:** `nums = [1]`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Unsorted Continuous Subarray**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,6,4,8,10,9,15]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

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
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, -1

        mx = float('-inf')
        for i in range(n):
            if nums[i] < mx:
                end = i
            else:
                mx = nums[i]

        mn = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > mn:
                start = i
            else:
                mn = nums[i]

        return end - start + 1
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
- [862. Shortest Subarray with Sum at Least K](../../0501-1000/0862-shortest-subarray-with-sum-at-least-k/)
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../../1501-2000/1574-shortest-subarray-to-be-removed-to-make-array-sorted/)
- [3095. Shortest Subarray With OR at Least K I](../../3001-3500/3095-shortest-subarray-with-or-at-least-k-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)
