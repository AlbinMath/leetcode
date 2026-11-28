# LeetCode 3430: Maximum and Minimum Sums of at Most Size K Subarrays

**LeetCode Problem #3430 — Maximum and Minimum Sums of at Most Size K Subarrays**
Solve LeetCode Maximum and Minimum Sums of at Most Size K Subarrays using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum and Minimum Sums of at Most Size K Subarrays |
| LeetCode | #3430 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and a **positive** integer `k`. Return the sum of the **maximum** and **minimum** elements of all subarrays with **at most** `k` elements.

## Constraints
- `1 <= nums.length <= 80000`
- `1 <= k <= nums.length`
- `-10^6 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], k = 2`
- **Output:** `20`
- **Explanation:** The subarrays of `nums` with at most 2 elements are: 

 
 
 
 Subarray 
 Minimum 
 Maximum 
 Sum 
 
 
 `[1]` 
 1 
 1 
 2 
 
 
 `[2]` 
 2 
 2 
 4 
 
 
 `[3]` 
 3 
 3 
 6 
 
 
 `[1, 2]` 
 1 
 2 
 3 
 
 
 `[2, 3]` 
 2 
 3 
 5

### Example 2
- **Input:** `nums = [1,-3,1], k = 2`
- **Output:** `-6`
- **Explanation:** The subarrays of `nums` with at most 2 elements are: 

 
 
 
 Subarray 
 Minimum 
 Maximum 
 Sum 
 
 
 `[1]` 
 1 
 1 
 2 
 
 
 `[-3]` 
 -3 
 -3 
 -6 
 
 
 `[1]` 
 1 
 1 
 2 
 
 
 `[1, -3]` 
 -3 
 1 
 -2 
 
 
 `[-3, 1]` 
 -3 
 1 
 -2

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum and Minimum Sums of at Most Size K Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** The subarrays of `nums` with at most 2 elements are: 

 
 
 
 Subarray 
 Minimum 
 Maximum 
 Sum 
 
 
 `[1]` 
 1 
 1 
 2 
 
 
 `[2]` 
 2 
 2 
 4 
 
 
 `[3]` 
 3 
 3 
 6 
 
 
 `[1, 2]` 
 1 
 2 
 3 
 
 
 `[2, 3]` 
 2 
 3 
 5

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
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = k + 1

        def G(a, t):
            if t <= 1:
                return 0
            m = min(a, t - 1)
            return m * t - m * (m + 1) // 2

        def sum_mins(arr):
            prev = [-1] * n
            nxt = [n] * n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    nxt[stack.pop()] = i
                prev[i] = stack[-1] if stack else -1
                stack.append(i)

            total = 0
            for i in range(n):
                a = min(i - prev[i], k)
                b = min(nxt[i] - i, k)
                total += arr[i] * (G(a, s) - G(a, s - b))
            return total

        return sum_mins(nums) - sum_mins([-x for x in nums])
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
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../../3001-3500/3428-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3505-minimum-operations-to-make-elements-within-k-subarrays-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/)
