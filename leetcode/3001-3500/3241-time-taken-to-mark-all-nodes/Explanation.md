# LeetCode 3241: Time Taken to Mark All Nodes

**LeetCode Problem #3241 — Time Taken to Mark All Nodes**
Solve LeetCode Time Taken to Mark All Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Time Taken to Mark All Nodes |
| LeetCode | #3241 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There exists an **undirected** tree with `n` nodes numbered `0` to `n - 1`. You are given a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the tree.

Initially, **all** nodes are **unmarked**. For each node `i`:

If `i` is odd, the node will get marked at time `x` if there is **at least** one node *adjacent* to it which was marked at time `x - 1`. 
 If `i` is even, the node will get marked at time `x` if there is **at least** one node *adjacent* to it which was marked at time `x - 2`.

Return an array `times` where `times[i]` is the time when all nodes get marked in the tree, if you mark node `i` at time `t = 0`.

**Note** that the answer for each `times[i]` is **independent**, i.e. when you mark node `i` all other nodes are *unmarked*.

## Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= edges[i][0], edges[i][1] <= n - 1`
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[0,1],[0,2]]`
- **Output:** `[2,4,3]`
- **Explanation:** For `i = 0`:

 
 Node 1 is marked at `t = 1`, and Node 2 at `t = 2`. 
 
 
 For `i = 1`:
 
 Node 0 is marked at `t = 2`, and Node 2 at `t = 4`. 
 
 
 For `i = 2`:
 
 Node 0 is marked at `t = 2`, and Node 1 at `t = 3`.

### Example 2
- **Input:** `edges = [[0,1]]`
- **Output:** `[1,2]`
- **Explanation:** For `i = 0`:

 
 Node 1 is marked at `t = 1`. 
 
 
 For `i = 1`:
 
 Node 0 is marked at `t = 2`.

### Example 3
- **Input:** `edges = [[2,4],[0,1],[2,3],[0,2]]`
- **Output:** `[4,6,3,5,5]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Time Taken to Mark All Nodes**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1],[0,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,4,3]`.
4. **Verification:** For `i = 0`:

 
 Node 1 is marked at `t = 1`, and Node 2 at `t = 2`. 
 
 
 For `i = 1`:
 
 Node 0 is marked at `t = 2`, and Node 2 at `t = 4`. 
 
 
 For `i = 2`:
 
 Node 0 is marked at `t = 2`, and Node 1 at `t = 3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var timeTaken = function(edges) {
    const n = edges.length + 1;

    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const cost = (node) => node % 2 === 0 ? 2 : 1;

    const parent = new Array(n).fill(-1);
    const order = [0];

    // First traversal: establish parent-child relationships.
    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const v of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            order.push(v);
        }
    }

    // down[u]: maximum time from u to a node in its subtree.
    const down = new Array(n).fill(0);

    // Process nodes in reverse order (children before parents).
    for (let i = n - 1; i >= 0; i--) {
        const u = order[i];

        for (const v of graph[u]) {
            if (parent[v] === u) {
                down[u] = Math.max(
                    down[u],
                    cost(v) + down[v]
                );
            }
        }
    }

    // up[u]: maximum time from u to a node outside its subtree.
    const up = new Array(n).fill(0);

    const answer = new Array(n);

    // Process parents before children.
    for (const u of order) {
        let best1 = 0;
        let best2 = 0;
        let bestChild = -1;

        // Find the two largest child contributions.
        for (const v of graph[u]) {
            if (parent[v] !== u) continue;

            const value = cost(v) + down[v];

            if (value > best1) {
                best2 = best1;
                best1 = value;
                bestChild = v;
            } else if (value > best2) {
                best2 = value;
            }
        }

        answer[u] = Math.max(down[u], up[u]);

        // Calculate up values for each child.
        for (const v of graph[u]) {
            if (parent[v] !== u) continue;

            // Best path from u that does not enter v's subtree.
            const bestOther = (v === bestChild) ? best2 : best1;

            up[v] = cost(u) + Math.max(up[u], bestOther);
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0847-shortest-path-visiting-all-nodes/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0863-all-nodes-distance-k-in-binary-tree/)
- [865. Smallest Subtree with all the Deepest Nodes](../../0501-1000/0865-smallest-subtree-with-all-the-deepest-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/time-taken-to-mark-all-nodes/)
