# LeetCode 3440: Reschedule Meetings for Maximum Free Time II

**LeetCode Problem #3440 — Reschedule Meetings for Maximum Free Time II**
Solve LeetCode Reschedule Meetings for Maximum Free Time II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reschedule Meetings for Maximum Free Time II |
| LeetCode | #3440 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `eventTime` denoting the duration of an event. You are also given two integer arrays `startTime` and `endTime`, each of length `n`.

These represent the start and end times of `n` **non-overlapping** meetings that occur during the event between time `t = 0` and time `t = eventTime`, where the `i^th` meeting occurs during the time `[startTime[i], endTime[i]].`

You can reschedule **at most **one meeting by moving its start time while maintaining the **same duration**, such that the meetings remain non-overlapping, to **maximize** the **longest** *continuous period of free time* during the event.

Return the **maximum** amount of free time possible after rearranging the meetings.

**Note** that the meetings can **not** be rescheduled to a time outside the event and they should remain non-overlapping.

**Note:** *In this version*, it is **valid** for the relative ordering of the meetings to change after rescheduling one meeting.

## Constraints
- `1 <= eventTime <= 10^9`
- `n == startTime.length == endTime.length`
- `2 <= n <= 10^5`
- `0 <= startTime[i] < endTime[i] <= eventTime`
- `endTime[i] <= startTime[i + 1]` where `i` lies in the range `[0, n - 2]`.

## Examples
### Example 1
- **Input:** `eventTime = 5, startTime = [1,3], endTime = [2,5]`
- **Output:** `2`
- **Explanation:** Reschedule the meeting at `[1, 2]` to `[2, 3]`, leaving no meetings during the time `[0, 2]`.

### Example 2
- **Input:** `eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]`
- **Output:** `7`
- **Explanation:** Reschedule the meeting at `[0, 1]` to `[8, 9]`, leaving no meetings during the time `[0, 7]`.

### Example 3
- **Input:** `eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]`
- **Output:** `6`

### Example 4
- **Input:** `eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]`
- **Output:** `0`
- **Explanation:** There is no time during the event not occupied by meetings.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reschedule Meetings for Maximum Free Time II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `eventTime = 5, startTime = [1,3], endTime = [2,5]`.
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
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        pre = [0] * (n + 1)
        suf = [0] * (n + 2)
        pre[0] = gaps[0]
        for i in range(1, n + 1):
            pre[i] = max(pre[i - 1], gaps[i])
        for i in range(n, -1, -1):
            suf[i] = max(suf[i + 1], gaps[i])

        ans = 0
        for i in range(n):
            d = endTime[i] - startTime[i]
            other = max(pre[i - 1] if i >= 1 else 0, suf[i + 2])
            merged = gaps[i] + gaps[i + 1]
            if other >= d:
                merged += d
            ans = max(ans, merged)
        return ans
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
- [3439. Reschedule Meetings for Maximum Free Time I](../../3501-4000/3743-reschedule-meetings-for-maximum-free-time-i/)
- [4009. Minimum Possible Maximum Waiting Time](../../4001-4500/4244-minimum-possible-maximum-waiting-time/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/)
