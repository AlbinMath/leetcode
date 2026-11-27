# LeetCode 3585: Find Weighted Median Node in Tree

**LeetCode Problem #3585 — Find Weighted Median Node in Tree**
Solve LeetCode Find Weighted Median Node in Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Weighted Median Node in Tree |
| LeetCode | #3585 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and an **undirected, weighted** tree rooted at node 0 with `n` nodes numbered from 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates an edge from node `u_i` to `v_i` with weight `w_i`.

The **weighted median node** is defined as the **first** node `x` on the path from `u_i` to `v_i` such that the sum of edge weights from `u_i` to `x` is **greater than or equal to half** of the total path weight.

You are given a 2D integer array `queries`. For each `queries[j] = [u_j, v_j]`, determine the weighted median node along the path from `u_j` to `v_j`.

Return an array `ans`, where `ans[j]` is the node index of the weighted median for `queries[j]`.

## Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] == [u_i, v_i, w_i]`
- `0 <= u_i, v_i < n`
- `1 <= w_i <= 10^9`
- `1 <= queries.length <= 10^5`
- `queries[j] == [u_j, v_j]`
- `0 <= u_j, v_j < n`
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]]`
- **Output:** `[0,1]`
- **Explanation:** Query 
 Path 
 Edge 
 Weights 
 Total 
 Path 
 Weight 
 Half 
 Explanation 
 Answer 
 
 
 
 
 `[1, 0]` 
 `1 &rarr; 0` 
 `[7]` 
 7 
 3.5 
 Sum from `1 &rarr; 0 = 7 >= 3.5`, median is node 0. 
 0 
 
 
 `[0, 1]` 
 `0 &rarr; 1` 
 `[7]` 
 7 
 3.5 
 Sum from `0 &rarr; 1 = 7 >= 3.5`, median is node 1. 
 1

### Example 2
- **Input:** `n = 3, edges = [[0,1,2],[2,0,4]], queries = [[0,1],[2,0],[1,2]]`
- **Output:** `[1,0,2]`

### Example 3
- **Input:** `n = 5, edges = [[0,1,2],[0,2,5],[1,3,1],[2,4,3]], queries = [[3,4],[1,2]]`
- **Output:** `[2,2]`
- **Explanation:** Query 
 Path 
 Edge 
 Weights 
 Total 
 Path 
 Weight 
 Half 
 Explanation 
 Answer 
 
 
 
 
 `[3, 4]` 
 `3 &rarr; 1 &rarr; 0 &rarr; 2 &rarr; 4` 
 `[1, 2, 5, 3]` 
 11 
 5.5 
 Sum from `3 &rarr; 1 = 1 < 5.5`. 
 Sum from `3 &rarr; 0 = 1 + 2 = 3 < 5.5`. 
 Sum from `3 &rarr; 2 = 1 + 2 + 5 = 8 >= 5.5`, median is node 2. 
 2 
 
 
 `[1, 2]` 
 `1 &rarr; 0 &rarr; 2` 
 `[2, 5]` 
 7 
 3.5 
 
 Sum from `1 &rarr; 0 = 2 < 3.5`. 
 Sum from `1 &rarr; 2 = 2 + 5 = 7 >= 3.5`, median is node 2. 
 
 2

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find Weighted Median Node in Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1]`.
4. **Verification:** Query 
 Path 
 Edge 
 Weights 
 Total 
 Path 
 Weight 
 Half 
 Explanation 
 Answer 
 
 
 
 
 `[1, 0]` 
 `1 &rarr; 0` 
 `[7]` 
 7 
 3.5 
 Sum from `1 &rarr; 0 = 7 >= 3.5`, median is node 0. 
 0 
 
 
 `[0, 1]` 
 `0 &rarr; 1` 
 `[7]` 
 7 
 3.5 
 Sum from `0 &rarr; 1 = 7 >= 3.5`, median is node 1. 
 1

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
    def findMedian(self, n, edges, queries):
        LOG = max(1, (n - 1).bit_length())
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [0] * n
        depth = [0] * n
        D = [0] * n
        seen = [False] * n
        seen[0] = True
        order = [0]
        for u in order:  # BFS; appending while iterating is fine
            for v, w in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    D[v] = D[u] + w
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
        for u, v in queries:
            if u == v:
                ans.append(u)
                continue
            l = lca(u, v)
            du = D[u] - D[l]
            dv = D[v] - D[l]
            total = du + dv
            if du >= dv:
                cur = u
                Du = D[u]
                for k in range(LOG - 1, -1, -1):
                    a = up[k][cur]
                    if 2 * (Du - D[a]) < total:
                        cur = a
                ans.append(parent[cur])
            else:
                cur = v
                Dl = D[l]
                for k in range(LOG - 1, -1, -1):
                    a = up[k][cur]
                    if 2 * (du + D[a] - Dl) >= total:
                        cur = a
                ans.append(cur)
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
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../../1001-1500/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [608. Tree Node](../../0501-1000/0608-tree-node/)
- [671. Second Minimum Node In a Binary Tree](../../0501-1000/0671-second-minimum-node-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-weighted-median-node-in-tree/)
