# LeetCode 3203: Find Minimum Diameter After Merging Two Trees

**LeetCode Problem #3203 — Find Minimum Diameter After Merging Two Trees**
Solve LeetCode Find Minimum Diameter After Merging Two Trees using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Minimum Diameter After Merging Two Trees |
| LeetCode | #3203 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There exist two **undirected **trees with `n` and `m` nodes, numbered from `0` to `n - 1` and from `0` to `m - 1`, respectively. You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the first tree and `edges2[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the **minimum **possible **diameter **of the resulting tree.

The **diameter** of a tree is the length of the *longest* path between any two nodes in the tree.

## Constraints
- `1 <= n, m <= 10^5`
- `edges1.length == n - 1`
- `edges2.length == m - 1`
- `edges1[i].length == edges2[i].length == 2`
- `edges1[i] = [a_i, b_i]`
- `0 <= a_i, b_i < n`
- `edges2[i] = [u_i, v_i]`
- `0 <= u_i, v_i < m`
- The input is generated such that `edges1` and `edges2` represent valid trees.

## Examples
### Example 1
- **Input:** `edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]`
- **Output:** `3`
- **Explanation:** We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

### Example 2
- **Input:** `edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]`
- **Output:** `5`
- **Explanation:** We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Minimum Diameter After Merging Two Trees**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

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
var minimumDiameterAfterMerge = function(edges1, edges2) {

    function findDiameter(edges) {
        const n = edges.length + 1;

        const graph = Array.from({ length: n }, () => []);

        for (const [u, v] of edges) {
            graph[u].push(v);
            graph[v].push(u);
        }

        // BFS to find the farthest node.
        function bfs(start) {
            const dist = new Array(n).fill(-1);
            const queue = [start];

            dist[start] = 0;
            let head = 0;
            let farthest = start;

            while (head < queue.length) {
                const u = queue[head++];

                if (dist[u] > dist[farthest]) {
                    farthest = u;
                }

                for (const v of graph[u]) {
                    if (dist[v] === -1) {
                        dist[v] = dist[u] + 1;
                        queue.push(v);
                    }
                }
            }

            return [farthest, dist[farthest]];
        }

        // First BFS: find one endpoint of the diameter.
        const [endpoint] = bfs(0);

        // Second BFS: find the diameter.
        const [, diameter] = bfs(endpoint);

        return diameter;
    }

    const d1 = findDiameter(edges1);
    const d2 = findDiameter(edges2);

    const radius1 = Math.ceil(d1 / 2);
    const radius2 = Math.ceil(d2 / 2);

    return Math.max(
        d1,
        d2,
        radius1 + radius2 + 1
    );
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
- [2918. Minimum Equal Sum of Two Arrays After Replacing Zeros](../../2501-3000/2918-minimum-equal-sum-of-two-arrays-after-replacing-zeros/)
- [310. Minimum Height Trees](../../0001-0500/0310-minimum-height-trees/)
- [558. Logical OR of Two Binary Grids Represented as Quad-Trees](../../0501-1000/0558-logical-or-of-two-binary-grids-represented-as-quad-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/)
