# LeetCode 1129: Shortest Path with Alternating Colors

**LeetCode Problem #1129 — Shortest Path with Alternating Colors**
Solve LeetCode Shortest Path with Alternating Colors using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path with Alternating Colors |
| LeetCode | #1129 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to `n - 1`. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays `redEdges` and `blueEdges` where:

`redEdges[i] = [a_i, b_i]` indicates that there is a directed red edge from node `a_i` to node `b_i` in the graph, and 
 `blueEdges[j] = [u_j, v_j]` indicates that there is a directed blue edge from node `u_j` to node `v_j` in the graph.

Return an array `answer` of length `n`, where each `answer[x]` is the length of the shortest path from node `0` to node `x` such that the edge colors alternate along the path, or `-1` if such a path does not exist.

## Constraints
- `1 <= n <= 100`
- `0 <= redEdges.length, blueEdges.length <= 400`
- `redEdges[i].length == blueEdges[j].length == 2`
- `0 <= a_i, b_i, u_j, v_j < n`

## Examples
### Example 1
- **Input:** `n = 3, redEdges = [[0,1],[1,2]], blueEdges = []`
- **Output:** `[0,1,-1]`

### Example 2
- **Input:** `n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]`
- **Output:** `[0,1,-1]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Path with Alternating Colors**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, redEdges = [[0,1],[1,2]], blueEdges = []`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1,-1]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        g = [[[] for _ in range(n)] for _ in range(2)]
        for u, v in redEdges:
            g[0][u].append(v)
        for u, v in blueEdges:
            g[1][u].append(v)

        d = [[-1] * n for _ in range(2)]
        d[0][0] = d[1][0] = 0
        q = deque([(0, 0), (0, 1)])

        while q:
            u, c = q.popleft()
            for v in g[1-c][u]:
                if d[1-c][v] == -1:
                    d[1-c][v] = d[c][u] + 1
                    q.append((v, 1-c))

        return [min((x for x in (d[0][i], d[1][i]) if x != -1), default=-1) for i in range(n)]
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [4003. Minimum Cost Path with Alternating Directions III](../../4001-4500/4003-minimum-cost-path-with-alternating-directions-iii/)
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0847-shortest-path-visiting-all-nodes/)
- [864. Shortest Path to Get All Keys](../../0501-1000/0864-shortest-path-to-get-all-keys/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-with-alternating-colors/)
