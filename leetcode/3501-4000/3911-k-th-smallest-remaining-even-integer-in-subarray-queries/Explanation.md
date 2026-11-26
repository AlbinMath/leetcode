# LeetCode 3911: K-th Smallest Remaining Even Integer in Subarray Queries

**LeetCode Problem #3911 — K-th Smallest Remaining Even Integer in Subarray Queries**
Solve LeetCode K-th Smallest Remaining Even Integer in Subarray Queries using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-th Smallest Remaining Even Integer in Subarray Queries |
| LeetCode | #3911 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` where `nums` is ** strictly increasing **.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i, k_i]`.

For each query `[l_i, r_i, k_i]`:

Consider the ** subarray ** `nums[l_i..r_i]` 
 From the **infinite** sequence of all **positive even integers**: `2, 4, 6, 8, 10, 12, 14, ...` 
 **Remove** all elements that appear in the **subarray** `nums[l_i..r_i]`. 
 Find the `k_i^th` **smallest integer** remaining in the sequence after the removals.

Return an integer array `ans`, where `ans[i]` is the result for the `i^th` query.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `nums` is strictly increasing
- `1 <= queries.length <= 10^5`
- `queries[i] = [l_i, r_i, k_i]`
- `0 <= l_i <= r_i < nums.length`
- `1 <= k_i <= 10^9`​​​​​​​

## Examples
### Example 1
- **Input:** `nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]`
- **Output:** `[2,6,6]`
- **Explanation:** `i` 
 `queries[i]` 
 `nums[l_i..r_i]` 
 Removed 
 Evens 
 Remaining 
 Evens 
 `k_i` 
 `ans[i]` 
 
 
 
 
 0 
 [0, 2, 1] 
 [1, 4, 7] 
 [4] 
 2, 6, 8, ... 
 1 
 2 
 
 
 1 
 [1, 1, 2] 
 [4] 
 [4] 
 2, 6, 8, ... 
 2 
 6 
 
 
 2 
 [0, 0, 3] 
 [1] 
 [] 
 2, 4, 6, ... 
 3 
 6 
 
 
 

 Thus, `ans = [2, 6, 6]`.

### Example 2
- **Input:** `nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]`
- **Output:** `[6,2,12]`
- **Explanation:** `i` 
 `queries[i]` 
 `nums[l_i..r_i]` 
 Removed 
 Evens 
 Remaining 
 Evens 
 `k_i` 
 `ans[i]` 
 
 
 
 
 0 
 [0, 1, 2] 
 [2, 5] 
 [2] 
 4, 6, 8, ... 
 2 
 6 
 
 
 1 
 [1, 2, 1] 
 [5, 8] 
 [8] 
 2, 4, 6, ... 
 1 
 2 
 
 
 2 
 [0, 2, 4] 
 [2, 5, 8] 
 [2, 8] 
 4, 6, 10, 12, ... 
 4 
 12 
 
 
 

 Thus, `ans = [6, 2, 12]`.

### Example 3
- **Input:** `nums = [3,6], queries = [[0,1,1],[1,1,3]]`
- **Output:** `[2,8]`
- **Explanation:** `i` 
 `queries[i]` 
 `nums[l_i..r_i]` 
 Removed 
 Evens 
 Remaining 
 Evens 
 `k_i` 
 `ans[i]` 
 
 
 
 
 0 
 [0, 1, 1] 
 [3, 6] 
 [6] 
 2, 4, 8, ... 
 1 
 2 
 
 
 1 
 [1, 1, 3] 
 [6] 
 [6] 
 2, 4, 8, ... 
 3 
 8 
 
 
 

 Thus, `ans = [2, 8]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **K-th Smallest Remaining Even Integer in Subarray Queries**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,6,6]`.
4. **Verification:** `i` 
 `queries[i]` 
 `nums[l_i..r_i]` 
 Removed 
 Evens 
 Remaining 
 Evens 
 `k_i` 
 `ans[i]` 
 
 
 
 
 0 
 [0, 2, 1] 
 [1, 4, 7] 
 [4] 
 2, 6, 8, ... 
 1 
 2 
 
 
 1 
 [1, 1, 2] 
 [4] 
 [4] 
 2, 6, 8, ... 
 2 
 6 
 
 
 2 
 [0, 0, 3] 
 [1] 
 [] 
 2, 4, 6, ... 
 3 
 6 
 
 
 

 Thus, `ans = [2, 6, 6]`.

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
    def kthRemainingInteger(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ev = []
        cnt = [0] * (n + 1)
        for i, x in enumerate(nums):
            cnt[i + 1] = cnt[i]
            if x % 2 == 0:
                ev.append(x // 2)
                cnt[i + 1] += 1

        ans = []
        for l, r, k in queries:
            a, b = cnt[l], cnt[r + 1]
            lo, hi = 0, b - a          # c in [0, b-a]
            while lo < hi:
                mid = (lo + hi) // 2
                if ev[a + mid] - (mid + 1) < k:
                    lo = mid + 1
                else:
                    hi = mid
            ans.append(2 * (k + lo))
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
- [440. K-th Smallest in Lexicographical Order](../../0001-0500/0440-k-th-smallest-in-lexicographical-order/)
- [719. Find K-th Smallest Pair Distance](../../0501-1000/0719-find-k-th-smallest-pair-distance/)
- [786. K-th Smallest Prime Fraction](../../0501-1000/0786-k-th-smallest-prime-fraction/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/)
