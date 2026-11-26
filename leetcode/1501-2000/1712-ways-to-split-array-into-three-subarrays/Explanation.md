# LeetCode 1712: Ways to Split Array Into Three Subarrays

**LeetCode Problem #1712 — Ways to Split Array Into Three Subarrays**
Solve LeetCode Ways to Split Array Into Three Subarrays using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Ways to Split Array Into Three Subarrays |
| LeetCode | #1712 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A split of an integer array is **good** if:

The array is split into three **non-empty** contiguous subarrays - named `left`, `mid`, `right` respectively from left to right. 
 The sum of the elements in `left` is less than or equal to the sum of the elements in `mid`, and the sum of the elements in `mid` is less than or equal to the sum of the elements in `right`.

Given `nums`, an array of **non-negative** integers, return *the number of **good** ways to split* `nums`. As the number may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `3 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,1,1]`
- **Output:** `1`
- **Explanation:** The only good way to split nums is [1] [1] [1].

### Example 2
- **Input:** `nums = [1,2,2,2,5,0]`
- **Output:** `3`
- **Explanation:** There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

### Example 3
- **Input:** `nums = [3,2,1]`
- **Output:** `0`
- **Explanation:** There is no good way to split nums.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Ways to Split Array Into Three Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only good way to split nums is [1] [1] [1].

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
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        total = pre[n]

        ans = 0
        lo = hi = 0
        for i in range(1, n - 1):                 # i = size of left
            L = pre[i]
            lo = max(lo, i + 1)
            while lo < n and pre[lo] < 2 * L:
                lo += 1
            hi = max(hi, lo)
            while hi < n and 2 * pre[hi] <= total + L:
                hi += 1
            ans += hi - lo                        # valid k in [lo, hi)
        return ans % MOD
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
- [2871. Split Array Into Maximum Number of Subarrays](../../2501-3000/2871-split-array-into-maximum-number-of-subarrays/)
- [2270. Number of Ways to Split Array](../../2001-2500/2270-number-of-ways-to-split-array/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0842-split-array-into-fibonacci-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/)
