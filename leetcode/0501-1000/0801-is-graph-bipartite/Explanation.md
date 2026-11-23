# LeetCode 785: Is Graph Bipartite?

**LeetCode Problem #785 — Is Graph Bipartite?**
Solve LeetCode Is Graph Bipartite? using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Is Graph Bipartite? |
| LeetCode | #785 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is an **undirected** graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. More formally, for each `v` in `graph[u]`, there is an undirected edge between node `u` and node `v`. The graph has the following properties:

There are no self-edges (`graph[u]` does not contain `u`). 
 There are no parallel edges (`graph[u]` does not contain duplicate values). 
 If `v` is in `graph[u]`, then `u` is in `graph[v]` (the graph is undirected). 
 The graph may not be connected, meaning there may be two nodes `u` and `v` such that there is no path between them.

A graph is **bipartite** if the nodes can be partitioned into two independent sets `A` and `B` such that **every** edge in the graph connects a node in set `A` and a node in set `B`.

Return `true`* if and only if it is **bipartite***.

## Constraints
- `graph.length == n`
- `1 <= n <= 100`
- `0 <= graph[u].length < n`
- `0 <= graph[u][i] <= n - 1`
- `graph[u]` does not contain `u`.
- All the values of `graph[u]` are **unique**.
- If `graph[u]` contains `v`, then `graph[v]` contains `u`.

## Examples
### Example 1
- **Input:** `graph = [[1,2,3],[0,2],[0,1,3],[0,2]]`
- **Output:** `false`
- **Explanation:** There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

### Example 2
- **Input:** `graph = [[1,3],[0,2],[1,3],[0,2]]`
- **Output:** `true`
- **Explanation:** We can partition the nodes into two sets: {0, 2} and {1, 3}.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Is Graph Bipartite?**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `graph = [[1,2,3],[0,2],[0,1,3],[0,2]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

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
from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1: color A, -1: color B
        
        for i in range(n):
            if color[i] != 0:
                continue
            
            # Start BFS from unvisited component
            queue = deque([i])
            color[i] = 1
            
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
                        
        return True
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
- [133. Clone Graph](../../0001-0500/0133-clone-graph/)
- [882. Reachable Nodes In Subdivided Graph](../../0501-1000/0918-reachable-nodes-in-subdivided-graph/)
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](../../1501-2000/1701-remove-max-number-of-edges-to-keep-graph-fully-traversable/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/is-graph-bipartite/)
