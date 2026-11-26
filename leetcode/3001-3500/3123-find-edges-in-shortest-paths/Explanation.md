# LeetCode 3123: Find Edges in Shortest Paths

**LeetCode Problem #3123 — Find Edges in Shortest Paths**
Solve LeetCode Find Edges in Shortest Paths using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Edges in Shortest Paths |
| LeetCode | #3123 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an undirected weighted graph of `n` nodes numbered from 0 to `n - 1`. The graph consists of `m` edges represented by a 2D array `edges`, where `edges[i] = [a_i, b_i, w_i]` indicates that there is an edge between nodes `a_i` and `b_i` with weight `w_i`.

Consider all the shortest paths from node 0 to node `n - 1` in the graph. You need to find a **boolean** array `answer` where `answer[i]` is `true` if the edge `edges[i]` is part of **at least** one shortest path. Otherwise, `answer[i]` is `false`.

Return the array `answer`.

**Note** that the graph may not be connected.

## Constraints
- `2 <= n <= 5 * 10^4`
- `m == edges.length`
- `1 <= m <= min(5 * 10^4, n * (n - 1) / 2)`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- `1 <= w_i <= 10^5`
- There are no repeated edges.

## Examples
### Example 1
- **Input:** `n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]`
- **Output:** `[true,true,true,false,true,true,true,false]`
- **Explanation:** The following are

### Example 2
- **Input:** `n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]`
- **Output:** `[true,false,false,true]`
- **Explanation:** There is one shortest path between nodes 0 and 3, which is the path `0 -> 2 -> 3` with the sum of weights `1 + 2 = 3`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Edges in Shortest Paths**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,true,true,false,true,true,true,false]`.
4. **Verification:** The following are

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var findAnswer = function (n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b, w] of edges) {
        adj[a].push([b, w]);
        adj[b].push([a, w]);
    }

    const dijkstra = (src) => {
        const heap = [];
        const push = (item) => {
            heap.push(item);
            let i = heap.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (heap[p][0] <= heap[i][0]) break;
                [heap[p], heap[i]] = [heap[i], heap[p]];
                i = p;
            }
        };
        const pop = () => {
            const top = heap[0];
            const last = heap.pop();
            if (heap.length) {
                heap[0] = last;
                let i = 0;
                const len = heap.length;
                while (true) {
                    const l = 2 * i + 1, r = l + 1;
                    let s = i;
                    if (l < len && heap[l][0] < heap[s][0]) s = l;
                    if (r < len && heap[r][0] < heap[s][0]) s = r;
                    if (s === i) break;
                    [heap[s], heap[i]] = [heap[i], heap[s]];
                    i = s;
                }
            }
            return top;
        };

        const dist = new Array(n).fill(Infinity);
        dist[src] = 0;
        push([0, src]);
        while (heap.length) {
            const [t, u] = pop();
            if (t > dist[u]) continue;
            for (const [v, w] of adj[u]) {
                const nt = t + w;
                if (nt < dist[v]) {
                    dist[v] = nt;
                    push([nt, v]);
                }
            }
        }
        return dist;
    };

    const d0 = dijkstra(0);
    const d1 = dijkstra(n - 1);
    const D = d0[n - 1];

    if (D === Infinity) return new Array(edges.length).fill(false);

    return edges.map(([a, b, w]) =>
        d0[a] + w + d1[b] === D || d0[b] + w + d1[a] === D
    );
};
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
- [943. Find the Shortest Superstring](../../0501-1000/0943-find-the-shortest-superstring/)
- [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](../../1001-1500/1489-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
- [214. Shortest Palindrome](../../0001-0500/0214-shortest-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-edges-in-shortest-paths/)
