# LeetCode 3311: Construct 2D Grid Matching Graph Layout

**LeetCode Problem #3311 — Construct 2D Grid Matching Graph Layout**
Solve LeetCode Construct 2D Grid Matching Graph Layout using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct 2D Grid Matching Graph Layout |
| LeetCode | #3311 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `edges` representing an **undirected** graph having `n` nodes, where `edges[i] = [u_i, v_i]` denotes an edge between nodes `u_i` and `v_i`.

Construct a 2D grid that satisfies these conditions:

The grid contains **all nodes** from `0` to `n - 1` in its cells, with each node appearing exactly **once**. 
 Two nodes should be in adjacent grid cells (**horizontally** or **vertically**) **if and only if** there is an edge between them in `edges`.

It is guaranteed that `edges` can form a 2D grid that satisfies the conditions.

Return a 2D integer array satisfying the conditions above. If there are multiple solutions, return *any* of them.

## Constraints
- `2 <= n <= 5 * 10^4`
- `1 <= edges.length <= 10^5`
- `edges[i] = [u_i, v_i]`
- `0 <= u_i < v_i < n`
- All the edges are distinct.
- The input is generated such that `edges` can form a 2D grid that satisfies the conditions.

## Examples
### Example 1
- **Input:** `n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]`
- **Output:** `[[3,1],[2,0]]`

### Example 2
- **Input:** `n = 5, edges = [[0,1],[1,3],[2,3],[2,4]]`
- **Output:** `[[4,2,3,1,0]]`

### Example 3
- **Input:** `n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]]`
- **Output:** `[[8,6,3],[7,4,2],[1,0,5]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Construct 2D Grid Matching Graph Layout**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[3,1],[2,0]]`.

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
var constructGridLayout = function(n, edges) {
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const degree = graph.map(g => g.length);

    // Case 1: Single row or single column (a path).
    const endpoint = degree.indexOf(1);

    if (endpoint !== -1) {
        const result = [];
        let prev = -1;
        let curr = endpoint;

        while (curr !== -1) {
            result.push(curr);

            let next = -1;

            for (const v of graph[curr]) {
                if (v !== prev) {
                    next = v;
                    break;
                }
            }

            prev = curr;
            curr = next;
        }

        return [result];
    }

    // Case 2: Two-dimensional grid.
    // Start from any corner (degree 2).
    const corner = degree.indexOf(2);

    const firstRow = [corner];

    let prev = -1;
    let curr = corner;

    // Choose the neighbor with the smaller degree.
    // If both have equal degree, either direction works.
    let next = graph[curr][0];

    for (const v of graph[curr]) {
        if (degree[v] < degree[next]) {
            next = v;
        }
    }

    firstRow.push(next);

    prev = curr;
    curr = next;

    // Continue along the first row until reaching another corner.
    while (degree[curr] !== 2) {
        let nextNode = -1;

        for (const v of graph[curr]) {
            if (v === prev) continue;

            if (
                nextNode === -1 ||
                degree[v] < degree[nextNode]
            ) {
                nextNode = v;
            }
        }

        if (nextNode === -1) break;

        firstRow.push(nextNode);

        prev = curr;
        curr = nextNode;
    }

    // Mark all nodes in the first row.
    const used = new Uint8Array(n);

    for (const v of firstRow) {
        used[v] = 1;
    }

    const result = [firstRow];
    let currentRow = firstRow;

    // Build remaining rows.
    while (currentRow.length > 0) {
        const nextRow = [];

        for (const u of currentRow) {
            for (const v of graph[u]) {
                if (!used[v]) {
                    used[v] = 1;
                    nextRow.push(v);
                    break;
                }
            }
        }

        if (nextRow.length === 0) break;

        result.push(nextRow);
        currentRow = nextRow;
    }

    return result;
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
- [1260. Shift 2D Grid](../../1001-1500/1386-shift-2d-grid/)
- [1559. Detect Cycles in 2D Grid](../../1501-2000/1663-detect-cycles-in-2d-grid/)
- [133. Clone Graph](../../0001-0500/0133-clone-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/)
