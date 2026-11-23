# LeetCode 1489: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

**LeetCode Problem #1489 — Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree**
Solve LeetCode Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree |
| LeetCode | #1489 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a weighted undirected connected graph with `n` vertices numbered from `0` to `n - 1`, and an array `edges` where `edges[i] = [a_i, b_i, weight_i]` represents a bidirectional and weighted edge between nodes `a_i` and `b_i`. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find *all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST)*. An MST edge whose deletion from the graph would cause the MST weight to increase is called a *critical edge*. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

## Constraints
- `2 <= n <= 100`
- `1 <= edges.length <= min(200, n * (n - 1) / 2)`
- `edges[i].length == 3`
- `0 <= a_i < b_i < n`
- `1 <= weight_i <= 1000`
- All pairs `(a_i, b_i)` are **distinct**.

## Examples
### Example 1
- **Input:** `n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]`
- **Output:** `[[0,1],[2,3,4,5]]`
- **Explanation:** The figure above describes the graph.
The following figure shows all the possible MSTs:
 
Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

### Example 2
- **Input:** `n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]`
- **Output:** `[[],[0,1,2,3]]`
- **Explanation:** We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,1],[2,3,4,5]]`.
4. **Verification:** The figure above describes the graph.
The following figure shows all the possible MSTs:
 
Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

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
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted((w, u, v, i) for i, (u, v, w) in enumerate(edges))

        def mst(skip=-1, pick=-1):
            p = list(range(n))

            def find(x):
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x

            cost, cnt = 0, 0

            if pick != -1:
                w, u, v, _ = edges[pick]
                p[find(u)] = find(v)
                cost, cnt = w, 1

            for i, (w, u, v, _) in enumerate(edges):
                if i == skip:
                    continue
                a, b = find(u), find(v)
                if a != b:
                    p[a] = b
                    cost += w
                    cnt += 1

            return cost if cnt == n - 1 else float('inf')

        base = mst()
        critical, pseudo = [], []

        for i, edge in enumerate(edges):
            if mst(skip=i) > base:
                critical.append(edge[3])
            elif mst(pick=i) == base:
                pseudo.append(edge[3])

        return [critical, pseudo]
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
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
