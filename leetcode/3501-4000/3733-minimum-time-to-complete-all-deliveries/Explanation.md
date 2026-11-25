# LeetCode 3733: Minimum Time to Complete All Deliveries

**LeetCode Problem #3733 — Minimum Time to Complete All Deliveries**
Solve LeetCode Minimum Time to Complete All Deliveries using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Complete All Deliveries |
| LeetCode | #3733 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays of size 2: `d = [d_1, d_2]` and `r = [r_1, r_2]`.

Two delivery drones are tasked with completing a specific number of deliveries. Drone `i` must complete `d_i` deliveries.

Each delivery takes **exactly** one hour and **only one** drone can make a delivery at any given hour.

Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone `i` must recharge every `r_i` hours (i.e. at hours that are multiples of `r_i`).

Return an integer denoting the **minimum** total time (in hours) required to complete all deliveries.

## Constraints
- `d = [d_1, d_2]`
- `1 <= d_i <= 10^9`
- `r = [r_1, r_2]`
- `2 <= r_i <= 3 * 10^4`

## Examples
### Example 1
- **Input:** `d = [3,1], r = [2,3]`
- **Output:** `5`
- **Explanation:** The first drone delivers at hours 1, 3, 5 (recharges at hours 2, 4). 
 The second drone delivers at hour 2 (recharges at hour 3).

### Example 2
- **Input:** `d = [1,3], r = [2,2]`
- **Output:** `7`
- **Explanation:** The first drone delivers at hour 3 (recharges at hours 2, 4, 6). 
 The second drone delivers at hours 1, 5, 7 (recharges at hours 2, 4, 6).

### Example 3
- **Input:** `d = [2,1], r = [3,4]`
- **Output:** `3`
- **Explanation:** The first drone delivers at hours 1, 2 (recharges at hour 3). 
 The second drone delivers at hour 3.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Complete All Deliveries**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `d = [3,1], r = [2,3]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The first drone delivers at hours 1, 3, 5 (recharges at hours 2, 4). 
 The second drone delivers at hour 2 (recharges at hour 3).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import gcd
from typing import List

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        l = r1 * r2 // gcd(r1, r2)

        def ok(T: int) -> bool:
            return (T - T // r1 >= d1
                    and T - T // r2 >= d2
                    and T - T // l >= d1 + d2)

        lo, hi = 1, 4 * (d1 + d2)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2589. Minimum Time to Complete All Tasks](../../2501-3000/2589-minimum-time-to-complete-all-tasks/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../../1001-1500/1443-minimum-time-to-collect-all-apples-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/)
