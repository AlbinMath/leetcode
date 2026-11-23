# LeetCode 4100: Minimum Cost Path With Even XOR Parity

**LeetCode Problem #4100 — Minimum Cost Path With Even XOR Parity**
Solve LeetCode Minimum Cost Path With Even XOR Parity using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path With Even XOR Parity |
| LeetCode | #4100 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a tree with `n` nodes numbered from 0 to `n - 1`, represented by a 2D integer array `edges`. Each `edges[i] = [u_i, v_i, c_i]` represents an edge between nodes `u_i` and `v_i` with cost `c_i`.

You are also given an integer array `values` of length `n`, where `values[i]` is the value of node `i`.

A path between two **distinct** nodes is **Balanced-XOR** if the bitwise XOR of the values of all nodes on the path, including both endpoints, has an **even** number of set bits .

The **cost** of a path is the sum of its edge costs.

Return the **minimum cost** of a Balanced-XOR path. If no such path exists, return -1.

The number 0 has zero set bits.

## Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] = [u_i, v_i, c_i​​​​​​​]`
 
 `0 <= u_i, v_i <= n - 1`
- `1 <= c_i <= 10^9`
- `values.length == n`
- `1 <= values[i] <= 10^9`
- `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[0,1,4],[0,2,6],[0,3,3],[3,4,5]], values = [3,1,7,1,3]`
- **Output:** `7`
- **Explanation:** Balanced-XOR Path 
 XOR Value 
 Total Cost 
 
 
 
 
 `1 - 0 - 2` 
 `1 XOR 3 XOR 7 = 5` 
 `4 + 6 = 10` 
 
 
 `1 - 0 - 3` 
 `1 XOR 3 XOR 1 = 3` 
 `4 + 3 = 7` 
 
 
 `1 - 0 - 3 - 4` 
 `1 XOR 3 XOR 1 XOR 3 = 0` 
 `4 + 3 + 5 = 12` 
 
 
 `2 - 0 - 3` 
 `7 XOR 3 XOR 1 = 5` 
 `6 + 3 = 9` 
 
 
 `2 - 0 - 3 - 4` 
 `7 XOR 3 XOR 1 XOR 3 = 6` 
 `6 + 3 + 5 = 14` 
 
 
 

 The minimum cost is 7, achieved by the path `1 - 0 - 3`. Thus, the answer is 7.

### Example 2
- **Input:** `edges = [[0,1,5],[1,2,10]], values = [1,7,3]`
- **Output:** `5`
- **Explanation:** Balanced-XOR Path 
 XOR Value 
 Total Cost 
 
 
 
 
 `0 - 1` 
 `1 XOR 7 = 6` 
 `5` 
 
 
 `0 - 1 - 2` 
 `1 XOR 7 XOR 3 = 5` 
 `5 + 10 = 15` 
 
 
 

 The minimum cost is 5, achieved by the path `0 - 1`. Thus, the answer is 5.

### Example 3
- **Input:** `edges = [[0,1,5],[0,2,7],[0,3,9]], values = [1,3,5,9]`
- **Output:** `-1`
- **Explanation:** Every path between two distinct nodes has an XOR value with an odd number of set bits. 
 Therefore, no Balanced-XOR path exists, so the answer is -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost Path With Even XOR Parity**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1,4],[0,2,6],[0,3,3],[3,4,5]], values = [3,1,7,1,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Balanced-XOR Path 
 XOR Value 
 Total Cost 
 
 
 
 
 `1 - 0 - 2` 
 `1 XOR 3 XOR 7 = 5` 
 `4 + 6 = 10` 
 
 
 `1 - 0 - 3` 
 `1 XOR 3 XOR 1 = 3` 
 `4 + 3 = 7` 
 
 
 `1 - 0 - 3 - 4` 
 `1 XOR 3 XOR 1 XOR 3 = 0` 
 `4 + 3 + 5 = 12` 
 
 
 `2 - 0 - 3` 
 `7 XOR 3 XOR 1 = 5` 
 `6 + 3 = 9` 
 
 
 `2 - 0 - 3 - 4` 
 `7 XOR 3 XOR 1 XOR 3 = 6` 
 `6 + 3 + 5 = 14` 
 
 
 

 The minimum cost is 7, achieved by the path `1 - 0 - 3`. Thus, the answer is 7.

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
class Solution(object):
    def minActivationCost(self, edges, values):
        n = len(values)
        INF = float('inf')
        p = [bin(v).count('1') & 1 for v in values]

        adj = [[] for _ in range(n)]
        for u, v, c in edges:
            adj[u].append((v, c))
            adj[v].append((u, c))

        # Iterative DFS to get parent array and a processing order
        parent = [-1] * n
        pcost = [0] * n
        order = []
        stack = [0]
        seen = [False] * n
        seen[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v, c in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    pcost[v] = c
                    stack.append(v)

        # cur[v][b] = min cost of a downward path starting at v with parity b
        cur = [[INF, INF] for _ in range(n)]
        for v in range(n):
            cur[v][p[v]] = 0

        ans = INF
        # Children are processed before parents (reverse of DFS order)
        for v in reversed(order):
            par = parent[v]
            if par == -1:
                continue
            w = pcost[v]
            cp = cur[par]
            pp = p[par]
            dv = cur[v]

            # 1) Join this branch with branches already merged into par
            for bc in (0, 1):
                if dv[bc] != INF and cp[bc] != INF:
                    total = cp[bc] + dv[bc] + w
                    if total < ans:
                        ans = total

            # 2) Only then merge this branch into par's best values
            for bc in (0, 1):
                if dv[bc] != INF:
                    nb = bc ^ pp
                    cost = dv[bc] + w
                    if cost < cp[nb]:
                        cp[nb] = cost

        return -1 if ans == INF else ans
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2686-minimum-cost-of-a-path-with-special-roads/)
- [3650. Minimum Cost Path with Edge Reversals](../../3501-4000/3887-minimum-cost-path-with-edge-reversals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-even-xor-parity/)
