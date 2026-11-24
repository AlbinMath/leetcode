# LeetCode 3439: Reschedule Meetings for Maximum Free Time I

**LeetCode Problem #3439 — Reschedule Meetings for Maximum Free Time I**
Solve LeetCode Reschedule Meetings for Maximum Free Time I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reschedule Meetings for Maximum Free Time I |
| LeetCode | #3439 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `eventTime` denoting the duration of an event, where the event occurs from time `t = 0` to time `t = eventTime`.

You are also given two integer arrays `startTime` and `endTime`, each of length `n`. These represent the start and end time of `n` **non-overlapping** meetings, where the `i^th` meeting occurs during the time `[startTime[i], endTime[i]]`.

You can reschedule **at most** `k` meetings by moving their start time while maintaining the **same duration**, to **maximize** the **longest** *continuous period of free time* during the event.

The **relative** order of all the meetings should stay the* same* and they should remain non-overlapping.

Return the **maximum** amount of free time possible after rearranging the meetings.

**Note** that the meetings can **not** be rescheduled to a time outside the event.

## Constraints
- `1 <= eventTime <= 10^9`
- `n == startTime.length == endTime.length`
- `2 <= n <= 10^5`
- `1 <= k <= n`
- `0 <= startTime[i] < endTime[i] <= eventTime`
- `endTime[i] <= startTime[i + 1]` where `i` lies in the range `[0, n - 2]`.

## Examples
### Example 1
- **Input:** `eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]`
- **Output:** `2`
- **Explanation:** Reschedule the meeting at `[1, 2]` to `[2, 3]`, leaving no meetings during the time `[0, 2]`.

### Example 2
- **Input:** `eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]`
- **Output:** `6`
- **Explanation:** Reschedule the meeting at `[2, 4]` to `[1, 3]`, leaving no meetings during the time `[3, 9]`.

### Example 3
- **Input:** `eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]`
- **Output:** `0`
- **Explanation:** There is no time during the event not occupied by meetings.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reschedule Meetings for Maximum Free Time I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Reschedule the meeting at `[1, 2]` to `[2, 3]`, leaving no meetings during the time `[0, 2]`.

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
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        w = k + 1
        cur = sum(gaps[:w])
        best = cur
        for i in range(w, len(gaps)):
            cur += gaps[i] - gaps[i - w]
            best = max(best, cur)
        return best
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
- [3440. Reschedule Meetings for Maximum Free Time II](../../3001-3500/3440-reschedule-meetings-for-maximum-free-time-ii/)
- [2141. Maximum Running Time of N Computers](../../2001-2500/2141-maximum-running-time-of-n-computers/)
- [4009. Minimum Possible Maximum Waiting Time](../../4001-4500/4009-minimum-possible-maximum-waiting-time/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/)
