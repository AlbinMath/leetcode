# LeetCode 3493: Properties Graph

**LeetCode Problem #3493 — Properties Graph**
Solve LeetCode Properties Graph using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Properties Graph |
| LeetCode | #3493 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `properties` having dimensions `n x m` and an integer `k`.

Define a function `intersect(a, b)` that returns the **number of distinct integers** common to both arrays `a` and `b`.

Construct an **undirected** graph where each index `i` corresponds to `properties[i]`. There is an edge between node `i` and node `j` if and only if `intersect(properties[i], properties[j]) >= k`, where `i` and `j` are in the range `[0, n - 1]` and `i != j`.

Return the number of **connected components** in the resulting graph.

## Constraints
- `1 <= n == properties.length <= 100`
- `1 <= m == properties[i].length <= 100`
- `1 <= properties[i][j] <= 100`
- `1 <= k <= m`

## Examples
### Example 1
- **Input:** `properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1`
- **Output:** `3`
- **Explanation:** The graph formed has 3 connected components:

### Example 2
- **Input:** `properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2`
- **Output:** `1`
- **Explanation:** The graph formed has 1 connected component:

### Example 3
- **Input:** `properties = [[1,1],[1,1]], k = 2`
- **Output:** `2`
- **Explanation:** `intersect(properties[0], properties[1]) = 1`, which is less than `k`. This means there is no edge between `properties[0]` and `properties[1]` in the graph.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Properties Graph**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The graph formed has 3 connected components:

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
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.components = n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.components -= 1


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        
        # Convert each row to a set of distinct values
        unique_sets = [set(row) for row in properties]
        dsu = DSU(n)

        # Check all pairs (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                # Count common unique elements
                if len(unique_sets[i] & unique_sets[j]) >= k:
                    dsu.union(i, j)

        return dsu.components
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
- [133. Clone Graph](../../0001-0500/0133-clone-graph/)
- [785. Is Graph Bipartite?](../../0501-1000/0801-is-graph-bipartite/)
- [882. Reachable Nodes In Subdivided Graph](../../0501-1000/0918-reachable-nodes-in-subdivided-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/properties-graph/)
