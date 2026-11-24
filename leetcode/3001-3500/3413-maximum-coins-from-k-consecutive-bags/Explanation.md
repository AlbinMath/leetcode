# LeetCode 3413: Maximum Coins From K Consecutive Bags

**LeetCode Problem #3413 — Maximum Coins From K Consecutive Bags**
Solve LeetCode Maximum Coins From K Consecutive Bags using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Coins From K Consecutive Bags |
| LeetCode | #3413 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are an infinite amount of bags on a number line, one bag for each coordinate. Some of these bags contain coins.

You are given a 2D array `coins`, where `coins[i] = [l_i, r_i, c_i]` denotes that every bag from `l_i` to `r_i` contains `c_i` coins.

The segments that `coins` contain are non-overlapping.

You are also given an integer `k`.

Return the **maximum** amount of coins you can obtain by collecting `k` consecutive bags.

## Constraints
- `1 <= coins.length <= 10^5`
- `1 <= k <= 10^9`
- `coins[i] == [l_i, r_i, c_i]`
- `1 <= l_i <= r_i <= 10^9`
- `1 <= c_i <= 1000`
- The given segments are non-overlapping.

## Examples
### Example 1
- **Input:** `coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4`
- **Output:** `10`
- **Explanation:** Selecting bags at positions `[3, 4, 5, 6]` gives the maximum number of coins: `2 + 0 + 4 + 4 = 10`.

### Example 2
- **Input:** `coins = [[1,10,3]], k = 2`
- **Output:** `6`
- **Explanation:** Selecting bags at positions `[1, 2]` gives the maximum number of coins: `3 + 3 = 6`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Coins From K Consecutive Bags**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** Selecting bags at positions `[3, 4, 5, 6]` gives the maximum number of coins: `2 + 0 + 4 + 4 = 10`.

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
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def solve(segs):
            segs.sort()
            n = len(segs)
            P = [0] * (n + 1)
            for i, (l, r, c) in enumerate(segs):
                P[i + 1] = P[i] + (r - l + 1) * c
            best = 0
            j = 0
            for i in range(n):
                s = segs[i][0]
                e = s + k - 1
                if j < i:
                    j = i
                while j < n and segs[j][1] <= e:
                    j += 1
                total = P[j] - P[i]
                if j < n and segs[j][0] <= e:
                    total += (e - segs[j][0] + 1) * segs[j][2]
                best = max(best, total)
            return best

        a = solve([[l, r, c] for l, r, c in coins])
        b = solve([[-r, -l, c] for l, r, c in coins])
        return max(a, b)
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
- [2920. Maximum Points After Collecting Coins From All Nodes](../../2501-3000/2920-maximum-points-after-collecting-coins-from-all-nodes/)
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1561-maximum-number-of-coins-you-can-get/)
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1191-k-concatenation-maximum-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/)
