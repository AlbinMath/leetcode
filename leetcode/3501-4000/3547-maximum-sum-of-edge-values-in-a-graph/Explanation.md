# LeetCode 3547: Maximum Sum of Edge Values in a Graph

**LeetCode Problem #3547 — Maximum Sum of Edge Values in a Graph**
Solve LeetCode Maximum Sum of Edge Values in a Graph using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of Edge Values in a Graph |
| LeetCode | #3547 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an **undirected connected** graph of `n` nodes, numbered from `0` to `n - 1`. Each node is connected to **at most** 2 other nodes.

The graph consists of `m` edges, represented by a 2D array `edges`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i`.

You have to assign a **unique** value from 1 to n to each node. The value of an edge will be the **product** of the values assigned to the two nodes it connects.

Your score is the sum of the values of all edges in the graph.

Return the **maximum** score you can achieve.

## Constraints
- `1 <= n <= 5 * 10^4`
- `m == edges.length`
- `1 <= m <= n`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- There are no repeated edges.
- The graph is connected.
- Each node is connected to at most 2 other nodes.

## Examples
### Example 1
- **Input:** `n = 4, edges = [[0,1],[1,2],[2,3]]`
- **Output:** `23`
- **Explanation:** The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: `(1 * 3) + (3 * 4) + (4 * 2) = 23`.

### Example 2
- **Input:** `n = 6, edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]`
- **Output:** `82`
- **Explanation:** The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: `(1 * 2) + (2 * 4) + (4 * 6) + (6 * 5) + (5 * 3) + (3 * 1) = 82`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum of Edge Values in a Graph**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[0,1],[1,2],[2,3]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `23`.
4. **Verification:** The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: `(1 * 3) + (3 * 4) + (4 * 2) = 23`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxScore = function(n, edges) {
    const sumOfSquares = n * (n + 1) * (2 * n + 1) / 6;

    if (edges.length === n) {
        // Cycle
        return sumOfSquares - (2 * n - 3);
    }

    // Path
    return sumOfSquares - (2 * n - 1);
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2497. Maximum Star Sum of a Graph](../../2001-2500/2497-maximum-star-sum-of-a-graph/)
- [3419. Minimize the Maximum Edge Weight of Graph](../../3001-3500/3419-minimize-the-maximum-edge-weight-of-graph/)
- [3068. Find the Maximum Sum of Node Values](../../3001-3500/3068-find-the-maximum-sum-of-node-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/)
