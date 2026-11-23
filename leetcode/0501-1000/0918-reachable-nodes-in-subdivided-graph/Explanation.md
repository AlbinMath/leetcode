# LeetCode 882: Reachable Nodes In Subdivided Graph

**LeetCode Problem #882 — Reachable Nodes In Subdivided Graph**
Solve LeetCode Reachable Nodes In Subdivided Graph using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reachable Nodes In Subdivided Graph |
| LeetCode | #882 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an undirected graph (the **"original graph"**) with `n` nodes labeled from `0` to `n - 1`. You decide to **subdivide** each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of `edges` where `edges[i] = [u_i, v_i, cnt_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the original graph, and `cnt_i` is the total number of new nodes that you will **subdivide** the edge into. Note that `cnt_i == 0` means you will not subdivide the edge.

To **subdivide** the edge `[u_i, v_i]`, replace it with `(cnt_i + 1)` new edges and `cnt_i` new nodes. The new nodes are `x_1`, `x_2`, ..., `x_cnt i `, and the new edges are `[u_i, x_1]`, `[x_1, x_2]`, `[x_2, x_3]`, ..., `[x_cnt i-1 , x_cnt i ]`, `[x_cnt i , v_i]`.

In this **new graph**, you want to know how many nodes are **reachable** from the node `0`, where a node is **reachable** if the distance is `maxMoves` or less.

Given the original graph and `maxMoves`, return *the number of nodes that are **reachable** from node *`0`* in the new graph*.

## Constraints
- `0 <= edges.length <= min(n * (n - 1) / 2, 10^4)`
- `edges[i].length == 3`
- `0 <= u_i < v_i < n`
- There are **no multiple edges** in the graph.
- `0 <= cnt_i <= 10^4`
- `0 <= maxMoves <= 10^9`
- `1 <= n <= 3000`

## Examples
### Example 1
- **Input:** `edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3`
- **Output:** `13`
- **Explanation:** The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.

### Example 2
- **Input:** `edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4`
- **Output:** `23`

### Example 3
- **Input:** `edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5`
- **Output:** `1`
- **Explanation:** Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reachable Nodes In Subdivided Graph**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.

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
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        g = defaultdict(list)
        for u, v, c in edges:
            g[u].append((v, c+1))
            g[v].append((u, c+1))

        d = [float('inf')] * n
        d[0] = 0
        q = [(0, 0)]

        while q:
            dist, u = heapq.heappop(q)
            if dist > d[u]:
                continue
            for v, w in g[u]:
                nd = dist + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(q, (nd, v))

        ans = sum(x <= maxMoves for x in d)
        for u, v, c in edges:
            a = max(0, maxMoves - d[u]) if d[u] <= maxMoves else 0
            b = max(0, maxMoves - d[v]) if d[v] <= maxMoves else 0
            ans += min(c, a + b)

        return ans
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
- [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](../../2001-2500/2403-count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
- [2876. Count Visited Nodes in a Directed Graph](../../3001-3500/3140-count-visited-nodes-in-a-directed-graph/)
- [2368. Reachable Nodes With Restrictions](../../2001-2500/2445-reachable-nodes-with-restrictions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)
