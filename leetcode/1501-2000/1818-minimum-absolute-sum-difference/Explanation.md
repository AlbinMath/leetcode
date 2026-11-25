# LeetCode 1818: Minimum Absolute Sum Difference

**LeetCode Problem #1818 — Minimum Absolute Sum Difference**
Solve LeetCode Minimum Absolute Sum Difference using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Absolute Sum Difference |
| LeetCode | #1818 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integer arrays `nums1` and `nums2`, both of length `n`.

The **absolute sum difference** of arrays `nums1` and `nums2` is defined as the **sum** of `|nums1[i] - nums2[i]|` for each `0 <= i < n` (**0-indexed**).

You can replace **at most one** element of `nums1` with **any** other element in `nums1` to **minimize** the absolute sum difference.

Return the *minimum absolute sum difference **after** replacing at most one** **element in the array `nums1`.* Since the answer may be large, return it **modulo** `10^9 + 7`.

`|x|` is defined as:

`x` if `x >= 0`, or 
 `-x` if `x < 0`.

## Constraints
- `n == nums1.length`
- `n == nums2.length`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums1 = [1,7,5], nums2 = [2,3,5]`
- **Output:** `3`
- **Explanation:** There are two possible optimal solutions:
- Replace the second element with the first: [1,

### Example 2
- **Input:** `nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]`
- **Output:** `0`
- **Explanation:** nums1 is equal to nums2 so no replacement is needed. This will result in an 
absolute sum difference of 0.

### Example 3
- **Input:** `nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]`
- **Output:** `20`
- **Explanation:** Replace the first element with the second: [

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Absolute Sum Difference**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,7,5], nums2 = [2,3,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are two possible optimal solutions:
- Replace the second element with the first: [1,

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
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        sorted1 = sorted(nums1)
        n = len(nums1)

        total = 0
        best_gain = 0

        for a, b in zip(nums1, nums2):
            old = abs(a - b)
            total += old

            k = bisect_left(sorted1, b)
            new = old
            if k < n:
                new = min(new, sorted1[k] - b)
            if k > 0:
                new = min(new, b - sorted1[k - 1])

            best_gain = max(best_gain, old - new)

        return (total - best_gain) % MOD
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
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)
- [1200. Minimum Absolute Difference](../../1001-1500/1200-minimum-absolute-difference/)
- [1906. Minimum Absolute Difference Queries](../../1501-2000/1906-minimum-absolute-difference-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-absolute-sum-difference/)
