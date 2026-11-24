# LeetCode 1617: Count Subtrees With Max Distance Between Cities

**LeetCode Problem #1617 — Count Subtrees With Max Distance Between Cities**
Solve LeetCode Count Subtrees With Max Distance Between Cities using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subtrees With Max Distance Between Cities |
| LeetCode | #1617 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` cities numbered from `1` to `n`. You are given an array `edges` of size `n-1`, where `edges[i] = [u_i, v_i]` represents a bidirectional edge between cities `u_i` and `v_i`. There exists a unique path between each pair of cities. In other words, the cities form a **tree**.

A **subtree** is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each `d` from `1` to `n-1`, find the number of subtrees in which the **maximum distance** between any two cities in the subtree is equal to `d`.

Return *an array of size* `n-1` *where the *`d^th`* **element **(1-indexed)** is the number of subtrees in which the **maximum distance** between any two cities is equal to *`d`.

**Notice** that the **distance** between the two cities is the number of edges in the path between them.

## Constraints
- `2 <= n <= 15`
- `edges.length == n-1`
- `edges[i].length == 2`
- `1 <= u_i, v_i <= n`
- All pairs `(u_i, v_i)` are distinct.

## Examples
### Example 1
- **Input:** `n = 4, edges = [[1,2],[2,3],[2,4]]`
- **Output:** `[3,4,0]`
- **Explanation:** The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

### Example 2
- **Input:** `n = 2, edges = [[1,2]]`
- **Output:** `[1]`

### Example 3
- **Input:** `n = 3, edges = [[1,2],[2,3]]`
- **Output:** `[2,1]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Subtrees With Max Distance Between Cities**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[1,2],[2,3],[2,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4,0]`.
4. **Verification:** The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var countSubgraphsForEachDiameter = function (n, edges) {
  const INF = 1e9;
  const dist = Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => (i === j ? 0 : INF))
  );
  for (const [u, v] of edges) {
    dist[u - 1][v - 1] = 1;
    dist[v - 1][u - 1] = 1;
  }
  for (let k = 0; k < n; k++)
    for (let i = 0; i < n; i++)
      for (let j = 0; j < n; j++)
        if (dist[i][k] + dist[k][j] < dist[i][j])
          dist[i][j] = dist[i][k] + dist[k][j];

  const ans = new Array(n - 1).fill(0);

  for (let mask = 1; mask < 1 << n; mask++) {
    let size = 0;
    for (let x = mask; x; x &= x - 1) size++;
    if (size < 2) continue;

    let inside = 0;
    for (const [u, v] of edges) {
      if (mask & (1 << (u - 1)) && mask & (1 << (v - 1))) inside++;
    }
    if (inside !== size - 1) continue;

    let diameter = 0;
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i))) continue;
      for (let j = i + 1; j < n; j++) {
        if (mask & (1 << j)) diameter = Math.max(diameter, dist[i][j]);
      }
    }
    ans[diameter - 1]++;
  }

  return ans;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1385-find-the-distance-value-between-two-arrays/)
- [2492. Minimum Score of a Path Between Two Cities](../../2001-2500/2492-minimum-score-of-a-path-between-two-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/)
