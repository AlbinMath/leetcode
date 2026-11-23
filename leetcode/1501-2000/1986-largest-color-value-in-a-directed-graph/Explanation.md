# LeetCode 1857: Largest Color Value in a Directed Graph

**LeetCode Problem #1857 — Largest Color Value in a Directed Graph**
Solve LeetCode Largest Color Value in a Directed Graph using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Color Value in a Directed Graph |
| LeetCode | #1857 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a **directed graph** of `n` colored nodes and `m` edges. The nodes are numbered from `0` to `n - 1`.

You are given a string `colors` where `colors[i]` is a lowercase English letter representing the **color** of the `i^th` node in this graph (**0-indexed**). You are also given a 2D array `edges` where `edges[j] = [a_j, b_j]` indicates that there is a **directed edge** from node `a_j` to node `b_j`.

A valid **path** in the graph is a sequence of nodes `x_1 -> x_2 -> x_3 -> ... -> x_k` such that there is a directed edge from `x_i` to `x_i+1` for every `1 <= i < k`. The **color value** of the path is the number of nodes that are colored the **most frequently** occurring color along that path.

Return *the **largest color value** of any valid path in the given graph, or *`-1`* if the graph contains a cycle*.

## Constraints
- `n == colors.length`
- `m == edges.length`
- `1 <= n <= 10^5`
- `0 <= m <= 10^5`
- `colors` consists of lowercase English letters.
- `0 <= a_j, b_j < n`

## Examples
### Example 1
- **Input:** `colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]`
- **Output:** `3`
- **Explanation:** The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored `"a" (red in the above image)`.

### Example 2
- **Input:** `colors = "a", edges = [[0,0]]`
- **Output:** `-1`
- **Explanation:** There is a cycle from 0 to 0.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Largest Color Value in a Directed Graph**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored `"a" (red in the above image)`.

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
/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */
var largestPathValue = function (colors, edges) {
    const n = colors.length;
    const adj = Array.from({ length: n }, () => []);
    const indeg = new Int32Array(n);
    for (const [a, b] of edges) {
        adj[a].push(b);
        indeg[b]++;
    }

    const dp = new Int32Array(n * 26);
    const queue = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);

    let head = 0, ans = 0;
    while (head < queue.length) {
        const u = queue[head++];
        const cu = colors.charCodeAt(u) - 97;
        const val = ++dp[u * 26 + cu];
        if (val > ans) ans = val;

        for (const v of adj[u]) {
            const bu = u * 26, bv = v * 26;
            for (let c = 0; c < 26; c++) {
                if (dp[bu + c] > dp[bv + c]) dp[bv + c] = dp[bu + c];
            }
            if (--indeg[v] === 0) queue.push(v);
        }
    }
    return head === n ? ans : -1;
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
- [2192. All Ancestors of a Node in a Directed Acyclic Graph](../../1001-1500/1431-all-ancestors-of-a-node-in-a-directed-acyclic-graph/)
- [2876. Count Visited Nodes in a Directed Graph](../../3001-3500/3140-count-visited-nodes-in-a-directed-graph/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../../3501-4000/3916-minimum-time-to-reach-destination-in-directed-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/)
