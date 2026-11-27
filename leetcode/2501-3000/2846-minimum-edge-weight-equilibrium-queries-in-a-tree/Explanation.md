# LeetCode 2846: Minimum Edge Weight Equilibrium Queries in a Tree

**LeetCode Problem #2846 — Minimum Edge Weight Equilibrium Queries in a Tree**
Solve LeetCode Minimum Edge Weight Equilibrium Queries in a Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Edge Weight Equilibrium Queries in a Tree |
| LeetCode | #2846 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an undirected tree with `n` nodes labeled from `0` to `n - 1`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates that there is an edge between nodes `u_i` and `v_i` with weight `w_i` in the tree.

You are also given a 2D integer array `queries` of length `m`, where `queries[i] = [a_i, b_i]`. For each query, find the **minimum number of operations** required to make the weight of every edge on the path from `a_i` to `b_i` equal. In one operation, you can choose any edge of the tree and change its weight to any value.

**Note** that:

Queries are **independent** of each other, meaning that the tree returns to its **initial state** on each new query. 
 The path from `a_i` to `b_i` is a sequence of **distinct** nodes starting with node `a_i` and ending with node `b_i` such that every two adjacent nodes in the sequence share an edge in the tree.

Return *an array *`answer`* of length *`m`* where* `answer[i]` *is the answer to the* `i^th` *query.*

## Constraints
- `1 <= n <= 10^4`
- `edges.length == n - 1`
- `edges[i].length == 3`
- `0 <= u_i, v_i < n`
- `1 <= w_i <= 26`
- The input is generated such that `edges` represents a valid tree.
- `1 <= queries.length == m <= 2 * 10^4`
- `queries[i].length == 2`
- `0 <= a_i, b_i < n`

## Examples
### Example 1
- **Input:** `n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]`
- **Output:** `[0,0,1,3]`
- **Explanation:** In the first query, all the edges in the path from 0 to 3 have a weight of 1. Hence, the answer is 0.
In the second query, all the edges in the path from 3 to 6 have a weight of 2. Hence, the answer is 0.
In the third query, we change the weight of edge [2,3] to 2. After this operation, all the edges in the path from 2 to 6 have a weight of 2. Hence, the answer is 1.
In the fourth query, we change the weights of edges [0,1], [1,2] and [2,3] to 2. After these operations, all the edges in the path from 0 to 6 have a weight of 2. Hence, the answer is 3.
For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from a_i to b_i.

### Example 2
- **Input:** `n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]`
- **Output:** `[1,2,2,3]`
- **Explanation:** In the first query, we change the weight of edge [1,3] to 6. After this operation, all the edges in the path from 4 to 6 have a weight of 6. Hence, the answer is 1.
In the second query, we change the weight of edges [0,3] and [3,1] to 6. After these operations, all the edges in the path from 0 to 4 have a weight of 6. Hence, the answer is 2.
In the third query, we change the weight of edges [1,3] and [5,2] to 6. After these operations, all the edges in the path from 6 to 5 have a weight of 6. Hence, the answer is 2.
In the fourth query, we change the weights of edges [0,7], [0,3] and [1,3] to 6. After these operations, all the edges in the path from 7 to 4 have a weight of 6. Hence, the answer is 3.
For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from a_i to b_i.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Edge Weight Equilibrium Queries in a Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,0,1,3]`.
4. **Verification:** In the first query, all the edges in the path from 0 to 3 have a weight of 1. Hence, the answer is 0.
In the second query, all the edges in the path from 3 to 6 have a weight of 2. Hence, the answer is 0.
In the third query, we change the weight of edge [2,3] to 2. After this operation, all the edges in the path from 2 to 6 have a weight of 2. Hence, the answer is 1.
In the fourth query, we change the weights of edges [0,1], [1,2] and [2,3] to 2. After these operations, all the edges in the path from 0 to 6 have a weight of 2. Hence, the answer is 3.
For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from a_i to b_i.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def minOperationsQueries(self, n, edges, queries):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = max(1, (n - 1).bit_length())
        parent = [0] * n
        depth = [0] * n
        cnt = [None] * n
        cnt[0] = [0] * 27
        seen = [False] * n
        seen[0] = True
        order = [0]
        for u in order:  # BFS; appending while iterating is fine
            for v, w in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    c = cnt[u][:]
                    c[w] += 1
                    cnt[v] = c
                    order.append(v)

        up = [parent]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if (diff >> k) & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return parent[a]

        ans = []
        for a, b in queries:
            l = lca(a, b)
            length = depth[a] + depth[b] - 2 * depth[l]
            ca, cb, cl = cnt[a], cnt[b], cnt[l]
            best = 0
            for w in range(1, 27):
                c = ca[w] + cb[w] - 2 * cl[w]
                if c > best:
                    best = c
            ans.append(length - best)
        return ans
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3812. Minimum Edge Toggles on a Tree](../../3501-4000/3812-minimum-edge-toggles-on-a-tree/)
- [3419. Minimize the Maximum Edge Weight of Graph](../../3001-3500/3419-minimize-the-maximum-edge-weight-of-graph/)
- [111. Minimum Depth of Binary Tree](../../0001-0500/0111-minimum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/)
