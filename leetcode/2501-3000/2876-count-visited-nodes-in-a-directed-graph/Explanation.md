# LeetCode 2876: Count Visited Nodes in a Directed Graph

**LeetCode Problem #2876 — Count Visited Nodes in a Directed Graph**
Solve LeetCode Count Visited Nodes in a Directed Graph using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Visited Nodes in a Directed Graph |
| LeetCode | #2876 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a **directed** graph consisting of `n` nodes numbered from `0` to `n - 1` and `n` directed edges.

You are given a **0-indexed** array `edges` where `edges[i]` indicates that there is an edge from node `i` to node `edges[i]`.

Consider the following process on the graph:

You start from a node `x` and keep visiting other nodes through edges until you reach a node that you have already visited before on this **same** process.

Return *an array *`answer`* where *`answer[i]`* is the number of **different** nodes that you will visit if you perform the process starting from node *`i`.

## Constraints
- `n == edges.length`
- `2 <= n <= 10^5`
- `0 <= edges[i] <= n - 1`
- `edges[i] != i`

## Examples
### Example 1
- **Input:** `edges = [1,2,0,0]`
- **Output:** `[3,3,3,4]`
- **Explanation:** We perform the process starting from each node in the following way:
- Starting from node 0, we visit the nodes 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 3.
- Starting from node 1, we visit the nodes 1 -> 2 -> 0 -> 1. The number of different nodes we visit is 3.
- Starting from node 2, we visit the nodes 2 -> 0 -> 1 -> 2. The number of different nodes we visit is 3.
- Starting from node 3, we visit the nodes 3 -> 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 4.

### Example 2
- **Input:** `edges = [1,2,3,4,0]`
- **Output:** `[5,5,5,5,5]`
- **Explanation:** Starting from any node we can visit every node in the graph in the process.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Visited Nodes in a Directed Graph**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [1,2,0,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,3,3,4]`.
4. **Verification:** We perform the process starting from each node in the following way:
- Starting from node 0, we visit the nodes 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 3.
- Starting from node 1, we visit the nodes 1 -> 2 -> 0 -> 1. The number of different nodes we visit is 3.
- Starting from node 2, we visit the nodes 2 -> 0 -> 1 -> 2. The number of different nodes we visit is 3.
- Starting from node 3, we visit the nodes 3 -> 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 4.

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
 * @param {number[]} edges
 * @return {number[]}
 */
var countVisitedNodes = function (edges) {
    const n = edges.length;
    const indeg = new Int32Array(n);
    for (let i = 0; i < n; i++) indeg[edges[i]]++;

    const order = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) order.push(i);
    let head = 0;
    while (head < order.length) {
        const u = order[head++];
        const v = edges[u];
        if (--indeg[v] === 0) order.push(v);
    }

    const ans = new Array(n).fill(0);
    const done = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0 || done[i]) continue; // tree node or already handled cycle node
        let len = 0, cur = i;
        do {
            done[cur] = 1;
            len++;
            cur = edges[cur];
        } while (cur !== i);
        do {
            ans[cur] = len;
            cur = edges[cur];
        } while (cur !== i);
    }

    for (let k = order.length - 1; k >= 0; k--) {
        const u = order[k];
        ans[u] = ans[edges[u]] + 1;
    }
    return ans;
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
- [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](../../2001-2500/2316-count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
- [1857. Largest Color Value in a Directed Graph](../../1501-2000/1857-largest-color-value-in-a-directed-graph/)
- [2192. All Ancestors of a Node in a Directed Acyclic Graph](../../2001-2500/2192-all-ancestors-of-a-node-in-a-directed-acyclic-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/)
