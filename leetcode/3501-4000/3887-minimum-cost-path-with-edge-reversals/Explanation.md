# LeetCode 3650: Minimum Cost Path with Edge Reversals

**LeetCode Problem #3650 — Minimum Cost Path with Edge Reversals**
Solve LeetCode Minimum Cost Path with Edge Reversals using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path with Edge Reversals |
| LeetCode | #3650 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a directed, weighted graph with `n` nodes labeled from 0 to `n - 1`, and an array `edges` where `edges[i] = [u_i, v_i, w_i]` represents a directed edge from node `u_i` to node `v_i` with cost `w_i`.

Each node `u_i` has a switch that can be used **at most once**: when you arrive at `u_i` and have not yet used its switch, you may activate it on one of its incoming edges `v_i &rarr; u_i` reverse that edge to `u_i &rarr; v_i` and **immediately** traverse it.

The reversal is only valid for that single move, and using a reversed edge costs `2 * w_i`.

Return the **minimum** total cost to travel from node 0 to node `n - 1`. If it is not possible, return -1.

## Constraints
- `2 <= n <= 5 * 10^4`
- `1 <= edges.length <= 10^5`
- `edges[i] = [u_i, v_i, w_i]`
- `0 <= u_i, v_i <= n - 1`
- `1 <= w_i <= 1000`

## Examples
### Example 1
- **Input:** `n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]`
- **Output:** `5`

### Example 2
- **Input:** `n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]`
- **Output:** `3`
- **Explanation:** No reversal is needed. Take the path `0 &rarr; 2` (cost 1), then `2 &rarr; 1` (cost 1), then `1 &rarr; 3` (cost 1). 
 Total cost is `1 + 1 + 1 = 3`.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost Path with Edge Reversals**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.

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
var minCost = function (n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, 2 * w]);
    }

    // Min-heap of [cost, node]
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
    dist[0] = 0;
    push([0, 0]);

    while (heap.length) {
        const [d, u] = pop();
        if (d > dist[u]) continue;
        if (u === n - 1) return d;
        for (const [v, w] of adj[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                push([nd, v]);
            }
        }
    }
    return -1;
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2686-minimum-cost-of-a-path-with-special-roads/)
- [4003. Minimum Cost Path with Alternating Directions III](../../3501-4000/3926-minimum-cost-path-with-alternating-directions-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/)
