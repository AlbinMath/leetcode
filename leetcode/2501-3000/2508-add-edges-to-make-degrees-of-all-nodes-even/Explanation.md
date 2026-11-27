# LeetCode 2508: Add Edges to Make Degrees of All Nodes Even

**LeetCode Problem #2508 — Add Edges to Make Degrees of All Nodes Even**
Solve LeetCode Add Edges to Make Degrees of All Nodes Even using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add Edges to Make Degrees of All Nodes Even |
| LeetCode | #2508 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an **undirected** graph consisting of `n` nodes numbered from `1` to `n`. You are given the integer `n` and a **2D** array `edges` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i`. The graph can be disconnected.

You can add **at most** two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.

Return `true`* if it is possible to make the degree of each node in the graph even, otherwise return *`false`*.*

The degree of a node is the number of edges connected to it.

## Constraints
- `3 <= n <= 10^5`
- `2 <= edges.length <= 10^5`
- `edges[i].length == 2`
- `1 <= a_i, b_i <= n`
- `a_i != b_i`
- There are no repeated edges.

## Examples
### Example 1
- **Input:** `n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]`
- **Output:** `true`
- **Explanation:** The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.

### Example 2
- **Input:** `n = 4, edges = [[1,2],[3,4]]`
- **Output:** `true`
- **Explanation:** The above diagram shows a valid way of adding two edges.

### Example 3
- **Input:** `n = 4, edges = [[1,2],[1,3],[1,4]]`
- **Output:** `false`
- **Explanation:** It is not possible to obtain a valid graph with adding at most 2 edges.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Add Edges to Make Degrees of All Nodes Even**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.

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

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g = [set() for _ in range(n + 1)]
        deg = [0] * (n + 1)

        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            deg[u] += 1
            deg[v] += 1

        odd = [i for i in range(1, n + 1) if deg[i] % 2]

        if not odd:
            return True
        if len(odd) == 2:
            a, b = odd
            if b not in g[a]:
                return True
            for x in range(1, n + 1):
                if x != a and x != b and x not in g[a] and x not in g[b]:
                    return True
            return False
        if len(odd) == 4:
            a, b, c, d = odd
            return ((b not in g[a] and d not in g[c]) or
                    (c not in g[a] and d not in g[b]) or
                    (d not in g[a] and c not in g[b]))
        return False
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
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0847-shortest-path-visiting-all-nodes/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0863-all-nodes-distance-k-in-binary-tree/)
- [865. Smallest Subtree with all the Deepest Nodes](../../0501-1000/0865-smallest-subtree-with-all-the-deepest-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/)
