# LeetCode 2187: Minimum Time to Complete Trips

**LeetCode Problem #2187 — Minimum Time to Complete Trips**
Solve LeetCode Minimum Time to Complete Trips using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Complete Trips |
| LeetCode | #2187 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `time` where `time[i]` denotes the time taken by the `i^th` bus to complete **one trip**.

Each bus can make multiple trips **successively**; that is, the next trip can start **immediately after** completing the current trip. Also, each bus operates **independently**; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer `totalTrips`, which denotes the number of trips all buses should make **in total**. Return *the **minimum time** required for all buses to complete **at least** *`totalTrips`* trips*.

## Constraints
- `1 <= time.length <= 10^5`
- `1 <= time[i], totalTrips <= 10^7`

## Examples
### Example 1
- **Input:** `time = [1,2,3], totalTrips = 5`
- **Output:** `3`
- **Explanation:** - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
 The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
 The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
 The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

### Example 2
- **Input:** `time = [2], totalTrips = 1`
- **Output:** `2`
- **Explanation:** There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Complete Trips**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `time = [1,2,3], totalTrips = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
 The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
 The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
 The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

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
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, min(time) * totalTrips

        while lo < hi:
            mid = (lo + hi) // 2
            if sum(mid // x for x in time) >= totalTrips:
                hi = mid
            else:
                lo = mid + 1

        return lo
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
- [2589. Minimum Time to Complete All Tasks](../../2501-3000/2589-minimum-time-to-complete-all-tasks/)
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-complete-trips/)
