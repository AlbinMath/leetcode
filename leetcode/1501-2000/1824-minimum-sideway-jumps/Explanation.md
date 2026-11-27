# LeetCode 1824: Minimum Sideway Jumps

**LeetCode Problem #1824 — Minimum Sideway Jumps**
Solve LeetCode Minimum Sideway Jumps using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Sideway Jumps |
| LeetCode | #1824 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a **3 lane road** of length `n` that consists of `n + 1` **points** labeled from `0` to `n`. A frog **starts** at point `0` in the **second **lane** **and wants to jump to point `n`. However, there could be obstacles along the way.

You are given an array `obstacles` of length `n + 1` where each `obstacles[i]` (**ranging from 0 to 3**) describes an obstacle on the lane `obstacles[i]` at point `i`. If `obstacles[i] == 0`, there are no obstacles at point `i`. There will be **at most one** obstacle in the 3 lanes at each point.

For example, if `obstacles[2] == 1`, then there is an obstacle on lane 1 at point 2.

The frog can only travel from point `i` to point `i + 1` on the same lane if there is not an obstacle on the lane at point `i + 1`. To avoid obstacles, the frog can also perform a **side jump** to jump to **another** lane (even if they are not adjacent) at the **same** point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.

Return* the **minimum number of side jumps** the frog needs to reach **any lane** at point n starting from lane `2` at point 0.*

**Note:** There will be no obstacles on points `0` and `n`.

## Constraints
- `obstacles.length == n + 1`
- `1 <= n <= 5 * 10^5`
- `0 <= obstacles[i] <= 3`
- `obstacles[0] == obstacles[n] == 0`

## Examples
### Example 1
- **Input:** `obstacles = [0,1,2,3,0]`
- **Output:** `2`
- **Explanation:** The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).

### Example 2
- **Input:** `obstacles = [0,1,1,3,3,0]`
- **Output:** `0`
- **Explanation:** There are no obstacles on lane 2. No side jumps are required.

### Example 3
- **Input:** `obstacles = [0,2,1,0,3,0]`
- **Output:** `2`
- **Explanation:** The optimal solution is shown by the arrows above. There are 2 side jumps.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Sideway Jumps**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `obstacles = [0,1,2,3,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = float('inf')
        dp = [1, 0, 1]
        for i in range(1, len(obstacles)):
            o = obstacles[i]
            if o:
                dp[o - 1] = INF
            best = min(dp)
            for l in range(3):
                if l != o - 1:
                    dp[l] = min(dp[l], best + 1)
        return min(dp)
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1654. Minimum Jumps to Reach Home](../../1501-2000/1654-minimum-jumps-to-reach-home/)
- [3629. Minimum Jumps to Reach End via Prime Teleportation](../../3501-4000/3629-minimum-jumps-to-reach-end-via-prime-teleportation/)
- [2770. Maximum Number of Jumps to Reach the Last Index](../../2501-3000/2770-maximum-number-of-jumps-to-reach-the-last-index/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-sideway-jumps/)
