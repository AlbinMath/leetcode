# LeetCode 3419: Minimize the Maximum Edge Weight of Graph

**LeetCode Problem #3419 — Minimize the Maximum Edge Weight of Graph**
Solve LeetCode Minimize the Maximum Edge Weight of Graph using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize the Maximum Edge Weight of Graph |
| LeetCode | #3419 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers, `n` and `threshold`, as well as a **directed** weighted graph of `n` nodes numbered from 0 to `n - 1`. The graph is represented by a **2D** integer array `edges`, where `edges[i] = [A_i, B_i, W_i]` indicates that there is an edge going from node `A_i` to node `B_i` with weight `W_i`.

You have to remove some edges from this graph (possibly **none**), so that it satisfies the following conditions:

Node 0 must be reachable from all other nodes. 
 The **maximum** edge weight in the resulting graph is **minimized**. 
 Each node has **at most** `threshold` outgoing edges.

Return the **minimum** possible value of the **maximum** edge weight after removing the necessary edges. If it is impossible for all conditions to be satisfied, return -1.

## Constraints
- `2 <= n <= 10^5`
- `1 <= threshold <= n - 1`
- `1 <= edges.length <= min(10^5, n * (n - 1) / 2).`
- `edges[i].length == 3`
- `0 <= A_i, B_i < n`
- `A_i != B_i`
- `1 <= W_i <= 10^6`
- There **may be** multiple edges between a pair of nodes, but they must have unique weights.

## Examples
### Example 1
- **Input:** `n = 5, edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], threshold = 2`
- **Output:** `1`
- **Explanation:** Remove the edge `2 -> 0`. The maximum weight among the remaining edges is 1.

### Example 2
- **Input:** `n = 5, edges = [[0,1,1],[0,2,2],[0,3,1],[0,4,1],[1,2,1],[1,4,1]], threshold = 1`
- **Output:** `-1`
- **Explanation:** It is impossible to reach node 0 from node 2.

### Example 3
- **Input:** `n = 5, edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]], threshold = 1`
- **Output:** `2`
- **Explanation:** Remove the edges `1 -> 3` and `1 -> 4`. The maximum weight among the remaining edges is 2.

### Example 4
- **Input:** `n = 5, edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[4,0,1]], threshold = 1`
- **Output:** `-1`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize the Maximum Edge Weight of Graph**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[1,0,1],[2,0,2],[3,0,1],[4,3,1],[2,1,1]], threshold = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Remove the edge `2 -> 0`. The maximum weight among the remaining edges is 1.

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
var minMaxWeight = function (n, edges, threshold) {
    // Reversed adjacency: for edge A -> B, store B -> A
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b, w] of edges) adj[b].push([a, w]);

    // Min-heap of [bottleneck, node]
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

    const best = new Array(n).fill(Infinity);
    best[0] = 0;
    push([0, 0]);

    while (heap.length) {
        const [b, u] = pop();
        if (b > best[u]) continue;
        for (const [v, w] of adj[u]) {
            const nb = Math.max(b, w);
            if (nb < best[v]) {
                best[v] = nb;
                push([nb, v]);
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (best[i] === Infinity) return -1;
        if (best[i] > ans) ans = best[i];
    }
    return ans;
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
- [3547. Maximum Sum of Edge Values in a Graph](../../3501-4000/3547-maximum-sum-of-edge-values-in-a-graph/)
- [2439. Minimize Maximum of Array](../../2001-2500/2439-minimize-maximum-of-array/)
- [2513. Minimize the Maximum of Two Arrays](../../2501-3000/2513-minimize-the-maximum-of-two-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/)
