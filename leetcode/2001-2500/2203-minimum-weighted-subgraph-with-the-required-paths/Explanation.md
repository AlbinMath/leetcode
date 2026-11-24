# LeetCode 2203: Minimum Weighted Subgraph With the Required Paths

**LeetCode Problem #2203 — Minimum Weighted Subgraph With the Required Paths**
Solve LeetCode Minimum Weighted Subgraph With the Required Paths using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Weighted Subgraph With the Required Paths |
| LeetCode | #2203 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` denoting the number of nodes of a **weighted directed** graph. The nodes are numbered from `0` to `n - 1`.

You are also given a 2D integer array `edges` where `edges[i] = [from_i, to_i, weight_i]` denotes that there exists a **directed** edge from `from_i` to `to_i` with weight `weight_i`.

Lastly, you are given three **distinct** integers `src1`, `src2`, and `dest` denoting three distinct nodes of the graph.

Return *the **minimum weight** of a subgraph of the graph such that it is **possible** to reach* `dest` *from both* `src1` *and* `src2` *via a set of edges of this subgraph*. In case such a subgraph does not exist, return `-1`.

A **subgraph** is a graph whose vertices and edges are subsets of the original graph. The **weight** of a subgraph is the sum of weights of its constituent edges.

## Constraints
- `3 <= n <= 10^5`
- `0 <= edges.length <= 10^5`
- `edges[i].length == 3`
- `0 <= from_i, to_i, src1, src2, dest <= n - 1`
- `from_i != to_i`
- `src1`, `src2`, and `dest` are pairwise distinct.
- `1 <= weight[i] <= 10^5`

## Examples
### Example 1
- **Input:** `n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5`
- **Output:** `9`
- **Explanation:** The above figure represents the input graph.
The blue edges represent one of the subgraphs that yield the optimal answer.
Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the

### Example 2
- **Input:** `n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2`
- **Output:** `-1`
- **Explanation:** The above figure represents the input graph.
It can be seen that there does not exist any path from node 1 to node 2, hence there are no subgraphs satisfying all the

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Weighted Subgraph With the Required Paths**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The above figure represents the input graph.
The blue edges represent one of the subgraphs that yield the optimal answer.
Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the

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
    def minimumWeight(self, n, edges, src1, src2, dest):
        g, rg = defaultdict(list), defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))

        def dij(s, graph):
            d = [float('inf')] * n
            d[s] = 0
            q = [(0, s)]
            while q:
                w, u = heapq.heappop(q)
                if w > d[u]:
                    continue
                for v, c in graph[u]:
                    if w + c < d[v]:
                        d[v] = w + c
                        heapq.heappush(q, (d[v], v))
            return d

        a = dij(src1, g)
        b = dij(src2, g)
        c = dij(dest, rg)

        ans = min((a[i] + b[i] + c[i] for i in range(n)
                   if a[i] < float('inf') and b[i] < float('inf')
                   and c[i] < float('inf')), default=float('inf'))
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
- [3553. Minimum Weighted Subgraph With the Required Paths II](../../3501-4000/3553-minimum-weighted-subgraph-with-the-required-paths-ii/)
- [3789. Minimum Cost to Acquire Required Items](../../3501-4000/3789-minimum-cost-to-acquire-required-items/)
- [3108. Minimum Cost Walk in Weighted Graph](../../3001-3500/3108-minimum-cost-walk-in-weighted-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/)
