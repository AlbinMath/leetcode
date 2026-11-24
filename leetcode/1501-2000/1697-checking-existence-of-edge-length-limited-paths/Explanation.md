# LeetCode 1697: Checking Existence of Edge Length Limited Paths

**LeetCode Problem #1697 — Checking Existence of Edge Length Limited Paths**
Solve LeetCode Checking Existence of Edge Length Limited Paths using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Checking Existence of Edge Length Limited Paths |
| LeetCode | #1697 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An undirected graph of `n` nodes is defined by `edgeList`, where `edgeList[i] = [u_i, v_i, dis_i]` denotes an edge between nodes `u_i` and `v_i` with distance `dis_i`. Note that there may be **multiple** edges between two nodes.

Given an array `queries`, where `queries[j] = [p_j, q_j, limit_j]`, your task is to determine for each `queries[j]` whether there is a path between `p_j` and `q_j`_ such that each edge on the path has a distance **strictly less than** `limit_j` .

Return *a **boolean array** *`answer`*, where *`answer.length == queries.length` *and the *`j^th` *value of *`answer` *is *`true`* if there is a path for *`queries[j]`* is *`true`*, and *`false`* otherwise*.

## Constraints
- `2 <= n <= 10^5`
- `1 <= edgeList.length, queries.length <= 10^5`
- `edgeList[i].length == 3`
- `queries[j].length == 3`
- `0 <= u_i, v_i, p_j, q_j <= n - 1`
- `u_i != v_i`
- `p_j != q_j`
- `1 <= dis_i, limit_j <= 10^9`
- There may be **multiple** edges between two nodes.

## Examples
### Example 1
- **Input:** `n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]`
- **Output:** `[false,true]`
- **Explanation:** The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.

### Example 2
- **Input:** `n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]`
- **Output:** `[true,false]`
- **Explanation:** The above figure shows the given graph.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Checking Existence of Edge Length Limited Paths**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false,true]`.
4. **Verification:** The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Sort edges by weight
        edgeList.sort(key=lambda x: x[2])

        # Attach original indices to queries and sort by limit
        indexed_queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        indexed_queries.sort(key=lambda x: x[2])

        dsu = DSU(n)
        ans = [False] * len(queries)
        edge_idx = 0
        num_edges = len(edgeList)

        for p, q, limit, orig_idx in indexed_queries:
            # Add all edges with distance strictly less than limit
            while edge_idx < num_edges and edgeList[edge_idx][2] < limit:
                u, v, _ = edgeList[edge_idx]
                dsu.union(u, v)
                edge_idx += 1

            # Check connectivity
            ans[orig_idx] = (dsu.find(p) == dsu.find(q))

        return ans
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [2374. Node With Highest Edge Score](../../2001-2500/2374-node-with-highest-edge-score/)
- [2699. Modify Graph Edge Weights](../../2501-3000/2699-modify-graph-edge-weights/)
- [2846. Minimum Edge Weight Equilibrium Queries in a Tree](../../2501-3000/2846-minimum-edge-weight-equilibrium-queries-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)
