# LeetCode 2858: Minimum Edge Reversals So Every Node Is Reachable

**LeetCode Problem #2858 — Minimum Edge Reversals So Every Node Is Reachable**
Solve LeetCode Minimum Edge Reversals So Every Node Is Reachable using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Edge Reversals So Every Node Is Reachable |
| LeetCode | #2858 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a **simple directed graph** with `n` nodes labeled from `0` to `n - 1`. The graph would form a **tree** if its edges were bi-directional.

You are given an integer `n` and a **2D** integer array `edges`, where `edges[i] = [u_i, v_i]` represents a **directed edge** going from node `u_i` to node `v_i`.

An **edge reversal** changes the direction of an edge, i.e., a directed edge going from node `u_i` to node `v_i` becomes a directed edge going from node `v_i` to node `u_i`.

For every node `i` in the range `[0, n - 1]`, your task is to **independently** calculate the **minimum** number of **edge reversals** required so it is possible to reach any other node starting from node `i` through a **sequence** of **directed edges**.

Return *an integer array *`answer`*, where *`answer[i]`* is the** * ***minimum** number of **edge reversals** required so it is possible to reach any other node starting from node *`i`* through a **sequence** of **directed edges**.*

## Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= u_i == edges[i][0] < n`
- `0 <= v_i == edges[i][1] < n`
- `u_i != v_i`
- The input is generated such that if the edges were bi-directional, the graph would be a tree.

## Examples
### Example 1
- **Input:** `n = 4, edges = [[2,0],[2,1],[1,3]]`
- **Output:** `[1,1,0,2]`
- **Explanation:** The image above shows the graph formed by the edges.
For node 0: after reversing the edge [2,0], it is possible to reach any other node starting from node 0.
So, answer[0] = 1.
For node 1: after reversing the edge [2,1], it is possible to reach any other node starting from node 1.
So, answer[1] = 1.
For node 2: it is already possible to reach any other node starting from node 2.
So, answer[2] = 0.
For node 3: after reversing the edges [1,3] and [2,1], it is possible to reach any other node starting from node 3.
So, answer[3] = 2.

### Example 2
- **Input:** `n = 3, edges = [[1,2],[2,0]]`
- **Output:** `[2,0,1]`
- **Explanation:** The image above shows the graph formed by the edges.
For node 0: after reversing the edges [2,0] and [1,2], it is possible to reach any other node starting from node 0.
So, answer[0] = 2.
For node 1: it is already possible to reach any other node starting from node 1.
So, answer[1] = 0.
For node 2: after reversing the edge [1, 2], it is possible to reach any other node starting from node 2.
So, answer[2] = 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Edge Reversals So Every Node Is Reachable**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[2,0],[2,1],[1,3]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,1,0,2]`.
4. **Verification:** The image above shows the graph formed by the edges.
For node 0: after reversing the edge [2,0], it is possible to reach any other node starting from node 0.
So, answer[0] = 1.
For node 1: after reversing the edge [2,1], it is possible to reach any other node starting from node 1.
So, answer[1] = 1.
For node 2: it is already possible to reach any other node starting from node 2.
So, answer[2] = 0.
For node 3: after reversing the edges [1,3] and [2,1], it is possible to reach any other node starting from node 3.
So, answer[3] = 2.

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
from collections import defaultdict
from typing import List

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((v, 0))  # u -> v: no reversal needed from u
            graph[v].append((u, 1))  # v -> u: reversing this edge is needed

        answer = [0] * n

        # First DFS: calculate reversals needed when starting at node 0
        def dfs(node, parent):
            for nei, cost in graph[node]:
                if nei == parent:
                    continue

                answer[0] += cost
                dfs(nei, node)

        dfs(0, -1)

        # Second DFS: calculate answers for all other starting nodes
        def reroot(node, parent):
            for nei, cost in graph[node]:
                if nei == parent:
                    continue

                if cost == 0:
                    answer[nei] = answer[node] + 1
                else:
                    answer[nei] = answer[node] - 1

                reroot(nei, node)

        reroot(0, -1)
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
- [3650. Minimum Cost Path with Edge Reversals](../../3501-4000/3650-minimum-cost-path-with-edge-reversals/)
- [2374. Node With Highest Edge Score](../../2001-2500/2374-node-with-highest-edge-score/)
- [2846. Minimum Edge Weight Equilibrium Queries in a Tree](../../2501-3000/2846-minimum-edge-weight-equilibrium-queries-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/)
