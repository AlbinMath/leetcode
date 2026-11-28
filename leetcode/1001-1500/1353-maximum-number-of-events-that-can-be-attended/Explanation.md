# LeetCode 1353: Maximum Number of Events That Can Be Attended

**LeetCode Problem #1353 — Maximum Number of Events That Can Be Attended**
Solve LeetCode Maximum Number of Events That Can Be Attended using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Events That Can Be Attended |
| LeetCode | #1353 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
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
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Number of Events That Can Be Attended**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `events = [[1,2],[2,3],[3,4]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
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
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1751. Maximum Number of Events That Can Be Attended II](../../1501-2000/1751-maximum-number-of-events-that-can-be-attended-ii/)
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1561-maximum-number-of-coins-you-can-get/)
- [1798. Maximum Number of Consecutive Values You Can Make](../../1501-2000/1798-maximum-number-of-consecutive-values-you-can-make/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)
