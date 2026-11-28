# LeetCode 1855: Maximum Distance Between a Pair of Values

**LeetCode Problem #1855 — Maximum Distance Between a Pair of Values**
Solve LeetCode Maximum Distance Between a Pair of Values using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Distance Between a Pair of Values |
| LeetCode | #1855 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **non-increasing 0-indexed **integer arrays `nums1`​​​​​​ and `nums2`​​​​​​.

A pair of indices `(i, j)`, where `0 <= i < nums1.length` and `0 <= j < nums2.length`, is **valid** if both `i <= j` and `nums1[i] <= nums2[j]`. The **distance** of the pair is `j - i`​​​​.

Return *the **maximum distance** of any **valid** pair *`(i, j)`*. If there are no valid pairs, return *`0`.

An array `arr` is **non-increasing** if `arr[i-1] >= arr[i]` for every `1 <= i < arr.length`.

## Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^5`
- Both `nums1` and `nums2` are **non-increasing**.

## Examples
### Example 1
- **Input:** `nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]`
- **Output:** `2`
- **Explanation:** The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

### Example 2
- **Input:** `nums1 = [2,2,2], nums2 = [10,10,1]`
- **Output:** `1`
- **Explanation:** The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).

### Example 3
- **Input:** `nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]`
- **Output:** `2`
- **Explanation:** The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Distance Between a Pair of Values**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

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

class Solution:
    def maxDistance(self, nums1, nums2):
        neg2 = [-x for x in nums2]          # non-decreasing
        best = 0
        for i, x in enumerate(nums1):
            # count of j with nums2[j] >= x  <=>  -nums2[j] <= -x
            j = bisect_left(neg2, -x + 1) - 1
            if j >= i:
                best = max(best, j - i)
        return best
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
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)
- [1184. Distance Between Bus Stops](../../1001-1500/1184-distance-between-bus-stops/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/)
