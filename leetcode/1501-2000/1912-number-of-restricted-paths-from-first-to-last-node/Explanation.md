# LeetCode 1786: Number of Restricted Paths From First to Last Node

**LeetCode Problem #1786 — Number of Restricted Paths From First to Last Node**
Solve LeetCode Number of Restricted Paths From First to Last Node using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Restricted Paths From First to Last Node |
| LeetCode | #1786 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected weighted connected graph. You are given a positive integer `n` which denotes that the graph has `n` nodes labeled from `1` to `n`, and an array `edges` where each `edges[i] = [u_i, v_i, weight_i]` denotes that there is an edge between nodes `u_i` and `v_i` with weight equal to `weight_i`.

A path from node `start` to node `end` is a sequence of nodes `[z_0, z_1,_ z_2, ..., z_k]` such that `z_0 = start` and `z_k = end` and there is an edge between `z_i` and `z_i+1` where `0 <= i <= k-1`.

The distance of a path is the sum of the weights on the edges of the path. Let `distanceToLastNode(x)` denote the shortest distance of a path between node `n` and node `x`. A **restricted path** is a path that also satisfies that `distanceToLastNode(z_i) > distanceToLastNode(z_i+1)` where `0 <= i <= k-1`.

Return *the number of restricted paths from node* `1` *to node* `n`. Since that number may be too large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n <= 2 * 10^4`
- `n - 1 <= edges.length <= 4 * 10^4`
- `edges[i].length == 3`
- `1 <= u_i, v_i <= n`
- `u_i != v_i`
- `1 <= weight_i <= 10^5`
- There is at most one edge between any two nodes.
- There is at least one path between any two nodes.

## Examples
### Example 1
- **Input:** `n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]`
- **Output:** `3`
- **Explanation:** Each circle contains the node number in black and its `distanceToLastNode value in blue. `The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

### Example 2
- **Input:** `n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]`
- **Output:** `1`
- **Explanation:** Each circle contains the node number in black and its `distanceToLastNode value in blue. `The only restricted path is 1 --> 3 --> 7.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Restricted Paths From First to Last Node**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Each circle contains the node number in black and its `distanceToLastNode value in blue. `The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

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
    def countRestrictedPaths(self, n, edges):
        mod = 10**9 + 7
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        d = [float('inf')] * (n+1)
        d[n] = 0
        q = [(0, n)]

        while q:
            dist, u = heapq.heappop(q)
            if dist > d[u]:
                continue
            for v, w in g[u]:
                nd = dist + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(q, (nd, v))

        dp = [0] * (n+1)
        dp[n] = 1
        for u in sorted(range(1, n+1), key=lambda x: d[x]):
            if u == n:
                continue
            dp[u] = sum(dp[v] for v, _ in g[u] if d[v] < d[u]) % mod

        return dp[1]
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
- [1301. Number of Paths with Max Score](../../1001-1500/1234-number-of-paths-with-max-score/)
- [2259. Remove Digit From Number to Maximize Result](../../2001-2500/2337-remove-digit-from-number-to-maximize-result/)
- [2328. Number of Increasing Paths in a Grid](../../2001-2500/2409-number-of-increasing-paths-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/)
