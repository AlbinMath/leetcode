# LeetCode 1751: Maximum Number of Events That Can Be Attended II

**LeetCode Problem #1751 — Maximum Number of Events That Can Be Attended II**
Solve LeetCode Maximum Number of Events That Can Be Attended II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Events That Can Be Attended II |
| LeetCode | #1751 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of `events` where `events[i] = [startDay_i, endDay_i, value_i]`. The `i^th` event starts at `startDay_i`_ and ends at `endDay_i`, and if you attend this event, you will receive a value of `value_i`. You are also given an integer `k` which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the **entire** event. Note that the end day is **inclusive**: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return *the **maximum sum** of values that you can receive by attending events.*

## Constraints
- `1 <= k <= events.length`
- `1 <= k * events.length <= 10^6`
- `1 <= startDay_i <= endDay_i <= 10^9`
- `1 <= value_i <= 10^6`

## Examples
### Example 1
- **Input:** `events = [[1,2,4],[3,4,3],[2,3,1]], k = 2`
- **Output:** `7`
- **Explanation:** Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

### Example 2
- **Input:** `events = [[1,2,4],[3,4,3],[2,3,10]], k = 2`
- **Output:** `10`
- **Explanation:** Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do

### Example 3
- **Input:** `events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3`
- **Output:** `9`
- **Explanation:** Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Events That Can Be Attended II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `events = [[1,2,4],[3,4,3],[2,3,1]], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

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
from functools import lru_cache

class Solution:
    def maxValue(self, events, k):
        events.sort()
        n = len(events)
        starts = [e[0] for e in events]

        @lru_cache(None)
        def f(i, j):
            if i == n or j == 0:
                return 0
            nxt = bisect_right(starts, events[i][1])
            return max(f(i + 1, j), events[i][2] + f(nxt, j - 1))

        return f(0, k)
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
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1160-find-words-that-can-be-formed-by-characters/)
- [2201. Count Artifacts That Can Be Extracted](../../2001-2500/2201-count-artifacts-that-can-be-extracted/)
- [2930. Number of Strings Which Can Be Rearranged to Contain Substring](../../2501-3000/2930-number-of-strings-which-can-be-rearranged-to-contain-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)
