# LeetCode 2973: Find Number of Coins to Place in Tree Nodes

**LeetCode Problem #2973 — Find Number of Coins to Place in Tree Nodes**
Solve LeetCode Find Number of Coins to Place in Tree Nodes using JavaScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Number of Coins to Place in Tree Nodes |
| LeetCode | #2973 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an **undirected** tree with `n` nodes labeled from `0` to `n - 1`, and rooted at node `0`. You are given a 2D integer array `edges` of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

You are also given a **0-indexed** integer array `cost` of length `n`, where `cost[i]` is the **cost** assigned to the `i^th` node.

You need to place some coins on every node of the tree. The number of coins to be placed at node `i` can be calculated as:

If size of the subtree of node `i` is less than `3`, place `1` coin. 
 Otherwise, place an amount of coins equal to the **maximum** product of cost values assigned to `3` distinct nodes in the subtree of node `i`. If this product is **negative**, place `0` coins.

Return *an array *`coin`* of size *`n`* such that *`coin[i]`* is the number of coins placed at node *`i`*.*

## Constraints
- `2 <= n <= 2 * 10^4`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `cost.length == n`
- `1 <= |cost[i]| <= 10^4`
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]`
- **Output:** `[120,1,1,1,1,1]`
- **Explanation:** For node 0 place 6 * 5 * 4 = 120 coins. All other nodes are leaves with subtree of size 1, place 1 coin on each of them.

### Example 2
- **Input:** `edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]`
- **Output:** `[280,140,32,1,1,1,1,1,1]`
- **Explanation:** The coins placed on each node are:
- Place 8 * 7 * 5 = 280 coins on node 0.
- Place 7 * 5 * 4 = 140 coins on node 1.
- Place 8 * 2 * 2 = 32 coins on node 2.
- All other nodes are leaves with subtree of size 1, place 1 coin on each of them.

### Example 3
- **Input:** `edges = [[0,1],[0,2]], cost = [1,2,-2]`
- **Output:** `[0,1,1]`
- **Explanation:** Node 1 and 2 are leaves with subtree of size 1, place 1 coin on each of them. For node 0 the only possible product of cost is 2 * 1 * -2 = -4. Hence place 0 coins on node 0.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Number of Coins to Place in Tree Nodes**, we observe the problem requirements and utilize the **Linked List** technique. We iterate through the inputs using **Pointer Traversal & Node Manipulation**, leveraging a **Linked List** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Linked List**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]`.
2. **Processing Steps:** We apply **Pointer Traversal & Node Manipulation** using our **Linked List**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[120,1,1,1,1,1]`.
4. **Verification:** For node 0 place 6 * 5 * 4 = 120 coins. All other nodes are leaves with subtree of size 1, place 1 coin on each of them.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List.

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var placedCoins = function(edges, cost) {
    const n = cost.length;

    const adj = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const parent = new Array(n).fill(-1);
    const order = [0];

    parent[0] = -2;

    for (let i = 0; i < order.length; i++) {
        const node = order[i];

        for (const child of adj[node]) {
            if (child === parent[node]) continue;

            parent[child] = node;
            order.push(child);
        }
    }

    const size = new Array(n).fill(1);
    const extremes = Array.from({ length: n }, () => []);
    const coins = new Array(n).fill(1);

    for (let i = n - 1; i >= 0; i--) {
        const node = order[i];

        const values = [cost[node]];

        for (const child of adj[node]) {
            if (parent[child] !== node) continue;

            size[node] += size[child];
            values.push(...extremes[child]);
        }

        values.sort((a, b) => a - b);

        if (values.length > 5) {
            extremes[node] = [
                values[0],
                values[1],
                ...values.slice(-3)
            ];
        } else {
            extremes[node] = values;
        }

        if (size[node] < 3) {
            coins[node] = 1;
            continue;
        }

        const len = extremes[node].length;

        const product1 =
            extremes[node][len - 1] *
            extremes[node][len - 2] *
            extremes[node][len - 3];

        const product2 =
            extremes[node][0] *
            extremes[node][1] *
            extremes[node][len - 1];

        coins[node] = Math.max(0, product1, product2);
    }

    return coins;
};
```

## Why This Works
By utilizing **Linked List**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1519. Number of Nodes in the Sub-Tree With the Same Label](../../1501-2000/1519-number-of-nodes-in-the-sub-tree-with-the-same-label/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [3025. Find the Number of Ways to Place People I](../../3001-3500/3025-find-the-number-of-ways-to-place-people-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/)
