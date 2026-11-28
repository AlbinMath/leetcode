# LeetCode 3661: Maximum Walls Destroyed by Robots

**LeetCode Problem #3661 — Maximum Walls Destroyed by Robots**
Solve LeetCode Maximum Walls Destroyed by Robots using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Walls Destroyed by Robots |
| LeetCode | #3661 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an endless straight line populated with some robots and walls. You are given integer arrays `robots`, `distance`, and `walls`:

`robots[i]` is the position of the `i^th` robot. 
 `distance[i]` is the **maximum** distance the `i^th` robot's bullet can travel. 
 `walls[j]` is the position of the `j^th` wall.

Every robot has **one** bullet that can either fire to the left or the right **at most **`distance[i]` meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it **immediately stops** at that robot and cannot continue.

Return the **maximum** number of **unique** walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position. 
 Robots are not destroyed by bullets.

## Constraints
- `1 <= robots.length == distance.length <= 10^5`
- `1 <= walls.length <= 10^5`
- `1 <= robots[i], walls[j] <= 10^9`
- `1 <= distance[i] <= 10^5`
- All values in `robots` are **unique**
- All values in `walls` are **unique**

## Examples
### Example 1
- **Input:** `robots = [4], distance = [3], walls = [1,10]`
- **Output:** `1`
- **Explanation:** `robots[0] = 4` fires

### Example 2
- **Input:** `robots = [10,2], distance = [5,1], walls = [5,2,7]`
- **Output:** `3`
- **Explanation:** `robots[0] = 10` fires

### Example 3
- **Input:** `robots = [1,2], distance = [100,1], walls = [10]`
- **Output:** `0`
- **Explanation:** In this example, only `robots[0]` can reach the wall, but its shot to the

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Walls Destroyed by Robots**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `robots = [4], distance = [3], walls = [1,10]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** `robots[0] = 4` fires

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
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        rs = sorted(zip(robots, distance))
        n = len(rs)
        INF = float('inf')

        def cnt(l, r):
            if l > r:
                return 0
            return bisect_right(walls, r) - bisect_left(walls, l)

        def left(i):
            p, d = rs[i]
            lo = p - d
            if i > 0:
                lo = max(lo, rs[i - 1][0] + 1)
            return lo, p

        def right(i):
            p, d = rs[i]
            hi = p + d
            if i < n - 1:
                hi = min(hi, rs[i + 1][0] - 1)
            return p, hi

        l0, r0 = left(0)
        a, b = right(0)
        dpL, dpR = cnt(l0, r0), cnt(a, b)

        for i in range(1, n):
            ll, lr = left(i)
            rl, rr = right(i)
            pl, pr = right(i - 1)
            overlap = cnt(max(pl, ll), min(pr, lr))
            newL = cnt(ll, lr) + max(dpL, dpR - overlap)
            newR = cnt(rl, rr) + max(dpL, dpR)
            dpL, dpR = newL, newR

        return max(dpL, dpR)
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
- [2398. Maximum Number of Robots Within Budget](../../2001-2500/2398-maximum-number-of-robots-within-budget/)
- [2731. Movement of Robots](../../2501-3000/2731-movement-of-robots/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-walls-destroyed-by-robots/)
