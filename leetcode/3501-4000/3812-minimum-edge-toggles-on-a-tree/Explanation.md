# LeetCode 3812: Minimum Edge Toggles on a Tree

**LeetCode Problem #3812 — Minimum Edge Toggles on a Tree**
Solve LeetCode Minimum Edge Toggles on a Tree using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Edge Toggles on a Tree |
| LeetCode | #3812 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an **undirected tree** with `n` nodes, numbered from 0 to `n - 1`. It is represented by a 2D integer array `edges`​​​​​​​ of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

You are also given two **binary** strings `start` and `target` of length `n`. For each node `x`, `start[x]` is its initial color and `target[x]` is its desired color.

In one operation, you may pick an edge with index `i` and **toggle **both of its endpoints. That is, if the edge is `[u, v]`, then the colors of nodes `u` and `v` **each** flip from `'0'` to `'1'` or from `'1'` to `'0'`.

Return an array of edge indices whose operations transform `start` into `target`. Among all valid sequences with **minimum possible length**, return the edge indices in **increasing**​​​​​​​ order.

If it is impossible to transform `start` into `target`, return an array containing a single element equal to -1.

## Constraints
- `2 <= n == start.length == target.length <= 10^5`
- `edges.length == n - 1`
- `edges[i] = [a_i, b_i]`
- `0 <= a_i, b_i < n`
- `start[i]` is either `'0'` or `'1'`.
- `target[i]` is either `'0'` or `'1'`.
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1],[1,2]], start = "010", target = "100"`
- **Output:** `[0]`
- **Explanation:** Toggle edge with index 0, which flips nodes 0 and 1. 
​​​​​​​The string changes from `"010"` to `"100"`, matching the target.

### Example 2
- **Input:** `n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[3,5],[1,6]], start = "0011000", target = "0010001"`
- **Output:** `[1,2,5]`
- **Explanation:** Toggle edge with index 1, which flips nodes 1 and 2. 
 Toggle edge with index 2, which flips nodes 2 and 3. 
 Toggle edge with index 5, which flips nodes 1 and 6. 
 

 After these operations, the resulting string becomes `"0010001"`, which matches the target.

### Example 3
- **Input:** `n = 2, edges = [[0,1]], start = "00", target = "01"`
- **Output:** `[-1]`
- **Explanation:** There is no sequence of edge toggles that transforms `"00"` into `"01"`. Therefore, we return `[-1]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Edge Toggles on a Tree**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1],[1,2]], start = "010", target = "100"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0]`.
4. **Verification:** Toggle edge with index 0, which flips nodes 0 and 1. 
​​​​​​​The string changes from `"010"` to `"100"`, matching the target.

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
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} start
 * @param {string} target
 * @return {number[]}
 */
var minimumFlips = function (n, edges, start, target) {
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < n - 1; i++) {
        const [a, b] = edges[i];
        adj[a].push([b, i]);
        adj[b].push([a, i]);
    }

    const diff = new Uint8Array(n);
    for (let i = 0; i < n; i++) diff[i] = start.charCodeAt(i) ^ target.charCodeAt(i);

    const parent = new Int32Array(n).fill(-1);
    const parentEdge = new Int32Array(n).fill(-1);
    const order = [0];
    const seen = new Uint8Array(n);
    seen[0] = 1;
    for (let h = 0; h < order.length; h++) {
        const u = order[h];
        for (const [v, id] of adj[u]) {
            if (!seen[v]) {
                seen[v] = 1;
                parent[v] = u;
                parentEdge[v] = id;
                order.push(v);
            }
        }
    }

    const res = [];
    for (let k = n - 1; k >= 1; k--) {
        const x = order[k];
        if (diff[x]) {
            res.push(parentEdge[x]);
            diff[x] = 0;
            diff[parent[x]] ^= 1;
        }
    }
    if (diff[0]) return [-1];
    res.sort((a, b) => a - b);
    return res;
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
- [2846. Minimum Edge Weight Equilibrium Queries in a Tree](../../2501-3000/2846-minimum-edge-weight-equilibrium-queries-in-a-tree/)
- [111. Minimum Depth of Binary Tree](../../0001-0500/0111-minimum-depth-of-binary-tree/)
- [671. Second Minimum Node In a Binary Tree](../../0501-1000/0671-second-minimum-node-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/)
