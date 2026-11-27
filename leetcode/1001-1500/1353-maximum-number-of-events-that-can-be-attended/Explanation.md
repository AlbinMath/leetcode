# LeetCode 1353: Maximum Number of Events That Can Be Attended

**LeetCode Problem #1353 — Maximum Number of Events That Can Be Attended**
Solve LeetCode Maximum Number of Events That Can Be Attended using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Events That Can Be Attended |
| LeetCode | #1353 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of `events` where `events[i] = [startDay_i, endDay_i]`. Every event `i` starts at `startDay_i`_ and ends at `endDay_i`.

You can attend an event `i` at any day `d` where `startDay_i <= d <= endDay_i`. You can only attend one event at any time `d`.

Return *the maximum number of events you can attend*.

## Constraints
- `1 <= events.length <= 10^5`
- `events[i].length == 2`
- `1 <= startDay_i <= endDay_i <= 10^5`

## Examples
### Example 1
- **Input:** `events = [[1,2],[2,3],[3,4]]`
- **Output:** `3`
- **Explanation:** You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

### Example 2
- **Input:** `events= [[1,2],[2,3],[3,4],[1,2]]`
- **Output:** `4`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Events That Can Be Attended**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `events = [[1,2],[2,3],[3,4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

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
import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        heap = []  # end days of events available today
        i = 0
        day = 0
        count = 0
        while i < n or heap:
            if not heap:
                day = max(day, events[i][0])  # skip idle days
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)  # expired
            if heap:
                heapq.heappop(heap)  # attend the earliest-ending event
                count += 1
            day += 1
        return count
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
- [1751. Maximum Number of Events That Can Be Attended II](../../1501-2000/1751-maximum-number-of-events-that-can-be-attended-ii/)
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1160-find-words-that-can-be-formed-by-characters/)
- [2201. Count Artifacts That Can Be Extracted](../../2001-2500/2201-count-artifacts-that-can-be-extracted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)
