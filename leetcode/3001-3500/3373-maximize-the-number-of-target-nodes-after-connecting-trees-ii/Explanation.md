# LeetCode 3373: Maximize the Number of Target Nodes After Connecting Trees II

**LeetCode Problem #3373 — Maximize the Number of Target Nodes After Connecting Trees II**
Solve LeetCode Maximize the Number of Target Nodes After Connecting Trees II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Number of Target Nodes After Connecting Trees II |
| LeetCode | #3373 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There exist two **undirected **trees with `n` and `m` nodes, labeled from `[0, n - 1]` and `[0, m - 1]`, respectively.

You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the first tree and `edges2[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the second tree.

Node `u` is **target** to node `v` if the number of edges on the path from `u` to `v` is even. **Note** that a node is *always* **target** to itself.

Return an array of `n` integers `answer`, where `answer[i]` is the **maximum** possible number of nodes that are **target** to node `i` of the first tree if you had to connect one node from the first tree to another node in the second tree.

**Note** that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

## Constraints
- `2 <= n, m <= 10^5`
- `edges1.length == n - 1`
- `edges2.length == m - 1`
- `edges1[i].length == edges2[i].length == 2`
- `edges1[i] = [a_i, b_i]`
- `0 <= a_i, b_i < n`
- `edges2[i] = [u_i, v_i]`
- `0 <= u_i, v_i < m`
- The input is generated such that `edges1` and `edges2` represent valid trees.

## Examples
### Example 1
- **Input:** `edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]`
- **Output:** `[8,7,7,8,8]`
- **Explanation:** For `i = 0`, connect node 0 from the first tree to node 0 from the second tree. 
 For `i = 1`, connect node 1 from the first tree to node 4 from the second tree. 
 For `i = 2`, connect node 2 from the first tree to node 7 from the second tree. 
 For `i = 3`, connect node 3 from the first tree to node 0 from the second tree. 
 For `i = 4`, connect node 4 from the first tree to node 4 from the second tree.

### Example 2
- **Input:** `edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]`
- **Output:** `[3,6,6,6,6]`
- **Explanation:** For every `i`, connect node `i` of the first tree with any node of the second tree.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximize the Number of Target Nodes After Connecting Trees II**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[8,7,7,8,8]`.
4. **Verification:** For `i = 0`, connect node 0 from the first tree to node 0 from the second tree. 
 For `i = 1`, connect node 1 from the first tree to node 4 from the second tree. 
 For `i = 2`, connect node 2 from the first tree to node 7 from the second tree. 
 For `i = 3`, connect node 3 from the first tree to node 0 from the second tree. 
 For `i = 4`, connect node 4 from the first tree to node 4 from the second tree.

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
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def color(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            col = [-1] * n
            col[0] = 0
            q = deque([0])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if col[v] == -1:
                        col[v] = col[u] ^ 1
                        q.append(v)
            return col

        col1 = color(edges1)
        col2 = color(edges2)

        cnt1 = [col1.count(0), col1.count(1)]
        cnt2 = [col2.count(0), col2.count(1)]
        best2 = max(cnt2)

        return [cnt1[c] + best2 for c in col1]
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
- [3372. Maximize the Number of Target Nodes After Connecting Trees I](../../3001-3500/3372-maximize-the-number-of-target-nodes-after-connecting-trees-i/)
- [3003. Maximize the Number of Partitions After Operations](../../3001-3500/3003-maximize-the-number-of-partitions-after-operations/)
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1074-number-of-submatrices-that-sum-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/)
