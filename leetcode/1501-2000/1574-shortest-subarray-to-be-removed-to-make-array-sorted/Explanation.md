# LeetCode 1574: Shortest Subarray to be Removed to Make Array Sorted

**LeetCode Problem #1574 — Shortest Subarray to be Removed to Make Array Sorted**
Solve LeetCode Shortest Subarray to be Removed to Make Array Sorted using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Subarray to be Removed to Make Array Sorted |
| LeetCode | #1574 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr`, remove a subarray (can be empty) from `arr` such that the remaining elements in `arr` are **non-decreasing**.

Return *the length of the shortest subarray to remove*.

A **subarray** is a contiguous subsequence of the array.

## Constraints
- `1 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [1,2,3,10,4,2,3,5]`
- **Output:** `3`
- **Explanation:** The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

### Example 2
- **Input:** `arr = [5,4,3,2,1]`
- **Output:** `4`
- **Explanation:** Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

### Example 3
- **Input:** `arr = [1,2,3]`
- **Output:** `0`
- **Explanation:** The array is already non-decreasing. We do not need to remove any elements.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Subarray to be Removed to Make Array Sorted**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3,10,4,2,3,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

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
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return 0

        ans = right  # remove arr[0..right-1]
        left = 0
        while left < right:
            while right < n and arr[right] < arr[left]:
                right += 1
            ans = min(ans, right - left - 1)
            if left + 1 < n and arr[left] > arr[left + 1]:
                break
            left += 1

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
- [3011. Find if Array Can Be Sorted](../../3001-3500/3011-find-if-array-can-be-sorted/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/)
