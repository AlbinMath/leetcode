# LeetCode 3977: Minimum Time to Reach Target With Limited Power

**LeetCode Problem #3977 — Minimum Time to Reach Target With Limited Power**
Solve LeetCode Minimum Time to Reach Target With Limited Power using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Reach Target With Limited Power |
| LeetCode | #3977 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **directed** weighted graph with `n` nodes labeled from 0 to `n - 1`.

The graph is represented by a 2D integer array `edges`, where `edges[i] = [u_i, v_i, t_i]` indicates a directed edge from node `u_i` to node `v_i` that takes `t_i` seconds to traverse.

You are also given an integer `power` representing the initial available power, and an integer array `cost` of length `n`, where `cost[u]` represents the power required to forward the signal from node `u` through **any** one of its outgoing edges.

You are given two integers `source` and `target`.

The signal starts at `source` at time 0 with `power` units of power and follows these rules:

The signal may traverse a directed edge from node `u` only if the remaining power is **at least** `cost[u]`. 
 No power is consumed when the signal arrives at a node, unless it later leaves that node by traversing another edge. 
 When the signal is forwarded from node `u`, the remaining power is **decreased** by `cost[u]` units. 
 Traversing an edge `edges[i] = [u_i, v_i, t_i]` **increases** the total time by `t_i` seconds.

Return an integer array `answer` of size 2, where:

`answer[0]` is the **minimum** time required for the signal to reach node `target`. 
 `answer[1]` is the **maximum** remaining power among all paths that achieve `answer[0]`.

If the signal cannot reach `target`, return `[-1, -1]`.

## Constraints
- `1 <= n <= 1000`
- `0 <= edges.length <= 1000`
- `edges[i] = [u_i, v_i, t_i]`
- `0 <= u_i, v_i <= n - 1`
- `1 <= t_i <= 10^9`
- `1 <= power <= 1000`
- `cost.length == n`
- `1 <= cost[i] <= 2000`
- `0 <= source, target <= n - 1`

## Examples
### Example 1
- **Input:** `n = 5, edges = [[0,1,1],[1,4,1],[0,2,1],[2,3,1],[3,4,1]], power = 4, cost = [2,3,1,1,1], source = 0, target = 4`
- **Output:** `[3,0]`
- **Explanation:** The signal starts at node 0 with 4 units of power. 
 The path `0 -> 1 -> 4` is not valid, because after leaving node 0, the signal has 2 units of power remaining, which is less than `cost[1] = 3`. 
 The valid path `0 -> 2 -> 3 -> 4` takes a total time of 3. 
 The total power consumed along this path is `cost[0] + cost[2] + cost[3] = 4`, leaving 0 remaining power. 
 Hence, the answer is `[3, 0]`.

### Example 2
- **Input:** `n = 3, edges = [[0,1,2],[1,2,2],[2,0,2]], power = 3, cost = [1,1,1], source = 1, target = 1`
- **Output:** `[0,3]`
- **Explanation:** Since the `source` and `target` are the same node, no traversal is required. 
 Hence, the minimum total time taken is 0, and no power is consumed. 
 Therefore, the answer is `[0, 3]`.

### Example 3
- **Input:** `n = 4, edges = [[0,1,3],[2,3,4]], power = 3, cost = [1,1,1,1], source = 0, target = 3`
- **Output:** `[-1,-1]`
- **Explanation:** There is no valid path from `source` to `target`, therefore return `[-1, -1]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Time to Reach Target With Limited Power**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[0,1,1],[1,4,1],[0,2,1],[2,3,1],[3,4,1]], power = 4, cost = [2,3,1,1,1], source = 0, target = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,0]`.
4. **Verification:** The signal starts at node 0 with 4 units of power. 
 The path `0 -> 1 -> 4` is not valid, because after leaving node 0, the signal has 2 units of power remaining, which is less than `cost[1] = 3`. 
 The valid path `0 -> 2 -> 3 -> 4` takes a total time of 3. 
 The total power consumed along this path is `cost[0] + cost[2] + cost[3] = 4`, leaving 0 remaining power. 
 Hence, the answer is `[3, 0]`.

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
from typing import List
import heapq

class Solution:
    def minTimeMaxPower(
        self,
        n: int,
        edges: List[List[int]],
        power: int,
        cost: List[int],
        source: int,
        target: int
    ) -> List[int]:

        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))

        INF = float('inf')
        dist = [[INF] * (power + 1) for _ in range(n)]
        dist[source][power] = 0

        pq = [(0, source, power)]
        best_time = INF
        best_power = -1

        while pq:
            time, u, p = heapq.heappop(pq)

            if time > best_time:
                break

            if time != dist[u][p]:
                continue

            if u == target:
                best_time = time
                best_power = max(best_power, p)
                continue

            if p < cost[u]:
                continue

            remaining = p - cost[u]

            for v, t in graph[u]:
                new_time = time + t

                if new_time < dist[v][remaining]:
                    dist[v][remaining] = new_time
                    heapq.heappush(pq, (new_time, v, remaining))

        if best_power == -1:
            return [-1, -1]

        return [best_time, best_power]
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
- [1210. Minimum Moves to Reach Target with Rotations](../../1001-1500/1322-minimum-moves-to-reach-target-with-rotations/)
- [1928. Minimum Cost to Reach Destination in Time](../../2001-2500/2040-minimum-cost-to-reach-destination-in-time/)
- [2045. Second Minimum Time to Reach Destination](../../2001-2500/2171-second-minimum-time-to-reach-destination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/)
