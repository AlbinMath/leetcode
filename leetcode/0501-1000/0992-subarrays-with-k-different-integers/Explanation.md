# LeetCode 992: Subarrays with K Different Integers

**LeetCode Problem #992 — Subarrays with K Different Integers**
Solve LeetCode Subarrays with K Different Integers using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subarrays with K Different Integers |
| LeetCode | #992 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return *the number of **good subarrays** of *`nums`.

A **good array** is an array where the number of different integers in that array is exactly `k`.

For example, `[1,2,3,1,2]` has `3` different integers: `1`, `2`, and `3`.

A **subarray** is a **contiguous** part of an array.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i], k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,2,1,2,3], k = 2`
- **Output:** `7`
- **Explanation:** Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

### Example 2
- **Input:** `nums = [1,2,1,3,4], k = 3`
- **Output:** `3`
- **Explanation:** Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Subarrays with K Different Integers**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,2,3], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

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
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(limit: int) -> int:
            if limit <= 0:
                return 0
            freq = [0] * (len(nums) + 1)
            distinct = count = left = 0
            
            for right, val in enumerate(nums):
                if freq[val] == 0:
                    distinct += 1
                freq[val] += 1
                
                while distinct > limit:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                    
                count += right - left + 1
            return count
            
        return at_most(k) - at_most(k - 1)
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
- [3859. Count Subarrays With K Distinct Integers](../../3501-4000/3859-count-subarrays-with-k-distinct-integers/)
- [1805. Number of Different Integers in a String](../../1501-2000/1805-number-of-different-integers-in-a-string/)
- [1481. Least Number of Unique Integers after K Removals](../../1001-1500/1481-least-number-of-unique-integers-after-k-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/)
