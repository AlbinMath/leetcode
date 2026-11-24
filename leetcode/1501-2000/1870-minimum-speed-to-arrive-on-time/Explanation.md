# LeetCode 1870: Minimum Speed to Arrive on Time

**LeetCode Problem #1870 — Minimum Speed to Arrive on Time**
Solve LeetCode Minimum Speed to Arrive on Time using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Speed to Arrive on Time |
| LeetCode | #1870 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a floating-point number `hour`, representing the amount of time you have to reach the office. To commute to the office, you must take `n` trains in sequential order. You are also given an integer array `dist` of length `n`, where `dist[i]` describes the distance (in kilometers) of the `i^th` train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the `1^st` train ride takes `1.5` hours, you must wait for an additional `0.5` hours before you can depart on the `2^nd` train ride at the 2 hour mark.

Return *the **minimum positive integer** speed **(in kilometers per hour)** that all the trains must travel at for you to reach the office on time, or *`-1`* if it is impossible to be on time*.

Tests are generated such that the answer will not exceed `10^7` and `hour` will have **at most two digits after the decimal point**.

## Constraints
- `n == dist.length`
- `1 <= n <= 10^5`
- `1 <= dist[i] <= 10^5`
- `1 <= hour <= 10^9`
- There will be at most two digits after the decimal point in `hour`.

## Examples
### Example 1
- **Input:** `dist = [1,3,2], hour = 6`
- **Output:** `1`
- **Explanation:** At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

### Example 2
- **Input:** `dist = [1,3,2], hour = 2.7`
- **Output:** `3`
- **Explanation:** At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.

### Example 3
- **Input:** `dist = [1,3,2], hour = 1.9`
- **Output:** `-1`
- **Explanation:** It is impossible because the earliest the third train can depart is at the 2 hour mark.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Speed to Arrive on Time**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `dist = [1,3,2], hour = 6`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

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
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        H = round(hour * 100)

        if H <= 100 * (n - 1):
            return -1

        def ok(v: int) -> bool:
            t = 0
            for d in dist[:-1]:
                t += (d + v - 1) // v          # whole hours
            t *= 100
            t += (100 * dist[-1] + v - 1) // v  # last ride, in hundredths, rounded up
            return t <= H

        lo, hi = 1, 10**7
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
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
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../../1001-1500/1443-minimum-time-to-collect-all-apples-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/)
