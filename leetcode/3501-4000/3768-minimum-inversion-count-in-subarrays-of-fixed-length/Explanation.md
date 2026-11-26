# LeetCode 3768: Minimum Inversion Count in Subarrays of Fixed Length

**LeetCode Problem #3768 — Minimum Inversion Count in Subarrays of Fixed Length**
Solve LeetCode Minimum Inversion Count in Subarrays of Fixed Length using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Inversion Count in Subarrays of Fixed Length |
| LeetCode | #3768 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `k`.

An **inversion** is a pair of indices `(i, j)` from `nums` such that `i < j` and `nums[i] > nums[j]`.

The **inversion count** of a ** subarray ** is the number of inversions within it.

Return the **minimum** inversion count among all **subarrays** of `nums` with length `k`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `nums = [3,1,2,5,4], k = 3`
- **Output:** `0`
- **Explanation:** We consider all subarrays of length `k = 3` (indices below are relative to each subarray): 

 
 `[3, 1, 2]` has 2 inversions: `(0, 1)` and `(0, 2)`. 
 `[1, 2, 5]` has 0 inversions. 
 `[2, 5, 4]` has 1 inversion: `(1, 2)`. 
 

 The minimum inversion count among all subarrays of length `3` is 0, achieved by subarray `[1, 2, 5]`.

### Example 2
- **Input:** `nums = [5,3,2,1], k = 4`
- **Output:** `6`
- **Explanation:** There is only one subarray of length `k = 4`: `[5, 3, 2, 1]`. 
Within this subarray, the inversions are: `(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 2)`, `(1, 3)`, and `(2, 3)`. 
Total inversions is 6, so the minimum inversion count is 6.

### Example 3
- **Input:** `nums = [2,1], k = 1`
- **Output:** `0`
- **Explanation:** All subarrays of length `k = 1` contain only one element, so no inversions are possible. 
The minimum inversion count is therefore 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Inversion Count in Subarrays of Fixed Length**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,2,5,4], k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** We consider all subarrays of length `k = 3` (indices below are relative to each subarray): 

 
 `[3, 1, 2]` has 2 inversions: `(0, 1)` and `(0, 2)`. 
 `[1, 2, 5]` has 0 inversions. 
 `[2, 5, 4]` has 1 inversion: `(1, 2)`. 
 

 The minimum inversion count among all subarrays of length `3` is 0, achieved by subarray `[1, 2, 5]`.

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
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        tree = [0] * (m + 1)

        def update(i, d):
            while i <= m:
                tree[i] += d
                i += i & -i

        def query(i):  # number of stored values with rank <= i
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        a = [rank[x] for x in nums]

        inv = 0
        size = 0
        for i in range(k):
            inv += size - query(a[i])   # elements already present that are larger
            update(a[i], 1)
            size += 1
        best = inv

        for r in range(k, n):
            l = r - k
            # remove nums[l]: it is leftmost, inverted with smaller elements to its right
            update(a[l], -1)
            size -= 1
            inv -= query(a[l] - 1)
            # add nums[r]: it is rightmost, inverted with larger elements to its left
            inv += size - query(a[r])
            update(a[r], 1)
            size += 1
            best = min(best, inv)
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
- [2444. Count Subarrays With Fixed Bounds](../../2001-2500/2444-count-subarrays-with-fixed-bounds/)
- [1588. Sum of All Odd Length Subarrays](../../1501-2000/1588-sum-of-all-odd-length-subarrays/)
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1750-minimum-length-of-string-after-deleting-similar-ends/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/)
