# LeetCode 2234: Maximum Total Beauty of the Gardens

**LeetCode Problem #2234 — Maximum Total Beauty of the Gardens**
Solve LeetCode Maximum Total Beauty of the Gardens using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total Beauty of the Gardens |
| LeetCode | #2234 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice is a caretaker of `n` gardens and she wants to plant flowers to maximize the total beauty of all her gardens.

You are given a **0-indexed** integer array `flowers` of size `n`, where `flowers[i]` is the number of flowers already planted in the `i^th` garden. Flowers that are already planted **cannot** be removed. You are then given another integer `newFlowers`, which is the **maximum** number of flowers that Alice can additionally plant. You are also given the integers `target`, `full`, and `partial`.

A garden is considered **complete** if it has **at least** `target` flowers. The **total beauty** of the gardens is then determined as the **sum** of the following:

The number of **complete** gardens multiplied by `full`. 
 The **minimum** number of flowers in any of the **incomplete** gardens multiplied by `partial`. If there are no incomplete gardens, then this value will be `0`.

Return *the **maximum** total beauty that Alice can obtain after planting at most *`newFlowers`* flowers.*

## Constraints
- `1 <= flowers.length <= 10^5`
- `1 <= flowers[i], target <= 10^5`
- `1 <= newFlowers <= 10^10`
- `1 <= full, partial <= 10^5`

## Examples
### Example 1
- **Input:** `flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1`
- **Output:** `14`
- **Explanation:** Alice can plant
- 2 flowers in the 0^th garden
- 3 flowers in the 1^st garden
- 1 flower in the 2^nd garden
- 1 flower in the 3^rd garden
The gardens will then be [3,6,2,2]. She planted a total of 2 + 3 + 1 + 1 = 7 flowers.
There is 1 garden that is complete.
The minimum number of flowers in the incomplete gardens is 2.
Thus, the total beauty is 1 * 12 + 2 * 1 = 12 + 2 = 14.
No other way of planting flowers can obtain a total beauty higher than 14.

### Example 2
- **Input:** `flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6`
- **Output:** `30`
- **Explanation:** Alice can plant
- 3 flowers in the 0^th garden
- 0 flowers in the 1^st garden
- 0 flowers in the 2^nd garden
- 2 flowers in the 3^rd garden
The gardens will then be [5,4,5,5]. She planted a total of 3 + 0 + 0 + 2 = 5 flowers.
There are 3 gardens that are complete.
The minimum number of flowers in the incomplete gardens is 4.
Thus, the total beauty is 3 * 2 + 4 * 6 = 6 + 24 = 30.
No other way of planting flowers can obtain a total beauty higher than 30.
Note that Alice could make all the gardens complete but in this case, she would obtain a lower total beauty.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Total Beauty of the Gardens**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** Alice can plant
- 2 flowers in the 0^th garden
- 3 flowers in the 1^st garden
- 1 flower in the 2^nd garden
- 1 flower in the 3^rd garden
The gardens will then be [3,6,2,2]. She planted a total of 2 + 3 + 1 + 1 = 7 flowers.
There is 1 garden that is complete.
The minimum number of flowers in the incomplete gardens is 2.
Thus, the total beauty is 1 * 12 + 2 * 1 = 12 + 2 = 14.
No other way of planting flowers can obtain a total beauty higher than 14.

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
class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        flowers = sorted(min(f, target) for f in flowers)
        n = len(flowers)

        # Gardens already complete don't need any new flowers
        already_full = 0
        while flowers and flowers[-1] == target:
            flowers.pop()
            already_full += 1

        m = len(flowers)
        if m == 0:
            return n * full

        # cost[i] = flowers needed to raise flowers[0..i] all up to flowers[i]
        cost = [0] * m
        for i in range(1, m):
            cost[i] = cost[i - 1] + i * (flowers[i] - flowers[i - 1])

        ans = 0
        rem = newFlowers
        j = m - 1

        # Try completing the k largest incomplete gardens (from right to left)
        for k in range(m + 1):
            if k > 0:
                rem -= target - flowers[m - k]
                if rem < 0:
                    break

            if k == m:
                ans = max(ans, (already_full + m) * full)
                break

            while j >= m - k or cost[j] > rem:
                j -= 1

            min_incomplete = min(target - 1, flowers[j] + (rem - cost[j]) // (j + 1))
            ans = max(ans, (already_full + k) * full + min_incomplete * partial)

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
- [2285. Maximum Total Importance of Roads](../../2001-2500/2285-maximum-total-importance-of-roads/)
- [3180. Maximum Total Reward Using Operations I](../../3001-3500/3180-maximum-total-reward-using-operations-i/)
- [3181. Maximum Total Reward Using Operations II](../../3001-3500/3181-maximum-total-reward-using-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/)
