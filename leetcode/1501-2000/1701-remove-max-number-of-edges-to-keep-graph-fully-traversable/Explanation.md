# LeetCode 1579: Remove Max Number of Edges to Keep Graph Fully Traversable

**LeetCode Problem #1579 — Remove Max Number of Edges to Keep Graph Fully Traversable**
Solve LeetCode Remove Max Number of Edges to Keep Graph Fully Traversable using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Max Number of Edges to Keep Graph Fully Traversable |
| LeetCode | #1579 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob have an undirected graph of `n` nodes and three types of edges:

Type 1: Can be traversed by Alice only. 
 Type 2: Can be traversed by Bob only. 
 Type 3: Can be traversed by both Alice and Bob.

Given an array `edges` where `edges[i] = [type_i, u_i, v_i]` represents a bidirectional edge of type `type_i` between nodes `u_i` and `v_i`, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return *the maximum number of edges you can remove, or return* `-1` *if Alice and Bob cannot fully traverse the graph.*

## Constraints
- `1 <= n <= 10^5`
- `1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)`
- `edges[i].length == 3`
- `1 <= type_i <= 3`
- `1 <= u_i < v_i <= n`
- All tuples `(type_i, u_i, v_i)` are distinct.

## Examples
### Example 1
- **Input:** `n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]`
- **Output:** `2`
- **Explanation:** If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

### Example 2
- **Input:** `n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]`
- **Output:** `0`
- **Explanation:** Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

### Example 3
- **Input:** `n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]`
- **Output:** `-1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Max Number of Edges to Keep Graph Fully Traversable**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.components -= 1
            return True
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_dsu = DSU(n)
        bob_dsu = DSU(n)
        edges_used = 0

        # Step 1: Greedily add Type 3 edges first
        for edge_type, u, v in edges:
            if edge_type == 3:
                a_used = alice_dsu.union(u, v)
                b_used = bob_dsu.union(u, v)
                if a_used or b_used:
                    edges_used += 1

        # Step 2: Add Type 1 (Alice) and Type 2 (Bob) edges
        for edge_type, u, v in edges:
            if edge_type == 1:
                if alice_dsu.union(u, v):
                    edges_used += 1
            elif edge_type == 2:
                if bob_dsu.union(u, v):
                    edges_used += 1

        # Step 3: Check if both graphs are fully connected
        if alice_dsu.components == 1 and bob_dsu.components == 1:
            return len(edges) - edges_used

        return -1
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [807. Max Increase to Keep City Skyline](../../0501-1000/0825-max-increase-to-keep-city-skyline/)
- [2259. Remove Digit From Number to Maximize Result](../../2001-2500/2337-remove-digit-from-number-to-maximize-result/)
- [1301. Number of Paths with Max Score](../../1001-1500/1234-number-of-paths-with-max-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/)
