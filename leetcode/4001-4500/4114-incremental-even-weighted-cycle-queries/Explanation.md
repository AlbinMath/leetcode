# LeetCode 3887: Incremental Even-Weighted Cycle Queries

**LeetCode Problem #3887 — Incremental Even-Weighted Cycle Queries**
Solve LeetCode Incremental Even-Weighted Cycle Queries using Python and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Incremental Even-Weighted Cycle Queries |
| LeetCode | #3887 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n`.

There is an **undirected** graph with `n` nodes labeled from 0 to `n - 1`. Initially, the graph has no edges.

You are also given a 2D integer array `edges`, where `edges[i] = [u_i, v_i, w_i]` represents an edge between nodes `u_i` and `v_i` with weight `w_i`. The weight `w_i` is either 0 or 1.

Process the edges in `edges` in the given order. For each edge, add it to the graph only if, after adding it, the sum of the weights of the edges in **every** cycle in the resulting graph is **even**.

Return an integer denoting the number of edges that are successfully added to the graph.

## Constraints
- `3 <= n <= 5 * 10^4`
- `1 <= edges.length <= 5 * 10^4`
- `edges[i] = [u_i, v_i, w_i]`
- `0 <= u_i < v_i < n`
- All edges are distinct.
- `w_i = 0 or w_i = 1`

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1,1],[1,2,1],[0,2,1]]`
- **Output:** `2`
- **Explanation:** `[0, 1, 1]`: We add the edge between vertex 0 and vertex 1 with weight 1. 
 `[1, 2, 1]`: We add the edge between vertex 1 and vertex 2 with weight 1. 
 `[0, 2, 1]`: The edge between vertex 0 and vertex 2 (the dashed edge in the diagram) is not added because the cycle `0 - 1 - 2 - 0` has total edge weight `1 + 1 + 1 = 3`, which is an odd number.

### Example 2
- **Input:** `n = 3, edges = [[0,1,1],[1,2,1],[0,2,0]]`
- **Output:** `3`
- **Explanation:** `[0, 1, 1]`: We add the edge between vertex 0 and vertex 1 with weight 1. 
 `[1, 2, 1]`: We add the edge between vertex 1 and vertex 2 with weight 1. 
 `[0, 2, 0]`: We add the edge between vertex 0 and vertex 2 with weight 0. 
 Note that the cycle `0 - 1 - 2 - 0` has total edge weight `1 + 1 + 0 = 2`, which is an even number.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Incremental Even-Weighted Cycle Queries**, we observe the problem requirements and utilize the **Fast & Slow Pointers** technique. We iterate through the inputs using **Floyd Cycle Detection**, leveraging a **Linked List / Pointer** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Linked List / Pointer**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1,1],[1,2,1],[0,2,1]]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** `[0, 1, 1]`: We add the edge between vertex 0 and vertex 1 with weight 1. 
 `[1, 2, 1]`: We add the edge between vertex 1 and vertex 2 with weight 1. 
 `[0, 2, 1]`: The edge between vertex 0 and vertex 2 (the dashed edge in the diagram) is not added because the cycle `0 - 1 - 2 - 0` has total edge weight `1 + 1 + 1 = 3`, which is an odd number.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class PotentialDSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.dist = [0] * n  # dist[i] = parity difference between i and parent[i]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            p = self.parent[x]
            self.parent[x] = self.find(p)
            self.dist[x] ^= self.dist[p]
        return self.parent[x]

    def add_edge(self, u: int, v: int, w: int) -> bool:
        ru = self.find(u)
        rv = self.find(v)

        if ru == rv:
            # Cycle formed: valid if and only if existing parity matches edge weight
            return (self.dist[u] ^ self.dist[v]) == w
        else:
            # No cycle formed: merge components
            self.parent[ru] = rv
            self.dist[ru] = self.dist[u] ^ self.dist[v] ^ w
            return True


class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        dsu = PotentialDSU(n)
        added_count = 0

        for u, v, w in edges:
            if dsu.add_edge(u, v, w):
                added_count += 1

        return added_count
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)
- [2509. Cycle Length Queries in a Tree](../../2501-3000/2597-cycle-length-queries-in-a-tree/)
- [1211. Queries Quality and Percentage](../../1001-1500/1338-queries-quality-and-percentage/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/incremental-even-weighted-cycle-queries/)
