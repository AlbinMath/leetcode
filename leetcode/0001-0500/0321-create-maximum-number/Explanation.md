# LeetCode 321: Create Maximum Number

**LeetCode Problem #321 — Create Maximum Number**
Solve LeetCode Create Maximum Number using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Maximum Number |
| LeetCode | #321 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. `nums1` and `nums2` represent the digits of two numbers. You are also given an integer `k`.

Create the maximum number of length `k <= m + n` from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the `k` digits representing the answer.

## Constraints
- `m == nums1.length`
- `n == nums2.length`
- `1 <= m, n <= 500`
- `0 <= nums1[i], nums2[i] <= 9`
- `1 <= k <= m + n`
- `nums1` and `nums2` do not have leading zeros.

## Examples
### Example 1
- **Input:** `nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5`
- **Output:** `[9,8,6,5,3]`

### Example 2
- **Input:** `nums1 = [6,7], nums2 = [6,0,4], k = 5`
- **Output:** `[6,7,6,0,4]`

### Example 3
- **Input:** `nums1 = [3,9], nums2 = [8,9], k = 3`
- **Output:** `[9,8,9]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Create Maximum Number**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[9,8,6,5,3]`.

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
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, t):
            drop = len(nums) - t
            st = []
            for d in nums:
                while drop and st and st[-1] < d:
                    st.pop()
                    drop -= 1
                st.append(d)
            return st[:t]

        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a[0])
                    a = a[1:]
                else:
                    res.append(b[0])
                    b = b[1:]
            return res

        m, n = len(nums1), len(nums2)
        best = []
        for i in range(max(0, k - n), min(k, m) + 1):
            cand = merge(pick(nums1, i), pick(nums2, k - i))
            if cand > best:
                best = cand
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
- [414. Third Maximum Number](../../0001-0500/0414-third-maximum-number/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1147-flip-columns-for-maximum-number-of-equal-rows/)
- [1189. Maximum Number of Balloons](../../1001-1500/1297-maximum-number-of-balloons/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-maximum-number/)
