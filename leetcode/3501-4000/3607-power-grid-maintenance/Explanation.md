# LeetCode 3607: Power Grid Maintenance

**LeetCode Problem #3607 — Power Grid Maintenance**
Solve LeetCode Power Grid Maintenance using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Power Grid Maintenance |
| LeetCode | #3607 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer c representing c power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing).

These stations are interconnected via n **bidirectional** cables, represented by a 2D array connections , where each element connections[i] = [u_i, v_i] indicates a connection between station `u_i` and station `v_i`. Stations that are directly or indirectly connected form a **power grid**.

Initially, **all** stations are online (operational).

You are also given a 2D array queries , where each query is one of the following *two* types:

[1, x] : A maintenance check is requested for station x . If station `x` is online, it resolves the check by itself. If station `x` is offline, the check is resolved by the operational station with the smallest `id` in the same **power grid** as `x`. If **no** **operational** station *exists* in that grid, return -1.

[2, x] : Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the **order** they appear.

**Note:** The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

## Constraints
- `1 <= c <= 10^5`
- `0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)`
- `connections[i].length == 2`
- `1 <= u_i, v_i <= c`
- `1 <= queries.length <= 2 * 10^5`
- `queries[i].length == 2`
- `1 <= queries[i][1] <= c`

## Examples
### Example 1
- **Input:** `c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]`
- **Output:** `[3,2,3]`
- **Explanation:** Initially, all stations `{1, 2, 3, 4, 5}` are online and form a single power grid. 
 Query `[1,3]`: Station 3 is online, so the maintenance check is resolved by station 3. 
 Query `[2,1]`: Station 1 goes offline. The remaining online stations are `{2, 3, 4, 5}`. 
 Query `[1,1]`: Station 1 is offline, so the check is resolved by the operational station with the smallest `id` among `{2, 3, 4, 5}`, which is station 2. 
 Query `[2,2]`: Station 2 goes offline. The remaining online stations are `{3, 4, 5}`. 
 Query `[1,2]`: Station 2 is offline, so the check is resolved by the operational station with the smallest `id` among `{3, 4, 5}`, which is station 3.

### Example 2
- **Input:** `c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]`
- **Output:** `[1,-1]`
- **Explanation:** There are no connections, so each station is its own isolated grid. 
 Query `[1,1]`: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1. 
 Query `[2,1]`: Station 1 goes offline. 
 Query `[1,1]`: Station 1 is offline and there are no other stations in its grid, so the result is -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Power Grid Maintenance**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,3]`.
4. **Verification:** Initially, all stations `{1, 2, 3, 4, 5}` are online and form a single power grid. 
 Query `[1,3]`: Station 3 is online, so the maintenance check is resolved by station 3. 
 Query `[2,1]`: Station 1 goes offline. The remaining online stations are `{2, 3, 4, 5}`. 
 Query `[1,1]`: Station 1 is offline, so the check is resolved by the operational station with the smallest `id` among `{2, 3, 4, 5}`, which is station 2. 
 Query `[2,2]`: Station 2 goes offline. The remaining online stations are `{3, 4, 5}`. 
 Query `[1,2]`: Station 2 is offline, so the check is resolved by the operational station with the smallest `id` among `{3, 4, 5}`, which is station 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq
from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        # Group all stations into their component lists
        comp_nodes = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            comp_nodes[root].append(i)

        # Convert each component's list into a min-heap
        heaps = {}
        for root, nodes in comp_nodes.items():
            heapq.heapify(nodes)
            heaps[root] = nodes

        is_online = [True] * (c + 1)
        ans = []

        for q_type, x in queries:
            if q_type == 1:
                if is_online[x]:
                    ans.append(x)
                else:
                    root = dsu.find(x)
                    hp = heaps[root]

                    # Lazily remove offline stations from the top of the heap
                    while hp and not is_online[hp[0]]:
                        heapq.heappop(hp)

                    ans.append(hp[0] if hp else -1)
            else:
                is_online[x] = False

        return ans
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1260. Shift 2D Grid](../../1001-1500/1260-shift-2d-grid/)
- [1293. Shortest Path in a Grid with Obstacles Elimination](../../1001-1500/1293-shortest-path-in-a-grid-with-obstacles-elimination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/power-grid-maintenance/)
