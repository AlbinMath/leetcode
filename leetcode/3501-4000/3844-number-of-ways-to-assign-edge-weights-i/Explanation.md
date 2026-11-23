# LeetCode 3558: Number of Ways to Assign Edge Weights I

**LeetCode Problem #3558 — Number of Ways to Assign Edge Weights I**
Solve LeetCode Number of Ways to Assign Edge Weights I using Java and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Assign Edge Weights I |
| LeetCode | #3558 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is an undirected tree with `n` nodes labeled from 1 to `n`, rooted at node 1. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i`.

Initially, all edges have a weight of 0. You must assign each edge a weight of either **1** or **2**.

The **cost** of a path between any two nodes `u` and `v` is the total weight of all edges in the path connecting them.

Select any one node `x` at the **maximum** depth. Return the number of ways to assign edge weights in the path from node 1 to `x` such that its total cost is **odd**.

Since the answer may be large, return it **modulo** `10^9 + 7`.

**Note:** Ignore all edges **not** in the path from node 1 to `x`.

## Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] == [u_i, v_i]`
- `1 <= u_i, v_i <= n`
- `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[1,2]]`
- **Output:** `1`
- **Explanation:** The path from Node 1 to Node 2 consists of one edge (`1 &rarr; 2`). 
 Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

### Example 2
- **Input:** `edges = [[1,2],[1,3],[3,4],[3,5]]`
- **Output:** `2`
- **Explanation:** The maximum depth is 2, with nodes 4 and 5 at the same depth. Either node can be selected for processing. 
 For example, the path from Node 1 to Node 4 consists of two edges (`1 &rarr; 3` and `3 &rarr; 4`). 
 Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Ways to Assign Edge Weights I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[1,2]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The path from Node 1 to Node 2 consists of one edge (`1 &rarr; 2`). 
 Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public int assignEdgeWeights(int[][] edges) {
        final int MOD = 1_000_000_007;

        int n = edges.length + 1;

        // Build adjacency list
        List<Integer>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        // Find maximum depth from node 1
        int maxDepth = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);

        int[] depth = new int[n + 1];
        Arrays.fill(depth, -1);
        depth[1] = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();

            for (int next : graph[node]) {
                if (depth[next] == -1) {
                    depth[next] = depth[node] + 1;
                    maxDepth = Math.max(maxDepth, depth[next]);
                    queue.offer(next);
                }
            }
        }

        // For a path with d edges:
        // Number of assignments with odd sum = 2^(d-1)
        //
        // We select a node at maximum depth,
        // so the path contains maxDepth edges.

        long ans = 1;

        for (int i = 1; i < maxDepth; i++) {
            ans = (ans * 2) % MOD;
        }

        return (int) ans;
    }
}
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
- [3559. Number of Ways to Assign Edge Weights II](../../3501-4000/3842-number-of-ways-to-assign-edge-weights-ii/)
- [2699. Modify Graph Edge Weights](../../2501-3000/2803-modify-graph-edge-weights/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1501-2000/1531-number-of-ways-to-wear-different-hats-to-each-other/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/)
