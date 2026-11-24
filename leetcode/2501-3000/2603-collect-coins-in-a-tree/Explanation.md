# LeetCode 2603: Collect Coins in a Tree

**LeetCode Problem #2603 — Collect Coins in a Tree**
Solve LeetCode Collect Coins in a Tree using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Collect Coins in a Tree |
| LeetCode | #2603 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There exists an undirected and unrooted tree with `n` nodes indexed from `0` to `n - 1`. You are given an integer `n` and a 2D integer array edges of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree. You are also given an array `coins` of size `n` where `coins[i]` can be either `0` or `1`, where `1` indicates the presence of a coin in the vertex `i`.

Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times:

Collect all the coins that are at a distance of at most `2` from the current vertex, or 
 Move to any adjacent vertex in the tree.

Find *the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex*.

Note that if you pass an edge several times, you need to count it into the answer several times.

## Constraints
- `n == coins.length`
- `1 <= n <= 3 * 10^4`
- `0 <= coins[i] <= 1`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]`
- **Output:** `2`
- **Explanation:** Start at vertex 2, collect the coin at vertex 0, move to vertex 3, collect the coin at vertex 5 then move back to vertex 2.

### Example 2
- **Input:** `coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]`
- **Output:** `2`
- **Explanation:** Start at vertex 0, collect the coins at vertices 4 and 3, move to vertex 2, collect the coin at vertex 7, then move back to vertex 0.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Collect Coins in a Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Start at vertex 2, collect the coin at vertex 0, move to vertex 3, collect the coin at vertex 5 then move back to vertex 2.

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
/**
 * @param {number[]} coins
 * @param {number[][]} edges
 * @return {number}
 */
var collectTheCoins = function (coins, edges) {
    const n = coins.length;
    const adj = Array.from({ length: n }, () => []);
    const deg = new Int32Array(n);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
        deg[a]++;
        deg[b]++;
    }

    const removed = new Uint8Array(n);
    let remaining = n;

    // Stage 1: strip coinless leaves
    let q = [];
    for (let i = 0; i < n; i++) if (deg[i] <= 1 && coins[i] === 0) q.push(i);
    let head = 0;
    while (head < q.length) {
        const u = q[head++];
        if (removed[u]) continue;
        removed[u] = 1;
        remaining--;
        for (const v of adj[u]) {
            if (removed[v]) continue;
            if (--deg[v] <= 1 && coins[v] === 0) q.push(v);
        }
    }

    // Stage 2: peel two layers of leaves
    for (let round = 0; round < 2; round++) {
        const leaves = [];
        for (let i = 0; i < n; i++) if (!removed[i] && deg[i] <= 1) leaves.push(i);
        for (const u of leaves) {
            removed[u] = 1;
            remaining--;
            for (const v of adj[u]) if (!removed[v]) deg[v]--;
        }
    }

    return remaining <= 1 ? 0 : 2 * (remaining - 1);
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
- [1443. Minimum Time to Collect All Apples in a Tree](../../1001-1500/1443-minimum-time-to-collect-all-apples-in-a-tree/)
- [979. Distribute Coins in Binary Tree](../../0501-1000/0979-distribute-coins-in-binary-tree/)
- [2869. Minimum Operations to Collect Elements](../../2501-3000/2869-minimum-operations-to-collect-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/collect-coins-in-a-tree/)
