# LeetCode 4045: Count Robot Groups

**LeetCode Problem #4045 — Count Robot Groups**
Solve LeetCode Count Robot Groups using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Robot Groups |
| LeetCode | #4045 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a strictly increasing integer array `position`, where `position[i]` is the initial position of the `i^th` robot at time `t = 0`.

You are also given an integer array `speed`, where `speed[i]` is the constant speed of the `i^th` robot in units per second, and an integer `distance`.

Time is **continuous** and measured in seconds. A robot or group with speed `v` moves `v * t` units to the right over any interval of `t` seconds.

Whenever the distance between two robots or groups becomes at most `distance`, they merge into a single group.

If multiple robots or groups satisfy the merging condition at the same time, all merges happen **simultaneously**. In particular, every connected collection of robots or groups whose consecutive positions differ by at most `distance` merges into one group.

After a merge, the resulting group takes the current position and speed of the **rightmost robot** in that group. Once merged, robots never separate.

Return the number of groups remaining after all possible merges have occurred.

## Constraints
- `1 <= position.length == speed.length <= 10^5`
- `1 <= position[i], speed[i], distance <= 10^9`
- `position` is strictly increasing.

## Examples
### Example 1
- **Input:** `position = [1,5,6,20], speed = [4,3,2,3], distance = 1`
- **Output:** `2`

### Example 2
- **Input:** `position = [1,5,9], speed = [3,2,2], distance = 2`
- **Output:** `2`

### Example 3
- **Input:** `position = [9], speed = [8], distance = 5`
- **Output:** `1`
- **Explanation:** Initially, there is only one group. Therefore, the answer is 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Robot Groups**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `position = [1,5,6,20], speed = [4,3,2,3], distance = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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
    def countGroups(self, position: List[int], speed: List[int], distance: int) -> int:
        n = len(position)
        d = distance
        T = [None] * n          # (num, den) or None for infinity
        stack = []
        groups = 0

        for i in range(n - 1, -1, -1):
            p, s = position[i], speed[i]
            res = None
            while stack:
                j = stack[-1]
                g = position[j] - p
                if g <= d:
                    t = (0, 1)
                elif s > speed[j]:
                    t = (g - d, s - speed[j])
                else:
                    stack.pop()          # can never catch j
                    continue
                tj = T[j]
                if tj is None or t[0] * tj[1] <= tj[0] * t[1]:
                    res = t
                    break
                stack.pop()              # j is absorbed before i reaches it
            T[i] = res
            if res is None:
                groups += 1
            stack.append(i)

        return groups
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
- [657. Robot Return to Origin](../../0501-1000/0657-robot-return-to-origin/)
- [874. Walking Robot Simulation](../../0501-1000/0874-walking-robot-simulation/)
- [1041. Robot Bounded In Circle](../../1001-1500/1041-robot-bounded-in-circle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-robot-groups/)
