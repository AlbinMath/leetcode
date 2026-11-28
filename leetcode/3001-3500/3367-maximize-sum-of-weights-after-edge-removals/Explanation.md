# LeetCode 3367: Maximize Sum of Weights after Edge Removals

**LeetCode Problem #3367 — Maximize Sum of Weights after Edge Removals**
Solve LeetCode Maximize Sum of Weights after Edge Removals using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Sum of Weights after Edge Removals |
| LeetCode | #3367 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There exists an **undirected** tree with `n` nodes numbered `0` to `n - 1`. You are given a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates that there is an edge between nodes `u_i` and `v_i` with weight `w_i` in the tree.

Your task is to remove *zero or more* edges such that:

Each node has an edge with **at most** `k` other nodes, where `k` is given. 
 The sum of the weights of the remaining edges is **maximized**.

Return the **maximum **possible sum of weights for the remaining edges after making the necessary removals.

## Constraints
- `2 <= n <= 10^5`
- `1 <= k <= n - 1`
- `edges.length == n - 1`
- `edges[i].length == 3`
- ` 0 <= edges[i][0] <= n - 1 `
- ` 0 <= edges[i][1] <= n - 1 `
- ` 1 <= edges[i][2] <= 10^6 `
- The input is generated such that `edges` form a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[0,1,4],[0,2,2],[2,3,12],[2,4,6]], k = 2`
- **Output:** `22`
- **Explanation:** Node 2 has edges with 3 other nodes. We remove the edge `[0, 2, 2]`, ensuring that no node has edges with more than `k = 2` nodes. 
 The sum of weights is 22, and we can't achieve a greater sum. Thus, the answer is 22.

### Example 2
- **Input:** `edges = [[0,1,5],[1,2,10],[0,3,15],[3,4,20],[3,5,5],[0,6,10]], k = 3`
- **Output:** `65`
- **Explanation:** Since no node has edges connecting it to more than `k = 3` nodes, we don't remove any edges. 
 The sum of weights is 65. Thus, the answer is 65.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Sum of Weights after Edge Removals**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1,4],[0,2,2],[2,3,12],[2,4,6]], k = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `22`.
4. **Verification:** Node 2 has edges with 3 other nodes. We remove the edge `[0, 2, 2]`, ensuring that no node has edges with more than `k = 2` nodes. 
 The sum of weights is 22, and we can't achieve a greater sum. Thus, the answer is 22.

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
var maximizeSumOfWeights = function(edges, k) {
    const n = edges.length + 1;

    const graph = Array.from({ length: n }, () => []);

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }

    const parent = new Array(n).fill(-1);
    const parentWeight = new Array(n).fill(0);

    const order = [0];
    parent[0] = 0;

    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const [v, w] of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            parentWeight[v] = w;

            order.push(v);
        }
    }

    const dp0 = new Array(n).fill(0);
    const dp1 = new Array(n).fill(0);

    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];

        let base = 0;
        const gains = [];

        for (const [v, w] of graph[u]) {
            if (parent[v] !== u) continue;

            base += dp0[v];

            const gain = w + dp1[v] - dp0[v];

            if (gain > 0) {
                gains.push(gain);
            }
        }

        gains.sort((a, b) => b - a);

        dp0[u] = base;

        for (let j = 0; j < Math.min(k, gains.length); j++) {
            dp0[u] += gains[j];
        }

        dp1[u] = base;

        for (let j = 0; j < Math.min(k - 1, gains.length); j++) {
            dp1[u] += gains[j];
        }
    }

    return dp0[0];
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
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1005-maximize-sum-of-array-after-k-negations/)
- [2382. Maximum Segment Sum After Removals](../../2001-2500/2382-maximum-segment-sum-after-removals/)
- [3410. Maximize Subarray Sum After Removing All Occurrences of One Element](../../3001-3500/3410-maximize-subarray-sum-after-removing-all-occurrences-of-one-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/)
