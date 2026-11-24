# LeetCode 3928: Minimum Cost to Buy Apples II

**LeetCode Problem #3928 — Minimum Cost to Buy Apples II**
Solve LeetCode Minimum Cost to Buy Apples II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Buy Apples II |
| LeetCode | #3928 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and an integer array `prices` of length `n`, where `prices[i]` is the price of apples at shop `i`.

You are also given a 2D integer array `roads`, where `roads[i] = [u_i, v_i, cost_i, tax_i]` represents a **bidirectional** road:

`u_i` and `v_i` are the shops connected by the road. 
 `cost_i` is the cost to travel the road **without** carrying apples. 
 `tax_i` is the multiplier applied to `cost_i` when traveling **with** apples.

For each shop `i`, you can either:

Buy apples locally at shop `i` for `prices[i]`. 
 Travel **empty** to any shop `j` using **any** number of roads, buy apples for `prices[j]`, and return to shop `i` while carrying apples, paying `cost * tax` on each road used for the return trip.

The forward path, where you travel empty, and the return path may be **different**.

Return an integer array `ans` of length `n`, where `ans[i]` is the **minimum** total cost to buy apples starting from shop `i`.

## Constraints
- `1 <= n <= 1000`
- `prices.length == n`
- `1 <= prices[i] <= 10^9`
- `0 <= roads.length <= min(n &times; (n - 1) / 2, 2000)`
- `roads[i] = [u_i, v_i, cost_i, tax_i]`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `1 <= cost_i <= 10^9`
- `​​​​​​​1 <= tax_​​​​​​​i <= 100`​​​​​​​
- There are no **repeated** edges.

## Examples
### Example 1
- **Input:** `n = 2, prices = [8,3], roads = [[0,1,1,2]]`
- **Output:** `[6,3]`
- **Explanation:** Shop i 
 prices[i] 
 Shop j 
 `prices[j]` 
 cost_i 
 tax_i 
 Travel cost 
 Return cost 
 Total 
 Minimum 
 
 
 
 
 0 
 8 
 1 
 3 
 1 
 2 
 1 
 `1 * 2 = 2` 
 `1 + 2 + 3 = 6` 
 `min(8, 6) = 6` 
 
 
 1 
 3 
 0 
 8 
 1 
 2 
 1 
 `1 * 2 = 2` 
 `1 + 2 + 8 = 11` 
 `min(3, 11) = 3` 
 
 
 

 Thus, the answer is `[6, 3]`.

### Example 2
- **Input:** `n = 3, prices = [9,4,6], roads = [[0,1,1,3],[1,2,4,2]]`
- **Output:** `[8,4,6]`

### Example 3
- **Input:** `n = 3, prices = [10,11,1], roads = [[0,2,1,3],[1,2,3,4],[0,1,5,2]]`
- **Output:** `[5,11,1]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost to Buy Apples II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, prices = [8,3], roads = [[0,1,1,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,3]`.
4. **Verification:** Shop i 
 prices[i] 
 Shop j 
 `prices[j]` 
 cost_i 
 tax_i 
 Travel cost 
 Return cost 
 Total 
 Minimum 
 
 
 
 
 0 
 8 
 1 
 3 
 1 
 2 
 1 
 `1 * 2 = 2` 
 `1 + 2 + 3 = 6` 
 `min(8, 6) = 6` 
 
 
 1 
 3 
 0 
 8 
 1 
 2 
 1 
 `1 * 2 = 2` 
 `1 + 2 + 8 = 11` 
 `min(3, 11) = 3` 
 
 
 

 Thus, the answer is `[6, 3]`.

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
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        empty_graph = [[] for _ in range(n)]
        loaded_graph = [[] for _ in range(n)]

        for u, v, cost, taxi in roads:
            empty_graph[u].append((v, cost))
            empty_graph[v].append((u, cost))

            loaded_graph[u].append((v, cost * taxi))
            loaded_graph[v].append((u, cost * taxi))

        INF = float('inf')

        def dijkstra(graph, src):
            dist = [INF] * n
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                d, u = heapq.heappop(pq)

                if d != dist[u]:
                    continue

                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))

            return dist

        # Empty-trip distances from each starting shop.
        empty_dist = [dijkstra(empty_graph, i) for i in range(n)]

        # Return-trip distances to each starting shop.
        # The loaded graph is undirected, so these distances are symmetric.
        loaded_dist = [dijkstra(loaded_graph, i) for i in range(n)]

        ans = []

        for i in range(n):
            best = prices[i]

            for j in range(n):
                total = empty_dist[i][j] + prices[j] + loaded_dist[j][i]
                best = min(best, total)

            ans.append(best)

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
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1130-minimum-cost-tree-from-leaf-values/)
- [1217. Minimum Cost to Move Chips to The Same Position](../../1001-1500/1217-minimum-cost-to-move-chips-to-the-same-position/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/)
