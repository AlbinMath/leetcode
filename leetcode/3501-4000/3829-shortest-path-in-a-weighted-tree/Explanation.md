# LeetCode 3515: Shortest Path in a Weighted Tree

**LeetCode Problem #3515 — Shortest Path in a Weighted Tree**
Solve LeetCode Shortest Path in a Weighted Tree using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path in a Weighted Tree |
| LeetCode | #3515 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` and an undirected, weighted tree rooted at node 1 with `n` nodes numbered from 1 to `n`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates an undirected edge from node `u_i` to `v_i` with weight `w_i`.

You are also given a 2D integer array `queries` of length `q`, where each `queries[i]` is either:

`[1, u, v, w']` &ndash; **Update** the weight of the edge between nodes `u` and `v` to `w'`, where `(u, v)` is guaranteed to be an edge present in `edges`. 
 `[2, x]` &ndash; **Compute** the **shortest** path distance from the root node 1 to node `x`.

Return an integer array `answer`, where `answer[i]` is the **shortest** path distance from node 1 to `x` for the `i^th` query of `[2, x]`.

## Constraints
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] == [u_i, v_i, w_i]`
- `1 <= u_i, v_i <= n`
- `1 <= w_i <= 10^4`
- The input is generated such that `edges` represents a valid tree.
- `1 <= queries.length == q <= 10^5`
- `queries[i].length == 2` or `4`
 
 `queries[i] == [1, u, v, w']` or,
- `queries[i] == [2, x]`
- `1 <= u, v, x <= n`
- `(u, v)` is always an edge from `edges`.
- `1 <= w' <= 10^4`

## Examples
### Example 1
- **Input:** `n = 2, edges = [[1,2,7]], queries = [[2,2],[1,1,2,4],[2,2]]`
- **Output:** `[7,4]`
- **Explanation:** Query `[2, 2]`: The shortest path from root node 1 to node 2 is 7. 
 Query `[1, 1, 2, 4]`: The weight of edge `(1, 2)` changes from 7 to 4. 
 Query `[2, 2]`: The shortest path from root node 1 to node 2 is 4.

### Example 2
- **Input:** `n = 3, edges = [[1,2,2],[1,3,4]], queries = [[2,1],[2,3],[1,1,3,7],[2,2],[2,3]]`
- **Output:** `[0,4,2,7]`
- **Explanation:** Query `[2, 1]`: The shortest path from root node 1 to node 1 is 0. 
 Query `[2, 3]`: The shortest path from root node 1 to node 3 is 4. 
 Query `[1, 1, 3, 7]`: The weight of edge `(1, 3)` changes from 4 to 7. 
 Query `[2, 2]`: The shortest path from root node 1 to node 2 is 2. 
 Query `[2, 3]`: The shortest path from root node 1 to node 3 is 7.

### Example 3
- **Input:** `n = 4, edges = [[1,2,2],[2,3,1],[3,4,5]], queries = [[2,4],[2,3],[1,2,3,3],[2,2],[2,3]]`
- **Output:** `[8,3,2,5]`
- **Explanation:** Query `[2, 4]`: The shortest path from root node 1 to node 4 consists of edges `(1, 2)`, `(2, 3)`, and `(3, 4)` with weights `2 + 1 + 5 = 8`. 
 Query `[2, 3]`: The shortest path from root node 1 to node 3 consists of edges `(1, 2)` and `(2, 3)` with weights `2 + 1 = 3`. 
 Query `[1, 2, 3, 3]`: The weight of edge `(2, 3)` changes from 1 to 3. 
 Query `[2, 2]`: The shortest path from root node 1 to node 2 is 2. 
 Query `[2, 3]`: The shortest path from root node 1 to node 3 consists of edges `(1, 2)` and `(2, 3)` with updated weights `2 + 3 = 5`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Shortest Path in a Weighted Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, edges = [[1,2,7]], queries = [[2,2],[1,1,2,4],[2,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[7,4]`.
4. **Verification:** Query `[2, 2]`: The shortest path from root node 1 to node 2 is 7. 
 Query `[1, 1, 2, 4]`: The weight of edge `(1, 2)` changes from 7 to 4. 
 Query `[2, 2]`: The shortest path from root node 1 to node 2 is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var treeQueries = function(n, edges, queries) {
    const adj = Array.from({ length: n + 1 }, () => []);
    const edgeMap = new Map();

    for (let i = 0; i < edges.length; i++) {
        const [u, v, w] = edges[i];

        adj[u].push([v, w, i]);
        adj[v].push([u, w, i]);

        const key = `${Math.min(u, v)},${Math.max(u, v)}`;
        edgeMap.set(key, i);
    }

    const tin = new Array(n + 1).fill(0);
    const tout = new Array(n + 1).fill(0);
    const dist = new Array(n + 1).fill(0);
    const edgeChild = new Array(n - 1).fill(0);
    const edgeWeight = edges.map(e => e[2]);

    // Iterative DFS: safe for a tree of depth 100000.
    let timer = 0;
    const stack = [[1, 0, 0]];

    while (stack.length) {
        const [u, p, state] = stack.pop();

        if (state === 0) {
            tin[u] = timer++;
            stack.push([u, p, 1]);

            for (let i = adj[u].length - 1; i >= 0; i--) {
                const [v, w, id] = adj[u][i];

                if (v === p) continue;

                dist[v] = dist[u] + w;
                edgeChild[id] = v;
                stack.push([v, u, 0]);
            }
        } else {
            tout[u] = timer - 1;
        }
    }

    // Fenwick tree for subtree range additions.
    const bit = new Array(n + 2).fill(0);

    function add(index, delta) {
        for (let i = index + 1; i <= n + 1; i += i & -i) {
            bit[i] += delta;
        }
    }

    function prefix(index) {
        let sum = 0;

        for (let i = index + 1; i > 0; i -= i & -i) {
            sum += bit[i];
        }

        return sum;
    }

    const answer = [];

    for (const query of queries) {
        if (query[0] === 1) {
            const [, u, v, newWeight] = query;
            const key = `${Math.min(u, v)},${Math.max(u, v)}`;
            const id = edgeMap.get(key);

            const delta = newWeight - edgeWeight[id];
            edgeWeight[id] = newWeight;

            const child = edgeChild[id];

            // Update all root distances in this child's subtree.
            add(tin[child], delta);
            add(tout[child] + 1, -delta);
        } else {
            const x = query[1];
            answer.push(dist[x] + prefix(tin[x]));
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [1104. Path In Zigzag Labelled Binary Tree](../../1001-1500/1194-path-in-zigzag-labelled-binary-tree/)
- [1372. Longest ZigZag Path in a Binary Tree](../../1001-1500/1474-longest-zigzag-path-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-in-a-weighted-tree/)
