# LeetCode 3613: Minimize Maximum Component Cost

**LeetCode Problem #3613 — Minimize Maximum Component Cost**
Solve LeetCode Minimize Maximum Component Cost using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Maximum Component Cost |
| LeetCode | #3613 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an undirected connected graph with n nodes labeled from 0 to n - 1 and a 2D integer array edges where edges[i] = [u_i, v_i, w_i] denotes an undirected edge between node u_i and node v_i with weight w_i , and an integer k .

You are allowed to remove any number of edges from the graph such that the resulting graph has **at most** k connected components.

The **cost** of a component is defined as the **maximum** edge weight in that component. If a component has no edges, its cost is 0.

Return the **minimum** possible value of the **maximum** cost among all components after such removals .

## Constraints
- `1 <= n <= 5 * 10^4`
- `0 <= edges.length <= 10^5`
- `edges[i].length == 3`
- `0 <= u_i, v_i < n`
- `1 <= w_i <= 10^6`
- `1 <= k <= n`
- The input graph is connected.

## Examples
### Example 1
- **Input:** `n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2`
- **Output:** `4`
- **Explanation:** Remove the edge between nodes 3 and 4 (weight 6). 
 The resulting components have costs of 0 and 4, so the overall maximum cost is 4.

### Example 2
- **Input:** `n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1`
- **Output:** `5`
- **Explanation:** No edge can be removed, since allowing only one component (`k = 1`) requires the graph to stay fully connected. 
 That single component&rsquo;s cost equals its largest edge weight, which is 5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimize Maximum Component Cost**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Remove the edge between nodes 3 and 4 (weight 6). 
 The resulting components have costs of 0 and 4, so the overall maximum cost is 4.

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

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx
            return True
        return False


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k >= n:
            return 0

        # Sort edges by weight in ascending order
        edges.sort(key=lambda e: e[2])

        dsu = DSU(n)
        components = n

        for u, v, w in edges:
            if dsu.union(u, v):
                components -= 1
                if components <= k:
                    return w

        return 0
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
- [2513. Minimize the Maximum of Two Arrays](../../2501-3000/2628-minimize-the-maximum-of-two-arrays/)
- [3419. Minimize the Maximum Edge Weight of Graph](../../3501-4000/3720-minimize-the-maximum-edge-weight-of-graph/)
- [4098. Minimize the Maximum Value of GCD-Connected Array](../../4001-4500/4462-minimize-the-maximum-value-of-gcd-connected-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-maximum-component-cost/)
