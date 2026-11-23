# LeetCode 1192: Critical Connections in a Network

**LeetCode Problem #1192 — Critical Connections in a Network**
Solve LeetCode Critical Connections in a Network using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Critical Connections in a Network |
| LeetCode | #1192 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between servers `a_i` and `b_i`. Any server can reach other servers directly or indirectly through the network.

A *critical connection* is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

## Constraints
- `2 <= n <= 10^5`
- `n - 1 <= connections.length <= 10^5`
- `0 <= a_i, b_i <= n - 1`
- `a_i != b_i`
- There are no repeated connections.

## Examples
### Example 1
- **Input:** `n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]`
- **Output:** `[[1,3]]`
- **Explanation:** [[3,1]] is also accepted.

### Example 2
- **Input:** `n = 2, connections = [[0,1]]`
- **Output:** `[[0,1]]`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Critical Connections in a Network**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,3]]`.
4. **Verification:** [[3,1]] is also accepted.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var criticalConnections = function(n, connections) {
    const graph = Array.from({ length: n }, () => []);

    // Build adjacency list
    for (const [u, v] of connections) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const disc = new Array(n).fill(-1);
    const low = new Array(n).fill(-1);
    const bridges = [];

    let time = 0;

    function dfs(node, parent) {
        disc[node] = low[node] = time++;

        for (const neighbor of graph[node]) {
            if (neighbor === parent) continue;

            if (disc[neighbor] === -1) {
                // Visit an unvisited neighbor
                dfs(neighbor, node);

                // Update low-link value
                low[node] = Math.min(low[node], low[neighbor]);

                // Check whether this edge is a bridge
                if (low[neighbor] > disc[node]) {
                    bridges.push([node, neighbor]);
                }
            } else {
                // Back edge to an already visited node
                low[node] = Math.min(low[node], disc[neighbor]);
            }
        }
    }

    // Start DFS from node 0
    dfs(0, -1);

    return bridges;
};
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
- [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](../../1501-2000/1613-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [743. Network Delay Time](../../0501-1000/0744-network-delay-time/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/)
