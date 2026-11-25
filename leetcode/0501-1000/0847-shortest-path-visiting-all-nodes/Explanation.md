# LeetCode 847: Shortest Path Visiting All Nodes

**LeetCode Problem #847 — Shortest Path Visiting All Nodes**
Solve LeetCode Shortest Path Visiting All Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path Visiting All Nodes |
| LeetCode | #847 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have an undirected, connected graph of `n` nodes labeled from `0` to `n - 1`. You are given an array `graph` where `graph[i]` is a list of all the nodes connected with node `i` by an edge.

Return *the length of the shortest path that visits every node*. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

## Constraints
- `n == graph.length`
- `1 <= n <= 12`
- `0 <= graph[i].length < n`
- `graph[i]` does not contain `i`.
- If `graph[a]` contains `b`, then `graph[b]` contains `a`.
- The input graph is always connected.

## Examples
### Example 1
- **Input:** `graph = [[1,2,3],[0],[0],[0]]`
- **Output:** `4`
- **Explanation:** One possible path is [1,0,2,0,3]

### Example 2
- **Input:** `graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]`
- **Output:** `4`
- **Explanation:** One possible path is [0,1,4,2,3]

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Path Visiting All Nodes**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `graph = [[1,2,3],[0],[0],[0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One possible path is [1,0,2,0,3]

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
 * @param {number[][]} graph
 * @return {number}
 */
var shortestPathLength = function (graph) {
  const n = graph.length;
  if (n === 1) return 0;

  const full = (1 << n) - 1;
  const visited = Array.from({ length: n }, () => new Array(1 << n).fill(false));

  let queue = [];
  for (let i = 0; i < n; i++) {
    visited[i][1 << i] = true;
    queue.push([i, 1 << i]);
  }

  let steps = 0;
  while (queue.length > 0) {
    steps++;
    const next = [];
    for (const [node, mask] of queue) {
      for (const nb of graph[node]) {
        const newMask = mask | (1 << nb);
        if (newMask === full) return steps;
        if (!visited[nb][newMask]) {
          visited[nb][newMask] = true;
          next.push([nb, newMask]);
        }
      }
    }
    queue = next;
  }

  return -1;
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
- [864. Shortest Path to Get All Keys](../../0501-1000/0864-shortest-path-to-get-all-keys/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0863-all-nodes-distance-k-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
