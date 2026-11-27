# LeetCode 3820: Pythagorean Distance Nodes in a Tree

**LeetCode Problem #3820 — Pythagorean Distance Nodes in a Tree**
Solve LeetCode Pythagorean Distance Nodes in a Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pythagorean Distance Nodes in a Tree |
| LeetCode | #3820 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and an undirected tree with `n` nodes numbered from 0 to `n - 1`. The tree is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between `u_i` and `v_i`.

You are also given three **distinct** target nodes `x`, `y`, and `z`.

For any node `u` in the tree:

Let `dx` be the distance from `u` to node `x` 
 Let `dy` be the distance from `u` to node `y` 
 Let `dz` be the distance from `u` to node `z`

The node `u` is called **special** if the three distances form a **Pythagorean Triplet**.

Return an integer denoting the number of special nodes in the tree.

A **Pythagorean triplet** consists of three integers `a`, `b`, and `c` which, when sorted in **ascending** order, satisfy `a^2 + b^2 = c^2`.

The **distance** between two nodes in a tree is the number of edges on the unique path between them.

## Constraints
- `4 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] = [u_i, v_i]`
- `0 <= u_i, v_i, x, y, z <= n - 1`
- `x`, `y`, and `z` are pairwise **distinct**.
- The input is generated such that `edges` represent a valid tree.

## Examples
### Example 1
- **Input:** `n = 4, edges = [[0,1],[0,2],[0,3]], x = 1, y = 2, z = 3`
- **Output:** `3`
- **Explanation:** For each node, we compute its distances to nodes `x = 1`, `y = 2`, and `z = 3`. 

 
 Node 0 has distances 1, 1, and 1. After sorting, the distances are 1, 1, and 1, which do not satisfy the Pythagorean condition. 
 Node 1 has distances 0, 2, and 2. After sorting, the distances are 0, 2, and 2. Since `0^2 + 2^2 = 2^2`, node 1 is special. 
 Node 2 has distances 2, 0, and 2. After sorting, the distances are 0, 2, and 2. Since `0^2 + 2^2 = 2^2`, node 2 is special. 
 Node 3 has distances 2, 2, and 0. After sorting, the distances are 0, 2, and 2. This also satisfies the Pythagorean condition. 
 

 Therefore, nodes 1, 2, and 3 are special, and the answer is 3.

### Example 2
- **Input:** `n = 4, edges = [[0,1],[1,2],[2,3]], x = 0, y = 3, z = 2`
- **Output:** `0`
- **Explanation:** For each node, we compute its distances to nodes `x = 0`, `y = 3`, and `z = 2`. 

 
 Node 0 has distances 0, 3, and 2. After sorting, the distances are 0, 2, and 3, which do not satisfy the Pythagorean condition. 
 Node 1 has distances 1, 2, and 1. After sorting, the distances are 1, 1, and 2, which do not satisfy the Pythagorean condition. 
 Node 2 has distances 2, 1, and 0. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition. 
 Node 3 has distances 3, 0, and 1. After sorting, the distances are 0, 1, and 3, which do not satisfy the Pythagorean condition. 
 

 No node satisfies the Pythagorean condition. Therefore, the answer is 0.

### Example 3
- **Input:** `n = 4, edges = [[0,1],[1,2],[1,3]], x = 1, y = 3, z = 0`
- **Output:** `1`
- **Explanation:** For each node, we compute its distances to nodes `x = 1`, `y = 3`, and `z = 0`. 

 
 Node 0 has distances 1, 2, and 0. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition. 
 Node 1 has distances 0, 1, and 1. After sorting, the distances are 0, 1, and 1. Since `0^2 + 1^2 = 1^2`, node 1 is special. 
 Node 2 has distances 1, 2, and 2. After sorting, the distances are 1, 2, and 2, which do not satisfy the Pythagorean condition. 
 Node 3 has distances 1, 0, and 2. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition. 
 

 Therefore, the answer is 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Pythagorean Distance Nodes in a Tree**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[0,1],[0,2],[0,3]], x = 1, y = 2, z = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** For each node, we compute its distances to nodes `x = 1`, `y = 2`, and `z = 3`. 

 
 Node 0 has distances 1, 1, and 1. After sorting, the distances are 1, 1, and 1, which do not satisfy the Pythagorean condition. 
 Node 1 has distances 0, 2, and 2. After sorting, the distances are 0, 2, and 2. Since `0^2 + 2^2 = 2^2`, node 1 is special. 
 Node 2 has distances 2, 0, and 2. After sorting, the distances are 0, 2, and 2. Since `0^2 + 2^2 = 2^2`, node 2 is special. 
 Node 3 has distances 2, 2, and 0. After sorting, the distances are 0, 2, and 2. This also satisfies the Pythagorean condition. 
 

 Therefore, nodes 1, 2, and 3 are special, and the answer is 3.

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
from collections import deque
from typing import List

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(src):
            dist = [-1] * n
            dist[src] = 0
            q = deque([src])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist

        dx, dy, dz = bfs(x), bfs(y), bfs(z)
        ans = 0
        for u in range(n):
            a, b, c = sorted((dx[u], dy[u], dz[u]))
            if a * a + b * b == c * c:
                ans += 1
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
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0863-all-nodes-distance-k-in-binary-tree/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)
- [1361. Validate Binary Tree Nodes](../../1001-1500/1361-validate-binary-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/)
