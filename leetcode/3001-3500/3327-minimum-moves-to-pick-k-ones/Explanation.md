# LeetCode 3086: Minimum Moves to Pick K Ones

**LeetCode Problem #3086 — Minimum Moves to Pick K Ones**
Solve LeetCode Minimum Moves to Pick K Ones using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Pick K Ones |
| LeetCode | #3086 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary array `nums` of length `n`, a **positive** integer `k` and a **non-negative** integer `maxChanges`.

Alice plays a game, where the goal is for Alice to pick up `k` ones from `nums` using the **minimum** number of **moves**. When the game starts, Alice picks up any index `aliceIndex` in the range `[0, n - 1]` and stands there. If `nums[aliceIndex] == 1` , Alice picks up the one and `nums[aliceIndex]` becomes `0`(this **does not** count as a move). After this, Alice can make **any** number of **moves** (**including** **zero**) where in each move Alice must perform **exactly** one of the following actions:

Select any index `j != aliceIndex` such that `nums[j] == 0` and set `nums[j] = 1`. This action can be performed **at** **most** `maxChanges` times. 
 Select any two adjacent indices `x` and `y` (`|x - y| == 1`) such that `nums[x] == 1`, `nums[y] == 0`, then swap their values (set `nums[y] = 1` and `nums[x] = 0`). If `y == aliceIndex`, Alice picks up the one after this move and `nums[y]` becomes `0`.

Return *the **minimum** number of moves required by Alice to pick **exactly ***`k` *ones*.

## Constraints
- `2 <= n <= 10^5`
- `0 <= nums[i] <= 1`
- `1 <= k <= 10^5`
- `0 <= maxChanges <= 10^5`
- `maxChanges + sum(nums) >= k`

## Examples
### Example 1
- **Input:** `nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1`
- **Output:** `3`
- **Explanation:** Alice can pick up `3` ones in `3` moves, if Alice performs the following actions in each move when standing at `aliceIndex == 1`: 

 
 At the start of the game Alice picks up the one and `nums[1]` becomes `0`. `nums` becomes [1,

### Example 2
- **Input:** `nums = [0,0,0,0], k = 2, maxChanges = 3`
- **Output:** `4`
- **Explanation:** Alice can pick up `2` ones in `4` moves, if Alice performs the following actions in each move when standing at `aliceIndex == 0`: 

 
 Select `j == 1` and perform an action of the first type. `nums` becomes [

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Moves to Pick K Ones**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Alice can pick up `3` ones in `3` moves, if Alice performs the following actions in each move when standing at `aliceIndex == 1`: 

 
 At the start of the game Alice picks up the one and `nums[1]` becomes `0`. `nums` becomes [1,

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
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        n = len(nums)
        best = float('inf')
        for i in range(n):
            a = nums[i]
            b = (nums[i - 1] if i > 0 else 0) + (nums[i + 1] if i + 1 < n else 0)
            t = min(k, a + b)
            r = k - t
            if r <= maxChanges:
                best = min(best, (t - a) + 2 * r)
        pos = [i for i, v in enumerate(nums) if v]
        m = len(pos)
        need = k - maxChanges
        if 1 <= need <= m:
            P = [0] * (m + 1)
            for i, p in enumerate(pos):
                P[i + 1] = P[i] + p
            cost2 = float('inf')
            for l in range(m - need + 1):
                r = l + need - 1
                mid = l + need // 2
                left = pos[mid] * (mid - l) - (P[mid] - P[l])
                right = (P[r + 1] - P[mid + 1]) - pos[mid] * (r - mid)
                cost2 = min(cost2, left + right)
            best = min(best, cost2 + 2 * maxChanges)

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
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1805-minimum-adjacent-swaps-for-k-consecutive-ones/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-pick-k-ones/)
