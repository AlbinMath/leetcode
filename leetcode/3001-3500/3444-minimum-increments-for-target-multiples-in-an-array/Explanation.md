# LeetCode 3444: Minimum Increments for Target Multiples in an Array

**LeetCode Problem #3444 — Minimum Increments for Target Multiples in an Array**
Solve LeetCode Minimum Increments for Target Multiples in an Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Increments for Target Multiples in an Array |
| LeetCode | #3444 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two arrays, `nums` and `target`.

In a single operation, you may increment any element of `nums` by 1.

Return **the minimum number** of operations required so that each element in `target` has **at least** one multiple in `nums`.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `1 <= target.length <= 4`
- `target.length <= nums.length`
- `1 <= nums[i], target[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], target = [4]`
- **Output:** `1`
- **Explanation:** The minimum number of operations required to satisfy the condition is 1. 

 
 Increment 3 to 4 with just one operation, making 4 a multiple of itself.

### Example 2
- **Input:** `nums = [8,4], target = [10,5]`
- **Output:** `2`
- **Explanation:** The minimum number of operations required to satisfy the condition is 2. 

 
 Increment 8 to 10 with 2 operations, making 10 a multiple of both 5 and 10.

### Example 3
- **Input:** `nums = [7,9,10], target = [7]`
- **Output:** `0`
- **Explanation:** Target 7 already has a multiple in nums, so no additional operations are needed.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Increments for Target Multiples in an Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], target = [4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The minimum number of operations required to satisfy the condition is 1. 

 
 Increment 3 to 4 with just one operation, making 4 a multiple of itself.

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
from math import gcd

class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        m = len(target)
        full = (1 << m) - 1

        lcm = [1] * (1 << m)
        for mask in range(1, 1 << m):
            low = (mask & -mask).bit_length() - 1
            prev = mask & (mask - 1)
            l = lcm[prev]
            t = target[low]
            lcm[mask] = l * t // gcd(l, t)

        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0

        for x in nums:
            cost = [0] * (1 << m)
            for s in range(1, 1 << m):
                cost[s] = (-x) % lcm[s]
            new = dp[:]
            for mask in range(1 << m):
                if dp[mask] == INF:
                    continue
                rest = full ^ mask
                sub = rest
                while sub:
                    nm = mask | sub
                    v = dp[mask] + cost[sub]
                    if v < new[nm]:
                        new[nm] = v
                    sub = (sub - 1) & rest
            dp = new

        return dp[full]
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
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1526-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1558-minimum-numbers-of-function-calls-to-make-target-array/)
- [3229. Minimum Operations to Make Array Equal to Target](../../3001-3500/3229-minimum-operations-to-make-array-equal-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/)
