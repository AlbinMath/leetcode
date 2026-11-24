# LeetCode 3559: Number of Ways to Assign Edge Weights II

**LeetCode Problem #3559 — Number of Ways to Assign Edge Weights II**
Solve LeetCode Number of Ways to Assign Edge Weights II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Assign Edge Weights II |
| LeetCode | #3559 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected tree with `n` nodes labeled from 1 to `n`, rooted at node 1. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i`.

Initially, all edges have a weight of 0. You must assign each edge a weight of either **1** or **2**.

The **cost** of a path between any two nodes `u` and `v` is the total weight of all edges in the path connecting them.

You are given a 2D integer array `queries`. For each `queries[i] = [u_i, v_i]`, determine the number of ways to assign weights to edges **in the path** such that the cost of the path between `u_i` and `v_i` is **odd**.

Return an array `answer`, where `answer[i]` is the number of valid assignments for `queries[i]`.

Since the answer may be large, apply **modulo** `10^9 + 7` to each `answer[i]`.

**Note:** For each query, disregard all edges **not** in the path between node `u_i` and `v_i`.

## Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] == [u_i, v_i]`
- `1 <= queries.length <= 10^5`
- `queries[i] == [u_i, v_i]`
- `1 <= u_i, v_i <= n`
- `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[1,2]], queries = [[1,1],[1,2]]`
- **Output:** `[0,1]`
- **Explanation:** Query `[1,1]`: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0. 
 Query `[1,2]`: The path from Node 1 to Node 2 consists of one edge (`1 &rarr; 2`). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

### Example 2
- **Input:** `edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]`
- **Output:** `[2,1,4]`
- **Explanation:** Query `[1,4]`: The path from Node 1 to Node 4 consists of two edges (`1 &rarr; 3` and `3 &rarr; 4`). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2. 
 Query `[3,4]`: The path from Node 3 to Node 4 consists of one edge (`3 &rarr; 4`). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1. 
 Query `[2,5]`: The path from Node 2 to Node 5 consists of three edges (`2 &rarr; 1, 1 &rarr; 3`, and `3 &rarr; 5`). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Ways to Assign Edge Weights II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[1,2]], queries = [[1,1],[1,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1]`.
4. **Verification:** Query `[1,1]`: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0. 
 Query `[1,2]`: The path from Node 1 to Node 2 consists of one edge (`1 &rarr; 2`). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:

    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        MOD = 1000000007

        # Number of nodes
        n = len(edges) + 1

        # Build tree
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Binary lifting
        LOG = (n).bit_length()

        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        # Iterative DFS/BFS
        stack = [1]
        parent = [0] * (n + 1)
        parent[1] = 0

        while stack:
            u = stack.pop()

            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                up[0][v] = u
                stack.append(v)

        # Build binary lifting table
        for j in range(1, LOG):
            prev = up[j - 1]
            cur = up[j]

            for v in range(1, n + 1):
                cur[v] = prev[prev[v]]

        def lca(a, b):
            # Make a the deeper node
            if depth[a] < depth[b]:
                a, b = b, a

            # Bring a to the same depth as b
            diff = depth[a] - depth[b]

            bit = 0
            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            # Lift both nodes
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]

            return up[0][a]

        # Precompute powers of 2.
        #
        # Maximum distance is n-1.
        pow2 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        answer = []

        for u, v in queries:

            # Same node -> path has 0 edges.
            # Cost is always 0 (even), so answer is 0.
            if u == v:
                answer.append(0)
                continue

            w = lca(u, v)

            distance = depth[u] + depth[v] - 2 * depth[w]

            # Exactly half of 2^distance assignments
            # have an odd total weight.
            answer.append(pow2[distance - 1])

        return answer
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
- [3558. Number of Ways to Assign Edge Weights I](../../3501-4000/3558-number-of-ways-to-assign-edge-weights-i/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1001-1500/1434-number-of-ways-to-wear-different-hats-to-each-other/)
- [1444. Number of Ways of Cutting a Pizza](../../1001-1500/1444-number-of-ways-of-cutting-a-pizza/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/)
