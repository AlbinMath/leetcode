# LeetCode 2497: Maximum Star Sum of a Graph

**LeetCode Problem #2497 — Maximum Star Sum of a Graph**
Solve LeetCode Maximum Star Sum of a Graph using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Star Sum of a Graph |
| LeetCode | #2497 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected graph consisting of `n` nodes numbered from `0` to `n - 1`. You are given a **0-indexed** integer array `vals` of length `n` where `vals[i]` denotes the value of the `i^th` node.

You are also given a 2D integer array `edges` where `edges[i] = [a_i, b_i]` denotes that there exists an **undirected** edge connecting nodes `a_i` and `b_i.`

A **star graph** is a subgraph of the given graph having a center node containing `0` or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.

The image below shows star graphs with `3` and `4` neighbors respectively, centered at the blue node.

The **star sum** is the sum of the values of all the nodes present in the star graph.

Given an integer `k`, return *the **maximum star sum** of a star graph containing **at most** *`k`* edges.*

## Constraints
- `n == vals.length`
- `1 <= n <= 10^5`
- `-10^4 <= vals[i] <= 10^4`
- `0 <= edges.length <= min(n * (n - 1) / 2``, 10^5)`
- `edges[i].length == 2`
- `0 <= a_i, b_i <= n - 1`
- `a_i != b_i`
- `0 <= k <= n - 1`

## Examples
### Example 1
- **Input:** `vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2`
- **Output:** `16`
- **Explanation:** The above diagram represents the input graph.
The star graph with the maximum star sum is denoted by blue. It is centered at 3 and includes its neighbors 1 and 4.
It can be shown it is not possible to get a star graph with a sum greater than 16.

### Example 2
- **Input:** `vals = [-5], edges = [], k = 0`
- **Output:** `-5`
- **Explanation:** There is only one possible star graph, which is node 0 itself.
Hence, we return -5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Star Sum of a Graph**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** The above diagram represents the input graph.
The star graph with the maximum star sum is denoted by blue. It is centered at 3 and includes its neighbors 1 and 4.
It can be shown it is not possible to get a star graph with a sum greater than 16.

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
var maxStarSum = function(vals, edges, k) {
    const n = vals.length;

    const graph = Array.from({ length: n }, () => []);

    // Build undirected graph.
    for (const [u, v] of edges) {
        graph[u].push(vals[v]);
        graph[v].push(vals[u]);
    }

    let answer = -Infinity;

    // Try every node as the center.
    for (let i = 0; i < n; i++) {
        // Keep only positive neighbor values.
        const neighbors = graph[i].filter(value => value > 0);

        // Sort in descending order.
        neighbors.sort((a, b) => b - a);

        // Start with the center's own value.
        let sum = vals[i];

        // Add at most k highest positive neighbors.
        for (let j = 0; j < Math.min(k, neighbors.length); j++) {
            sum += neighbors[j];
        }

        answer = Math.max(answer, sum);
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
- [3547. Maximum Sum of Edge Values in a Graph](../../3501-4000/3845-maximum-sum-of-edge-values-in-a-graph/)
- [1791. Find Center of Star Graph](../../1501-2000/1916-find-center-of-star-graph/)
- [2065. Maximum Path Quality of a Graph](../../2001-2500/2189-maximum-path-quality-of-a-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-star-sum-of-a-graph/)
