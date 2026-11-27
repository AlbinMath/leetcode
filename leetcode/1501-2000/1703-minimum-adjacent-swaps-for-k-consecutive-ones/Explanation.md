# LeetCode 1703: Minimum Adjacent Swaps for K Consecutive Ones

**LeetCode Problem #1703 — Minimum Adjacent Swaps for K Consecutive Ones**
Solve LeetCode Minimum Adjacent Swaps for K Consecutive Ones using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Adjacent Swaps for K Consecutive Ones |
| LeetCode | #1703 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array, `nums`, and an integer `k`. `nums` comprises of only `0`'s and `1`'s. In one move, you can choose two **adjacent** indices and swap their values.

Return *the **minimum** number of moves required so that *`nums`* has *`k`* **consecutive** *`1`*'s*.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is `0` or `1`.
- `1 <= k <= sum(nums)`

## Examples
### Example 1
- **Input:** `nums = [1,0,0,1,0,1], k = 2`
- **Output:** `1`
- **Explanation:** In 1 move, nums could be [1,0,0,0, 1 , 1 ] and have 2 consecutive 1's.

### Example 2
- **Input:** `nums = [1,0,0,0,0,0,1,1], k = 3`
- **Output:** `5`
- **Explanation:** In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0, 1 , 1 , 1 ].

### Example 3
- **Input:** `nums = [1,1,0,1], k = 2`
- **Output:** `0`
- **Explanation:** nums already has 2 consecutive 1's.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Adjacent Swaps for K Consecutive Ones**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,0,1,0,1], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** In 1 move, nums could be [1,0,0,0, 1 , 1 ] and have 2 consecutive 1's.

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
    def minMoves(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
            
        g = [i - r for r, i in enumerate(idx for idx, val in enumerate(nums) if val == 1)]
        m = len(g)
        
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = pref[i] + g[i]
            
        min_swaps = float('inf')
        for i in range(m - k + 1):
            mid = i + k // 2
            median_val = g[mid]
            left_cost = median_val * (mid - i) - (pref[mid] - pref[i])
            right_cost = (pref[i + k] - pref[mid + 1]) - median_val * (i + k - 1 - mid)
            if left_cost + right_cost < min_swaps:
                min_swaps = left_cost + right_cost
                
        return min_swaps
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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [2379. Minimum Recolors to Get K Consecutive Black Blocks](../../2001-2500/2379-minimum-recolors-to-get-k-consecutive-black-blocks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/)
