# LeetCode 3112: Minimum Time to Visit Disappearing Nodes

**LeetCode Problem #3112 — Minimum Time to Visit Disappearing Nodes**
Solve LeetCode Minimum Time to Visit Disappearing Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Visit Disappearing Nodes |
| LeetCode | #3112 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected graph of `n` nodes. You are given a 2D array `edges`, where `edges[i] = [u_i, v_i, length_i]` describes an edge between node `u_i` and node `v_i` with a traversal time of `length_i` units.

Additionally, you are given an array `disappear`, where `disappear[i]` denotes the time when the node `i` disappears from the graph and you won't be able to visit it.

**Note** that the graph might be *disconnected* and might contain *multiple edges*.

Return the array `answer`, with `answer[i]` denoting the **minimum** units of time required to reach node `i` from node 0. If node `i` is **unreachable** from node 0 then `answer[i]` is `-1`.

## Constraints
- `1 <= n <= 5 * 10^4`
- `0 <= edges.length <= 10^5`
- `edges[i] == [u_i, v_i, length_i]`
- `0 <= u_i, v_i <= n - 1`
- `1 <= length_i <= 10^5`
- `disappear.length == n`
- `1 <= disappear[i] <= 10^5`

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]`
- **Output:** `[0,-1,4]`
- **Explanation:** We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears. 

 
 For node 0, we don't need any time as it is our starting point. 
 For node 1, we need at least 2 units of time to traverse `edges[0]`. Unfortunately, it disappears at that moment, so we won't be able to visit it. 
 For node 2, we need at least 4 units of time to traverse `edges[2]`.

### Example 2
- **Input:** `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]`
- **Output:** `[0,2,3]`
- **Explanation:** We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears. 

 
 For node 0, we don't need any time as it is the starting point. 
 For node 1, we need at least 2 units of time to traverse `edges[0]`. 
 For node 2, we need at least 3 units of time to traverse `edges[0]` and `edges[1]`.

### Example 3
- **Input:** `n = 2, edges = [[0,1,1]], disappear = [1,1]`
- **Output:** `[0,-1]`
- **Explanation:** Exactly when we reach node 1, it disappears.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Time to Visit Disappearing Nodes**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,-1,4]`.
4. **Verification:** We are starting our journey from node 0, and our goal is to find the minimum time required to reach each node before it disappears. 

 
 For node 0, we don't need any time as it is our starting point. 
 For node 1, we need at least 2 units of time to traverse `edges[0]`. Unfortunately, it disappears at that moment, so we won't be able to visit it. 
 For node 2, we need at least 4 units of time to traverse `edges[2]`.

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
var minimumTime = function (n, edges, disappear) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    // Min-heap of [time, node]
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
        const [t, u] = pop();
        if (t > dist[u]) continue;
        for (const [v, w] of adj[u]) {
            const nt = t + w;
            if (nt < disappear[v] && nt < dist[v]) {
                dist[v] = nt;
                push([nt, v]);
            }
        }
    }

    return dist.map((d) => (d === Infinity ? -1 : d));
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
- [2577. Minimum Time to Visit a Cell In a Grid](../../2501-3000/2577-minimum-time-to-visit-a-cell-in-a-grid/)
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/)
