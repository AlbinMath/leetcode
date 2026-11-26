# LeetCode 1761: Minimum Degree of a Connected Trio in a Graph

**LeetCode Problem #1761 — Minimum Degree of a Connected Trio in a Graph**
Solve LeetCode Minimum Degree of a Connected Trio in a Graph using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Degree of a Connected Trio in a Graph |
| LeetCode | #1761 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an undirected graph. You are given an integer `n` which is the number of nodes in the graph and an array `edges`, where each `edges[i] = [u_i, v_i]` indicates that there is an undirected edge between `u_i` and `v_i`.

A **connected trio** is a set of **three** nodes where there is an edge between every pair of them.

The **degree of a connected trio** is the number of edges where one endpoint is in the trio, and the other is not.

Return *the **minimum** degree of a connected trio in the graph, or* `-1` *if the graph has no connected trios.*

## Constraints
- `2 <= n <= 400`
- `edges[i].length == 2`
- `1 <= edges.length <= n * (n-1) / 2`
- `1 <= u_i, v_i <= n`
- `u_i != v_i`
- There are no repeated edges.

## Examples
### Example 1
- **Input:** `n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]`
- **Output:** `3`
- **Explanation:** There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.

### Example 2
- **Input:** `n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]`
- **Output:** `0`
- **Explanation:** There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Minimum Degree of a Connected Trio in a Graph**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.

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
var minTrioDegree = function(n, edges) {
    // Build adjacency matrix
    const graph = Array.from(
        { length: n + 1 },
        () => new Array(n + 1).fill(false)
    );

    // Count edges connected to each node
    const degree = new Array(n + 1).fill(0);

    for (const [u, v] of edges) {
        graph[u][v] = true;
        graph[v][u] = true;

        degree[u]++;
        degree[v]++;
    }

    let minDegree = Infinity;

    // Check every possible trio
    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {

            // First two nodes must be connected
            if (!graph[i][j]) continue;

            for (let k = j + 1; k <= n; k++) {

                // All three pairs must be connected
                if (graph[i][k] && graph[j][k]) {

                    // Remove the three internal edges
                    const trioDegree =
                        degree[i] + degree[j] + degree[k] - 6;

                    minDegree = Math.min(
                        minDegree,
                        trioDegree
                    );
                }
            }
        }
    }

    return minDegree === Infinity ? -1 : minDegree;
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
- [3108. Minimum Cost Walk in Weighted Graph](../../3001-3500/3108-minimum-cost-walk-in-weighted-graph/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../../3501-4000/3604-minimum-time-to-reach-destination-in-directed-graph/)
- [3608. Minimum Time for K Connected Components](../../3501-4000/3608-minimum-time-for-k-connected-components/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/)
