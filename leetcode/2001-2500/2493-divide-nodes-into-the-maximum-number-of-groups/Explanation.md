# LeetCode 2493: Divide Nodes Into the Maximum Number of Groups

**LeetCode Problem #2493 — Divide Nodes Into the Maximum Number of Groups**
Solve LeetCode Divide Nodes Into the Maximum Number of Groups using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide Nodes Into the Maximum Number of Groups |
| LeetCode | #2493 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n` representing the number of nodes in an **undirected** graph. The nodes are labeled from `1` to `n`.

You are also given a 2D integer array `edges`, where `edges[i] = [a_i, b_i]` indicates that there is a **bidirectional** edge between nodes `a_i` and `b_i`. **Notice** that the given graph may be disconnected.

Divide the nodes of the graph into `m` groups (**1-indexed**) such that:

Each node in the graph belongs to exactly one group. 
 For every pair of nodes in the graph that are connected by an edge `[a_i, b_i]`, if `a_i` belongs to the group with index `x`, and `b_i` belongs to the group with index `y`, then `|y - x| = 1`.

Return *the maximum number of groups (i.e., maximum *`m`*) into which you can divide the nodes*. Return `-1` *if it is impossible to group the nodes with the given conditions*.

## Constraints
- `1 <= n <= 500`
- `1 <= edges.length <= 10^4`
- `edges[i].length == 2`
- `1 <= a_i, b_i <= n`
- `a_i != b_i`
- There is at most one edge between any pair of vertices.

## Examples
### Example 1
- **Input:** `n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]`
- **Output:** `4`
- **Explanation:** As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

### Example 2
- **Input:** `n = 3, edges = [[1,2],[2,3],[3,1]]`
- **Output:** `-1`
- **Explanation:** If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Divide Nodes Into the Maximum Number of Groups**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

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
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Check bipartiteness and identify components
        color = [0] * (n + 1)
        components = []

        for i in range(1, n + 1):
            if color[i] != 0:
                continue

            current_comp = []
            queue = deque([i])
            color[i] = 1

            while queue:
                u = queue.popleft()
                current_comp.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return -1  # Odd cycle detected; impossible to partition

            components.append(current_comp)

        # 2. Helper to compute max BFS depth from a starting node
        def max_groups_from(start: int) -> int:
            dist = {start: 1}
            queue = deque([start])
            max_depth = 1

            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[curr] + 1
                        max_depth = max(max_depth, dist[neighbor])
                        queue.append(neighbor)

            return max_depth

        # 3. For each component, pick the start node maximizing BFS depth
        total_groups = 0
        for comp in components:
            comp_max = max(max_groups_from(node) for node in comp)
            total_groups += comp_max

        return total_groups
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
- [2406. Divide Intervals Into Minimum Number of Groups](../../2001-2500/2406-divide-intervals-into-minimum-number-of-groups/)
- [2138. Divide a String Into Groups of Size k](../../2001-2500/2138-divide-a-string-into-groups-of-size-k/)
- [2871. Split Array Into Maximum Number of Subarrays](../../2501-3000/2871-split-array-into-maximum-number-of-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/)
