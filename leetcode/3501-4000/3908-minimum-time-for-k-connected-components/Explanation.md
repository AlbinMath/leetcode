# LeetCode 3608: Minimum Time for K Connected Components

**LeetCode Problem #3608 — Minimum Time for K Connected Components**
Solve LeetCode Minimum Time for K Connected Components using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time for K Connected Components |
| LeetCode | #3608 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` and an undirected graph with `n` nodes labeled from 0 to `n - 1`. This is represented by a 2D array `edges`, where `edges[i] = [u_i, v_i, time_i]` indicates an undirected edge between nodes `u_i` and `v_i` that can be removed at `time_i`.

You are also given an integer `k`.

Initially, the graph may be connected or disconnected. Your task is to find the **minimum** time `t` such that after removing all edges with `time <= t`, the graph contains **at least** `k` connected components.

Return the **minimum** time `t`.

A **connected component** is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

## Constraints
- `1 <= n <= 10^5`
- `0 <= edges.length <= 10^5`
- `edges[i] = [u_i, v_i, time_i]`
- `0 <= u_i, v_i < n`
- `u_i != v_i`
- `1 <= time_i <= 10^9`
- `1 <= k <= n`
- There are no duplicate edges.

## Examples
### Example 1
- **Input:** `n = 2, edges = [[0,1,3]], k = 2`
- **Output:** `3`
- **Explanation:** Initially, there is one connected component `{0, 1}`. 
 At `time = 1` or `2`, the graph remains unchanged. 
 At `time = 3`, edge `[0, 1]` is removed, resulting in `k = 2` connected components `{0}`, `{1}`. Thus, the answer is 3.

### Example 2
- **Input:** `n = 3, edges = [[0,1,2],[1,2,4]], k = 3`
- **Output:** `4`
- **Explanation:** Initially, there is one connected component `{0, 1, 2}`. 
 At `time = 2`, edge `[0, 1]` is removed, resulting in two connected components `{0}`, `{1, 2}`. 
 At `time = 4`, edge `[1, 2]` is removed, resulting in `k = 3` connected components `{0}`, `{1}`, `{2}`. Thus, the answer is 4.

### Example 3
- **Input:** `n = 3, edges = [[0,2,5]], k = 2`
- **Output:** `0`
- **Explanation:** Since there are already `k = 2` disconnected components `{1}`, `{0, 2}`, no edge removal is needed. Thus, the answer is 0.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time for K Connected Components**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, edges = [[0,1,3]], k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Initially, there is one connected component `{0, 1}`. 
 At `time = 1` or `2`, the graph remains unchanged. 
 At `time = 3`, edge `[0, 1]` is removed, resulting in `k = 2` connected components `{0}`, `{1}`. Thus, the answer is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

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
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx
            return True
        return False


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        # Sort edges in descending order of time
        edges.sort(key=lambda x: x[2], reverse=True)

        dsu = DSU(n)
        components = n

        for u, v, t in edges:
            ru, rv = dsu.find(u), dsu.find(v)
            if ru != rv:
                # If merging would drop components below k, this edge must be removed
                if components == k:
                    return t
                dsu.union(u, v)
                components -= 1

        return 0
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3378. Count Connected Components in LCM Graph](../../3501-4000/3680-count-connected-components-in-lcm-graph/)
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [995. Minimum Number of K Consecutive Bit Flips](../../1001-1500/1037-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-for-k-connected-components/)
