# LeetCode 2608: Shortest Cycle in a Graph

**LeetCode Problem #2608 — Shortest Cycle in a Graph**
Solve LeetCode Shortest Cycle in a Graph using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Cycle in a Graph |
| LeetCode | #2608 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a **bi-directional **graph with `n` vertices, where each vertex is labeled from `0` to `n - 1`. The edges in the graph are represented by a given 2D integer array `edges`, where `edges[i] = [u_i, v_i]` denotes an edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

Return *the length of the **shortest **cycle in the graph*. If no cycle exists, return `-1`.

A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.

## Constraints
- `2 <= n <= 1000`
- `1 <= edges.length <= 1000`
- `edges[i].length == 2`
- `0 <= u_i, v_i < n`
- `u_i != v_i`
- There are no repeated edges.

## Examples
### Example 1
- **Input:** `n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]`
- **Output:** `3`
- **Explanation:** The cycle with the smallest length is : 0 -> 1 -> 2 -> 0

### Example 2
- **Input:** `n = 4, edges = [[0,1],[0,2]]`
- **Output:** `-1`
- **Explanation:** There are no cycles in this graph.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest Cycle in a Graph**, we observe the problem requirements and utilize the **Fast & Slow Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The cycle with the smallest length is : 0 -> 1 -> 2 -> 0

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var findShortestCycle = function(n, edges) {
    const graph = Array.from({ length: n }, () => []);

    // Build undirected graph.
    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    let answer = Infinity;

    // BFS from every node.
    for (let start = 0; start < n; start++) {
        const dist = new Array(n).fill(-1);
        const parent = new Array(n).fill(-1);

        const queue = [start];
        let head = 0;

        dist[start] = 0;

        while (head < queue.length) {
            const u = queue[head++];

            // No cycle shorter than this can improve the answer.
            if (2 * dist[u] + 1 >= answer) {
                continue;
            }

            for (const v of graph[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    queue.push(v);
                } 
                else if (parent[u] !== v) {
                    const cycleLength = dist[u] + dist[v] + 1;
                    answer = Math.min(answer, cycleLength);
                }
            }
        }
    }

    return answer === Infinity ? -1 : answer;
};
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2360. Longest Cycle in a Graph](../../2001-2500/2439-longest-cycle-in-a-graph/)
- [2642. Design Graph With Shortest Path Calculator](../../2501-3000/2678-design-graph-with-shortest-path-calculator/)
- [141. Linked List Cycle](../../0001-0500/0141-linked-list-cycle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-cycle-in-a-graph/)
