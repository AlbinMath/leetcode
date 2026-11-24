# LeetCode 1971: Find if Path Exists in Graph

**LeetCode Problem #1971 — Find if Path Exists in Graph**
Solve LeetCode Find if Path Exists in Graph using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find if Path Exists in Graph |
| LeetCode | #1971 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u_i, v_i]` denotes a bi-directional edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true`* if there is a **valid path** from *`source`* to *`destination`*, or *`false`* otherwise**.*

## Constraints
- `1 <= n <= 2 * 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `edges[i].length == 2`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `0 <= source, destination <= n - 1`
- There are no duplicate edges.
- There are no self edges.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2`
- **Output:** `true`
- **Explanation:** There are two paths from vertex 0 to vertex 2:
- 0 &rarr; 1 &rarr; 2
- 0 &rarr; 2

### Example 2
- **Input:** `n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5`
- **Output:** `false`
- **Explanation:** There is no path from vertex 0 to vertex 5.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find if Path Exists in Graph**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** There are two paths from vertex 0 to vertex 2:
- 0 &rarr; 1 &rarr; 2
- 0 &rarr; 2

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var validPath = function(n, edges, source, destination) {
    const g = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        g[u].push(v);
        g[v].push(u);
    }

    const seen = new Set([source]);
    const q = [source];

    for (let i = 0; i < q.length; i++) {
        const u = q[i];

        if (u === destination) return true;

        for (const v of g[u]) {
            if (!seen.has(v)) {
                seen.add(v);
                q.push(v);
            }
        }
    }

    return false;
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1791. Find Center of Star Graph](../../1501-2000/1791-find-center-of-star-graph/)
- [2812. Find the Safest Path in a Grid](../../2501-3000/2812-find-the-safest-path-in-a-grid/)
- [3011. Find if Array Can Be Sorted](../../3001-3500/3011-find-if-array-can-be-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/)
