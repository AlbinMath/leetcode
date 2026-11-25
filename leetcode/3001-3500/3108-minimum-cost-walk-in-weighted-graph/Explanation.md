# LeetCode 3108: Minimum Cost Walk in Weighted Graph

**LeetCode Problem #3108 — Minimum Cost Walk in Weighted Graph**
Solve LeetCode Minimum Cost Walk in Weighted Graph using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Walk in Weighted Graph |
| LeetCode | #3108 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected weighted graph with `n` vertices labeled from `0` to `n - 1`.

You are given the integer `n` and an array `edges`, where `edges[i] = [u_i, v_i, w_i]` indicates that there is an edge between vertices `u_i` and `v_i` with a weight of `w_i`.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The **cost** of a walk starting at node `u` and ending at node `v` is defined as the bitwise `AND` of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is `w_0, w_1, w_2, ..., w_k`, then the cost is calculated as `w_0 & w_1 & w_2 & ... & w_k`, where `&` denotes the bitwise `AND` operator.

You are also given a 2D array `query`, where `query[i] = [s_i, t_i]`. For each query, you need to find the minimum cost of the walk starting at vertex `s_i` and ending at vertex `t_i`. If there exists no such walk, the answer is `-1`.

Return *the array *`answer`*, where *`answer[i]`* denotes the **minimum** cost of a walk for query *`i`.

## Constraints
- `2 <= n <= 10^5`
- `0 <= edges.length <= 10^5`
- `edges[i].length == 3`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `0 <= w_i <= 10^5`
- `1 <= query.length <= 10^5`
- `query[i].length == 2`
- `0 <= s_i, t_i <= n - 1`
- `s_i != t_i`

## Examples
### Example 1
- **Input:** `n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]`
- **Output:** `[1,-1]`
- **Explanation:** To achieve the cost of 1 in the first query, we need to move on the following edges: `0->1` (weight 7), `1->2` (weight 1), `2->1` (weight 1), `1->3` (weight 7). 

 In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

### Example 2
- **Input:** `n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]`
- **Output:** `[0]`
- **Explanation:** To achieve the cost of 0 in the first query, we need to move on the following edges: `1->2` (weight 1), `2->1` (weight 6), `1->2` (weight 1).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost Walk in Weighted Graph**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,-1]`.
4. **Verification:** To achieve the cost of 1 in the first query, we need to move on the following edges: `0->1` (weight 7), `1->2` (weight 1), `2->1` (weight 1), `1->3` (weight 7). 

 In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

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

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        # (1 << 30) - 1 has all bits set for integers up to 10^5
        self.and_cost = [(1 << 30) - 1] * n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, u: int, v: int, w: int):
        ru, rv = self.find(u), self.find(v)
        if ru != rv:
            self.parent[rv] = ru
            self.and_cost[ru] &= self.and_cost[rv]
        self.and_cost[ru] &= w


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)

        for u, v, w in edges:
            dsu.union(u, v, w)

        ans = []
        for s, t in query:
            if s == t:
                ans.append(0)
            elif dsu.find(s) != dsu.find(t):
                ans.append(-1)
            else:
                ans.append(dsu.and_cost[dsu.find(s)])

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
- [2203. Minimum Weighted Subgraph With the Required Paths](../../2001-2500/2203-minimum-weighted-subgraph-with-the-required-paths/)
- [3553. Minimum Weighted Subgraph With the Required Paths II](../../3501-4000/3553-minimum-weighted-subgraph-with-the-required-paths-ii/)
- [1761. Minimum Degree of a Connected Trio in a Graph](../../1501-2000/1761-minimum-degree-of-a-connected-trio-in-a-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/)
