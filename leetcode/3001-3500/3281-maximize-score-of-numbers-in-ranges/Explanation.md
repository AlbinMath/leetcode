# LeetCode 3281: Maximize Score of Numbers in Ranges

**LeetCode Problem #3281 — Maximize Score of Numbers in Ranges**
Solve LeetCode Maximize Score of Numbers in Ranges using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Score of Numbers in Ranges |
| LeetCode | #3281 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `start` and an integer `d`, representing `n` intervals `[start[i], start[i] + d]`.

You are asked to choose `n` integers where the `i^th` integer must belong to the `i^th` interval. The **score** of the chosen integers is defined as the **minimum** absolute difference between any two integers that have been chosen.

Return the **maximum** *possible score* of the chosen integers.

## Constraints
- `2 <= start.length <= 10^5`
- `0 <= start[i] <= 10^9`
- `0 <= d <= 10^9`

## Examples
### Example 1
- **Input:** `start = [6,0,3], d = 2`
- **Output:** `4`
- **Explanation:** The maximum possible score can be obtained by choosing integers: 8, 0, and 4. The score of these chosen integers is `min(|8 - 0|, |8 - 4|, |0 - 4|)` which equals 4.

### Example 2
- **Input:** `start = [2,6,13,13], d = 5`
- **Output:** `5`
- **Explanation:** The maximum possible score can be obtained by choosing integers: 2, 7, 13, and 18. The score of these chosen integers is `min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|)` which equals 5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize Score of Numbers in Ranges**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `start = [6,0,3], d = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The maximum possible score can be obtained by choosing integers: 8, 0, and 4. The score of these chosen integers is `min(|8 - 0|, |8 - 4|, |0 - 4|)` which equals 4.

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
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)

        def ok(g: int) -> bool:
            cur = start[0]
            for i in range(1, n):
                cur = max(start[i], cur + g)
                if cur > start[i] + d:
                    return False
            return True

        lo, hi = 0, (start[-1] + d - start[0]) // (n - 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
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
- [1799. Maximize Score After N Operations](../../1501-2000/1799-maximize-score-after-n-operations/)
- [2587. Rearrange Array to Maximize Prefix Score](../../2501-3000/2587-rearrange-array-to-maximize-prefix-score/)
- [2818. Apply Operations to Maximize Score](../../2501-3000/2818-apply-operations-to-maximize-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/)
