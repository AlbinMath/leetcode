# LeetCode 2532: Time to Cross a Bridge

**LeetCode Problem #2532 — Time to Cross a Bridge**
Solve LeetCode Time to Cross a Bridge using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Time to Cross a Bridge |
| LeetCode | #2532 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `k` workers who want to move `n` boxes from the right (old) warehouse to the left (new) warehouse. You are given the two integers `n` and `k`, and a 2D integer array `time` of size `k x 4` where `time[i] = [right_i, pick_i, left_i, put_i]`.

The warehouses are separated by a river and connected by a bridge. Initially, all `k` workers are waiting on the left side of the bridge. To move the boxes, the `i^th` worker can do the following:

Cross the bridge to the right side in `right_i` minutes. 
 Pick a box from the right warehouse in `pick_i` minutes. 
 Cross the bridge to the left side in `left_i` minutes. 
 Put the box into the left warehouse in `put_i` minutes.

The `i^th` worker is **less efficient** than the j`^th` worker if either condition is met:

`left_i + right_i > left_j + right_j` 
 `left_i + right_i == left_j + right_j` and `i > j`

The following rules regulate the movement of the workers through the bridge:

Only one worker can use the bridge at a time. 
 When the bridge is unused prioritize the **least efficient** worker (who have picked up the box) on the right side to cross. If not, prioritize the **least efficient** worker on the left side to cross. 
 If enough workers have already been dispatched from the left side to pick up all the remaining boxes, **no more** workers will be sent from the left side.

Return the **elapsed minutes** at which the last box reaches the **left side of the bridge**.

## Constraints
- `1 <= n, k <= 10^4`
- `time.length == k`
- `time[i].length == 4`
- `1 <= left_i, pick_i, right_i, put_i <= 1000`

## Examples
### Example 1
- **Input:** `n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]`
- **Output:** `6`
- **Explanation:** From 0 to 1 minutes: worker 2 crosses the bridge to the right.
From 1 to 2 minutes: worker 2 picks up a box from the right warehouse.
From 2 to 6 minutes: worker 2 crosses the bridge to the left.
From 6 to 7 minutes: worker 2 puts a box at the left warehouse.
The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left side of the bridge.

### Example 2
- **Input:** `n = 3, k = 2, time = [[1,5,1,8],[10,10,10,10]]`
- **Output:** `37`
- **Explanation:** The last box reaches the left side at 37 seconds. Notice, how we

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Time to Cross a Bridge**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** From 0 to 1 minutes: worker 2 crosses the bridge to the right.
From 1 to 2 minutes: worker 2 picks up a box from the right warehouse.
From 2 to 6 minutes: worker 2 crosses the bridge to the left.
From 6 to 7 minutes: worker 2 puts a box at the left warehouse.
The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left side of the bridge.

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
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # Max-heaps (via negative values) ordered by least efficiency: (-(left + right), -index)
        left_wait = [(-(time[i][0] + time[i][2]), -i) for i in range(k)]
        heapq.heapify(left_wait)
        right_wait = []
        
        # Min-heaps ordered by completion time: (finish_time, index)
        left_work = []
        right_work = []
        
        curr_time = 0
        remaining_boxes = n
        
        while remaining_boxes > 0 or right_wait or right_work:
            # 1. Move any workers who finished working in either warehouse to their bridge queue
            while left_work and left_work[0][0] <= curr_time:
                _, i = heapq.heappop(left_work)
                heapq.heappush(left_wait, (-(time[i][0] + time[i][2]), -i))
                
            while right_work and right_work[0][0] <= curr_time:
                _, i = heapq.heappop(right_work)
                heapq.heappush(right_wait, (-(time[i][0] + time[i][2]), -i))
                
            # 2. Prioritize workers waiting on the right side to cross left
            if right_wait:
                _, neg_i = heapq.heappop(right_wait)
                i = -neg_i
                curr_time += time[i][2]  # left_i
                heapq.heappush(left_work, (curr_time + time[i][3], i))  # + put_i
                
            # 3. Otherwise, send a worker from the left if boxes still need to be picked up
            elif remaining_boxes > 0 and left_wait:
                _, neg_i = heapq.heappop(left_wait)
                i = -neg_i
                remaining_boxes -= 1
                curr_time += time[i][0]  # right_i
                heapq.heappush(right_work, (curr_time + time[i][1], i))  # + pick_i
                
            # 4. Bridge is idle; jump clock to the earliest warehouse completion event
            else:
                next_time = float('inf')
                if remaining_boxes > 0 and left_work:
                    next_time = min(next_time, left_work[0][0])
                if right_work:
                    next_time = min(next_time, right_work[0][0])
                curr_time = next_time
                
        return curr_time
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
- [934. Shortest Bridge](../../0501-1000/0971-shortest-bridge/)
- [121. Best Time to Buy and Sell Stock](../../0001-0500/0121-best-time-to-buy-and-sell-stock/)
- [122. Best Time to Buy and Sell Stock II](../../0001-0500/0122-best-time-to-buy-and-sell-stock-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/time-to-cross-a-bridge/)
