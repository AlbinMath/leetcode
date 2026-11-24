# LeetCode 802: Find Eventual Safe States

**LeetCode Problem #802 — Find Eventual Safe States**
Solve LeetCode Find Eventual Safe States using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Eventual Safe States |
| LeetCode | #802 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`. The graph is represented by a **0-indexed** 2D integer array `graph` where `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in `graph[i]`.

A node is a **terminal node** if there are no outgoing edges. A node is a **safe node** if every possible path starting from that node leads to a **terminal node** (or another safe node).

Return *an array containing all the **safe nodes** of the graph*. The answer should be sorted in **ascending** order.

## Constraints
- `n == graph.length`
- `1 <= n <= 10^4`
- `0 <= graph[i].length <= n`
- `0 <= graph[i][j] <= n - 1`
- `graph[i]` is sorted in a strictly increasing order.
- The graph may contain self-loops.
- The number of edges in the graph will be in the range `[1, 4 * 10^4]`.

## Examples
### Example 1
- **Input:** `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`
- **Output:** `[2,4,5,6]`
- **Explanation:** The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

### Example 2
- **Input:** `graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]`
- **Output:** `[4]`
- **Explanation:** Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Eventual Safe States**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,4,5,6]`.
4. **Verification:** The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function (graph) {
    const n = graph.length;
    const rev = Array.from({ length: n }, () => []);
    const outDeg = new Array(n);

    for (let i = 0; i < n; i++) {
        outDeg[i] = graph[i].length;
        for (const j of graph[i]) rev[j].push(i);
    }

    const queue = [];
    for (let i = 0; i < n; i++) if (outDeg[i] === 0) queue.push(i);

    const safe = new Uint8Array(n);
    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        safe[u] = 1;
        for (const p of rev[u]) {
            if (--outDeg[p] === 0) queue.push(p);
        }
    }

    const res = [];
    for (let i = 0; i < n; i++) if (safe[i]) res.push(i);
    return res;
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3286. Find a Safe Walk Through a Grid](../../3001-3500/3286-find-a-safe-walk-through-a-grid/)
- [753. Cracking the Safe](../../0501-1000/0753-cracking-the-safe/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-eventual-safe-states/)
