# LeetCode 2316: Count Unreachable Pairs of Nodes in an Undirected Graph

**LeetCode Problem #2316 — Count Unreachable Pairs of Nodes in an Undirected Graph**
Solve LeetCode Count Unreachable Pairs of Nodes in an Undirected Graph using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unreachable Pairs of Nodes in an Undirected Graph |
| LeetCode | #2316 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`. There is an **undirected** graph with `n` nodes, numbered from `0` to `n - 1`. You are given a 2D integer array `edges` where `edges[i] = [a_i, b_i]` denotes that there exists an **undirected** edge connecting nodes `a_i` and `b_i`.

Return *the **number of pairs** of different nodes that are **unreachable** from each other*.

## Constraints
- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- There are no repeated edges.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1],[0,2],[1,2]]`
- **Output:** `0`
- **Explanation:** There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

### Example 2
- **Input:** `n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]`
- **Output:** `14`
- **Explanation:** There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Unreachable Pairs of Nodes in an Undirected Graph**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1],[0,2],[1,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

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
        self.size = [1] * n

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
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)

        # Total possible pairs
        total_pairs = n * (n - 1) // 2

        # Subtract pairs that are in the same component
        reachable_pairs = 0
        for i in range(n):
            if dsu.parent[i] == i:
                s = dsu.size[i]
                reachable_pairs += s * (s - 1) // 2

        return total_pairs - reachable_pairs
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
- [1782. Count Pairs Of Nodes](../../1501-2000/1782-count-pairs-of-nodes/)
- [2876. Count Visited Nodes in a Directed Graph](../../2501-3000/2876-count-visited-nodes-in-a-directed-graph/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
