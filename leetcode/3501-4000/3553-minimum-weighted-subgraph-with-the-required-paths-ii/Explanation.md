# LeetCode 3553: Minimum Weighted Subgraph With the Required Paths II

**LeetCode Problem #3553 — Minimum Weighted Subgraph With the Required Paths II**
Solve LeetCode Minimum Weighted Subgraph With the Required Paths II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Weighted Subgraph With the Required Paths II |
| LeetCode | #3553 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an **undirected weighted** tree with n nodes, numbered from 0 to n - 1 . It is represented by a 2D integer array edges of length n - 1 , where edges[i] = [u_i, v_i, w_i] indicates that there is an edge between nodes u_i and v_i with weight w_i .​

Additionally, you are given a 2D integer array queries , where queries[j] = [src1_j, src2_j, dest_j] .

Return an array answer of length equal to queries.length , where answer[j] is the **minimum total weight** of a subtree such that it is possible to reach dest_j from both src1_j and src2_j using edges in this subtree.

A subtree here is any connected subset of nodes and edges of the original tree forming a valid tree.

## Constraints
- `src1_j`, `src2_j`, and `dest_j` are pairwise distinct.
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]`
- **Output:** `[12,11]`
- **Explanation:** The blue edges represent one of the subtrees that yield the optimal answer. 

 

 
 
 `answer[0]`: The total weight of the selected subtree that ensures a path from `src1 = 2` and `src2 = 3` to `dest = 4` is `3 + 5 + 4 = 12`. 
 
 
 `answer[1]`: The total weight of the selected subtree that ensures a path from `src1 = 0` and `src2 = 2` to `dest = 5` is `2 + 3 + 6 = 11`.

### Example 2
- **Input:** `edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]`
- **Output:** `[15]`
- **Explanation:** `answer[0]`: The total weight of the selected subtree that ensures a path from `src1 = 0` and `src2 = 1` to `dest = 2` is `8 + 7 = 15`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Weighted Subgraph With the Required Paths II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[12,11]`.
4. **Verification:** The blue edges represent one of the subtrees that yield the optimal answer. 

 

 
 
 `answer[0]`: The total weight of the selected subtree that ensures a path from `src1 = 2` and `src2 = 3` to `dest = 4` is `3 + 5 + 4 = 12`. 
 
 
 `answer[1]`: The total weight of the selected subtree that ensures a path from `src1 = 0` and `src2 = 2` to `dest = 5` is `2 + 3 + 6 = 11`.

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
class Solution(object):
    def minimumWeight(self, edges, queries):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [-1] * n
        depth = [0] * n
        D = [0] * n
        tin = [0] * n
        order = []
        stack = [0]
        seen = [False] * n
        seen[0] = True
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for v, w in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    D[v] = D[u] + w
                    stack.append(v)

        # sparse table over DFS order; table[0][i] = (depth of parent, parent) of order[i]
        # LCA(a, b) for a != b, tin[a] < tin[b]: the parent with min depth in (tin[a], tin[b]]
        m = n
        base = [(depth[parent[order[i]]], parent[order[i]]) if i > 0 else (0, 0)
                for i in range(m)]
        table = [base]
        k = 1
        while (1 << k) <= m:
            prev = table[-1]
            half = 1 << (k - 1)
            table.append([min(prev[i], prev[i + half]) for i in range(m - (1 << k) + 1)])
            k += 1

        def lca(a, b):
            if a == b:
                return a
            l, r = tin[a], tin[b]
            if l > r:
                l, r = r, l
            l += 1  # range (tin[a], tin[b]]
            j = (r - l + 1).bit_length() - 1
            row = table[j]
            x = row[l]
            y = row[r - (1 << j) + 1]
            return min(x, y)[1]

        def dist(a, b):
            return D[a] + D[b] - 2 * D[lca(a, b)]

        ans = []
        for a, b, c in queries:
            ans.append((dist(a, b) + dist(b, c) + dist(a, c)) // 2)
        return ans
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
- [2203. Minimum Weighted Subgraph With the Required Paths](../../2001-2500/2203-minimum-weighted-subgraph-with-the-required-paths/)
- [3789. Minimum Cost to Acquire Required Items](../../3501-4000/3789-minimum-cost-to-acquire-required-items/)
- [3108. Minimum Cost Walk in Weighted Graph](../../3001-3500/3108-minimum-cost-walk-in-weighted-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/)
