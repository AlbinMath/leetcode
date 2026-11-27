# LeetCode 1606: Find Servers That Handled Most Number of Requests

**LeetCode Problem #1606 — Find Servers That Handled Most Number of Requests**
Solve LeetCode Find Servers That Handled Most Number of Requests using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Servers That Handled Most Number of Requests |
| LeetCode | #1606 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `k` servers numbered from `0` to `k-1` that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but **cannot handle more than one request at a time**. The requests are assigned to servers according to a specific algorithm:

The `i^th` (0-indexed) request arrives. 
 If all servers are busy, the request is dropped (not handled at all). 
 If the `(i % k)^th` server is available, assign the request to that server. 
 Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the `i^th` server is busy, try to assign the request to the `(i+1)^th` server, then the `(i+2)^th` server, and so on.

You are given a **strictly increasing** array `arrival` of positive integers, where `arrival[i]` represents the arrival time of the `i^th` request, and another array `load`, where `load[i]` represents the load of the `i^th` request (the time it takes to complete). Your goal is to find the **busiest server(s)**. A server is considered **busiest** if it handled the most number of requests successfully among all the servers.

Return *a list containing the IDs (0-indexed) of the **busiest server(s)***. You may return the IDs in any order.

## Constraints
- `1 <= k <= 10^5`
- `1 <= arrival.length, load.length <= 10^5`
- `arrival.length == load.length`
- `1 <= arrival[i], load[i] <= 10^9`
- `arrival` is **strictly increasing**.

## Examples
### Example 1
- **Input:** `k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]`
- **Output:** `[1]`
- **Explanation:** All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.

### Example 2
- **Input:** `k = 3, arrival = [1,2,3,4], load = [1,2,1,2]`
- **Output:** `[0]`
- **Explanation:** The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.

### Example 3
- **Input:** `k = 3, arrival = [1,2,3], load = [10,12,11]`
- **Output:** `[0,1,2]`
- **Explanation:** Each server handles a single request, so they are all considered the busiest.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Servers That Handled Most Number of Requests**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1]`.
4. **Verification:** All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.

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
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))          # heap of virtual indices (already a valid heap)
        busy = []                      # heap of (end_time, server_id)
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            # Release servers that have finished by time `start`.
            while busy and busy[0][0] <= start:
                _, sid = heapq.heappop(busy)
                # Smallest value >= i that is congruent to sid (mod k)
                nxt = i + ((sid - i) % k)
                heapq.heappush(free, nxt)

            if not free:
                continue               # all servers busy -> drop

            sid = heapq.heappop(free) % k
            count[sid] += 1
            heapq.heappush(busy, (start + dur, sid))

        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]
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
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2177-find-three-consecutive-integers-that-sum-to-a-given-number/)
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1160-find-words-that-can-be-formed-by-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/)
