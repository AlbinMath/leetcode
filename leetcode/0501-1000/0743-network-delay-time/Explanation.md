# LeetCode 743: Network Delay Time

**LeetCode Problem #743 — Network Delay Time**
Solve LeetCode Network Delay Time using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Network Delay Time |
| LeetCode | #743 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`, where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return *the **minimum** time it takes for all the* `n` *nodes to receive the signal*. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

## Constraints
- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u_i, v_i <= n`
- `u_i != v_i`
- `0 <= w_i <= 100`
- All the pairs `(u_i, v_i)` are **unique**. (i.e., no multiple edges.)

## Examples
### Example 1
- **Input:** `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`
- **Output:** `2`

### Example 2
- **Input:** `times = [[1,2,1]], n = 2, k = 1`
- **Output:** `1`

### Example 3
- **Input:** `times = [[1,2,1]], n = 2, k = 2`
- **Output:** `-1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Network Delay Time**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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

class Solution:
    def networkDelayTime(self, times, n, k):
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))

        d = [float('inf')] * (n + 1)
        d[k] = 0
        q = [(0, k)]

        while q:
            t, u = heapq.heappop(q)
            if t > d[u]:
                continue
            for v, w in g[u]:
                if t + w < d[v]:
                    d[v] = t + w
                    heapq.heappush(q, (d[v], v))

        ans = max(d[1:])
        return ans if ans < float('inf') else -1
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
- [2039. The Time When the Network Becomes Idle](../../2001-2500/2039-the-time-when-the-network-becomes-idle/)
- [1192. Critical Connections in a Network](../../1001-1500/1192-critical-connections-in-a-network/)
- [1319. Number of Operations to Make Network Connected](../../1001-1500/1319-number-of-operations-to-make-network-connected/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/network-delay-time/)
