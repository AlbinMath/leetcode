# LeetCode 1466: Reorder Routes to Make All Paths Lead to the City Zero

**LeetCode Problem #1466 — Reorder Routes to Make All Paths Lead to the City Zero**
Solve LeetCode Reorder Routes to Make All Paths Lead to the City Zero using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reorder Routes to Make All Paths Lead to the City Zero |
| LeetCode | #1466 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` cities numbered from `0` to `n - 1` and `n - 1` roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by `connections` where `connections[i] = [a_i, b_i]` represents a road from city `a_i` to city `b_i`.

This year, there will be a big event in the capital (city `0`), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city `0`. Return the **minimum** number of edges changed.

It's **guaranteed** that each city can reach city `0` after reorder.

## Constraints
- `2 <= n <= 5 * 10^4`
- `connections.length == n - 1`
- `connections[i].length == 2`
- `0 <= a_i, b_i <= n - 1`
- `a_i != b_i`

## Examples
### Example 1
- **Input:** `n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]`
- **Output:** `3`
- **Explanation:** Change the direction of edges show in red such that each node can reach the node 0 (capital).

### Example 2
- **Input:** `n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]`
- **Output:** `2`
- **Explanation:** Change the direction of edges show in red such that each node can reach the node 0 (capital).

### Example 3
- **Input:** `n = 3, connections = [[1,0],[2,0]]`
- **Output:** `0`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reorder Routes to Make All Paths Lead to the City Zero**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Change the direction of edges show in red such that each node can reach the node 0 (capital).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minReorder = function(n, connections) {
    const graph = Array.from({ length: n }, () => []);

    for (const [a, b] of connections) {
        graph[a].push([b, 1]);
        graph[b].push([a, 0]);
    }

    const visited = new Array(n).fill(false);
    let changes = 0;

    function dfs(city) {
        visited[city] = true;

        for (const [neighbor, cost] of graph[city]) {
            if (!visited[neighbor]) {
                changes += cost;
                dfs(neighbor);
            }
        }
    }

    dfs(0);

    return changes;
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1787. Make the XOR of All Segments Equal to Zero](../../1501-2000/1787-make-the-xor-of-all-segments-equal-to-zero/)
- [2772. Apply Operations to Make All Array Elements Equal to Zero](../../2501-3000/2772-apply-operations-to-make-all-array-elements-equal-to-zero/)
- [797. All Paths From Source to Target](../../0501-1000/0797-all-paths-from-source-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)
