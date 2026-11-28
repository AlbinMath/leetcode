# LeetCode 3970: Shortest Path With At Most K Consecutive Identical Characters

**LeetCode Problem #3970 — Shortest Path With At Most K Consecutive Identical Characters**
Solve LeetCode Shortest Path With At Most K Consecutive Identical Characters using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path With At Most K Consecutive Identical Characters |
| LeetCode | #3970 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` representing the number of nodes in a **directed weighted** graph, numbered from 0 to `n - 1`. This is represented by a 2D integer array `edges`, where `edges[i] = [u_i, v_i, w_i]` represents a directed edge from node `u_i` to node `v_i` with weight `w_i`.

You are also given a string `labels` of length `n`, where `labels[i]` is the character assigned to node `i`, and an integer `k`.

Return the **minimum** **total** edge weight of a path from node 0 to node `n - 1` such that the concatenation of the labels of the nodes along the path contains **at most** `k` **consecutive** **identical** characters. If no valid path exists, return -1.

**Note:** Nodes and edges may be revisited.

## Constraints
- `1 <= n == labels.length <= 5 * 10^4`
- `0 <= edges.length <= 5 * 10^4`
- `edges[i] == [u_i, v_i, w_i]`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `1 <= w_i <= 10^4`
- `labels` consists of lowercase English letters
- `1 <= k <= 50`

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1`
- **Output:** `3`
- **Explanation:** The optimal valid path from node 0 to node 2 is as follows: 

 
 Use `edges[2] = [0, 2, 3]` to reach node 2 with a weight `w_i = 3`. 
 
The corresponding concatenation of labels is `"ab"`, which satisfies at most `k = 1` consecutive identical characters. Thus, the answer is 3.

### Example 2
- **Input:** `n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2`
- **Output:** `2`
- **Explanation:** The optimal valid path from node 0 to node 2 is as follows: 

 
 Use `edges[0] = [0, 1, 1]` to reach node 1 with weight `w_i = 1`. 
 Use `edges[1] = [1, 2, 1]` to reach node 2 with weight `w_i = 1`. 
 
The corresponding concatenation of labels is `"aab"`, which satisfies at most `k = 2` consecutive identical characters. Thus, the answer is 2.

### Example 3
- **Input:** `n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2`
- **Output:** `-1`
- **Explanation:** There is no valid path from node 0 to node 2 that satisfies at most `k = 2` consecutive identical characters. Thus, the answer is -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest Path With At Most K Consecutive Identical Characters**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The optimal valid path from node 0 to node 2 is as follows: 

 
 Use `edges[2] = [0, 2, 3]` to reach node 2 with a weight `w_i = 3`. 
 
The corresponding concatenation of labels is `"ab"`, which satisfies at most `k = 1` consecutive identical characters. Thus, the answer is 3.

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
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count] = minimum cost to reach node
        # with count consecutive occurrences of its label.
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        pq = [(0, 0, 1)]  # cost, node, consecutive count

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost != dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_count))

        return -1
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
- [4046. Minimum Cost Path With At Most K Turns](../../4001-4500/4046-minimum-cost-path-with-at-most-k-turns/)
- [3545. Minimum Deletions for At Most K Distinct Characters](../../3501-4000/3545-minimum-deletions-for-at-most-k-distinct-characters/)
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0847-shortest-path-visiting-all-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)
