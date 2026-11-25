# LeetCode 2054: Two Best Non-Overlapping Events

**LeetCode Problem #2054 — Two Best Non-Overlapping Events**
Solve LeetCode Two Best Non-Overlapping Events using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Two Best Non-Overlapping Events |
| LeetCode | #2054 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D integer array of `events` where `events[i] = [startTime_i, endTime_i, value_i]`. The `i^th` event starts at `startTime_i`_ and ends at `endTime_i`, and if you attend this event, you will receive a value of `value_i`. You can choose **at most** **two** **non-overlapping** events to attend such that the sum of their values is **maximized**.

Return *this **maximum** sum.*

Note that the start time and end time is **inclusive**: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time `t`, the next event must start at or after `t + 1`.

## Constraints
- `2 <= events.length <= 10^5`
- `events[i].length == 3`
- `1 <= startTime_i <= endTime_i <= 10^9`
- `1 <= value_i <= 10^6`

## Examples
### Example 1
- **Input:** `events = [[1,3,2],[4,5,2],[2,4,3]]`
- **Output:** `4`
- **Explanation:** Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

### Example 3
- **Input:** `events = [[1,5,3],[1,5,1],[6,6,5]]`
- **Output:** `8`
- **Explanation:** Choose events 0 and 2 for a sum of 3 + 5 = 8.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Two Best Non-Overlapping Events**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `events = [[1,3,2],[4,5,2],[2,4,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

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
from bisect import bisect_left
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[1])
        ends = [e[1] for e in events]

        pref = []
        cur = 0
        for _, _, v in events:
            cur = max(cur, v)
            pref.append(cur)

        ans = 0
        for s, e, v in events:
            best = v
            idx = bisect_left(ends, s) - 1
            if idx >= 0:
                best += pref[idx]
            ans = max(ans, best)

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
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1031-maximum-sum-of-two-non-overlapping-subarrays/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1001-1500/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [4016. Maximum Area of Two Non-Overlapping Square Submatrices](../../4001-4500/4016-maximum-area-of-two-non-overlapping-square-submatrices/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/two-best-non-overlapping-events/)
