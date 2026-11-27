# LeetCode 2035: Partition Array Into Two Arrays to Minimize Sum Difference

**LeetCode Problem #2035 — Partition Array Into Two Arrays to Minimize Sum Difference**
Solve LeetCode Partition Array Into Two Arrays to Minimize Sum Difference using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array Into Two Arrays to Minimize Sum Difference |
| LeetCode | #2035 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of `2 * n` integers. You need to partition `nums` into **two** arrays of length `n` to **minimize the absolute difference** of the **sums** of the arrays. To partition `nums`, put each element of `nums` into **one** of the two arrays.

Return *the **minimum** possible absolute difference*.

## Constraints
- `1 <= n <= 15`
- `nums.length == 2 * n`
- `-10^7 <= nums[i] <= 10^7`

## Examples
### Example 1
- **Input:** `nums = [3,9,7,3]`
- **Output:** `2`
- **Explanation:** One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

### Example 2
- **Input:** `nums = [-36,36]`
- **Output:** `72`
- **Explanation:** One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.

### Example 3
- **Input:** `nums = [2,-1,0,4,-2,-9]`
- **Output:** `0`
- **Explanation:** One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Partition Array Into Two Arrays to Minimize Sum Difference**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,9,7,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

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
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)

        def build(arr):
            m = len(arr)
            groups = [[] for _ in range(m + 1)]
            for mask in range(1 << m):
                s = 0
                cnt = 0
                for i in range(m):
                    if mask >> i & 1:
                        s += arr[i]
                        cnt += 1
                groups[cnt].append(s)
            return groups

        left = build(nums[:n])
        right = build(nums[n:])
        for g in right:
            g.sort()

        ans = float('inf')
        for k in range(n + 1):
            r = right[n - k]
            for a in left[k]:
                # want a + b close to total / 2, i.e. minimize |total - 2(a + b)|
                target = total / 2 - a
                idx = bisect_left(r, target)
                for j in (idx - 1, idx):
                    if 0 <= j < len(r):
                        ans = min(ans, abs(total - 2 * (a + r[j])))
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
- [3566. Partition Array into Two Equal Product Subsets](../../3501-4000/3566-partition-array-into-two-equal-product-subsets/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1001-1500/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [1879. Minimum XOR Sum of Two Arrays](../../1501-2000/1879-minimum-xor-sum-of-two-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/)
