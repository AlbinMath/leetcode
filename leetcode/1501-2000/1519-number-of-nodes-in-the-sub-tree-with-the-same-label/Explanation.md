# LeetCode 1519: Number of Nodes in the Sub-Tree With the Same Label

**LeetCode Problem #1519 — Number of Nodes in the Sub-Tree With the Same Label**
Solve LeetCode Number of Nodes in the Sub-Tree With the Same Label using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Nodes in the Sub-Tree With the Same Label |
| LeetCode | #1519 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` `edges`. The **root** of the tree is the node `0`, and each node of the tree has **a label** which is a lower-case character given in the string `labels` (i.e. The node with the number `i` has the label `labels[i]`).

The `edges` array is given on the form `edges[i] = [a_i, b_i]`, which means there is an edge between nodes `a_i` and `b_i` in the tree.

Return *an array of size `n`* where `ans[i]` is the number of nodes in the subtree of the `i^th` node which have the same label as node `i`.

A subtree of a tree `T` is the tree consisting of a node in `T` and all of its descendant nodes.

## Constraints
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- `labels.length == n`
- `labels` is consisting of only of lowercase English letters.

## Examples
### Example 1
- **Input:** `n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"`
- **Output:** `[2,1,1,1,1,1,1]`
- **Explanation:** Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).

### Example 2
- **Input:** `n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"`
- **Output:** `[4,2,1,1]`
- **Explanation:** The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.

### Example 3
- **Input:** `n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"`
- **Output:** `[3,2,1,1,1]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Nodes in the Sub-Tree With the Same Label**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,1,1,1,1,1]`.
4. **Verification:** Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).

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
from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        parent = [-1] * n
        parent[0] = 0  # sentinel so the root is never seen as unvisited
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)

        cnt = [[0] * 26 for _ in range(n)]
        ans = [0] * n
        for u in reversed(order):
            c = ord(labels[u]) - 97
            cnt[u][c] += 1
            ans[u] = cnt[u][c]
            if u != 0:
                p = cnt[parent[u]]
                cu = cnt[u]
                for i in range(26):
                    p[i] += cu[i]
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
- [100. Same Tree](../../0001-0500/0100-same-tree/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1001-1500/1467-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1569-number-of-ways-to-reorder-array-to-get-same-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)
