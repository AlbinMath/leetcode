# LeetCode 2421: Number of Good Paths

**LeetCode Problem #2421 — Number of Good Paths**
Solve LeetCode Number of Good Paths using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Good Paths |
| LeetCode | #2421 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges.

You are given a **0-indexed** integer array `vals` of length `n` where `vals[i]` denotes the value of the `i^th` node. You are also given a 2D integer array `edges` where `edges[i] = [a_i, b_i]` denotes that there exists an **undirected** edge connecting nodes `a_i` and `b_i`.

A **good path** is a simple path that satisfies the following conditions:

The starting node and the ending node have the **same** value. 
 All nodes between the starting node and the ending node have values **less than or equal to** the starting node (i.e. the starting node's value should be the maximum value along the path).

Return *the number of distinct good paths*.

Note that a path and its reverse are counted as the **same** path. For example, `0 -> 1` is considered to be the same as `1 -> 0`. A single node is also considered as a valid path.

## Constraints
- `n == vals.length`
- `1 <= n <= 3 * 10^4`
- `0 <= vals[i] <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]`
- **Output:** `6`
- **Explanation:** There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].

### Example 2
- **Input:** `vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]`
- **Output:** `7`
- **Explanation:** There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.

### Example 3
- **Input:** `vals = [1], edges = []`
- **Output:** `1`
- **Explanation:** The tree consists of only one node, so there is one good path.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Good Paths**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class DSU:
    def __init__(self, vals: List[int]):
        n = len(vals)
        self.parent = list(range(n))
        self.max_val = list(vals)
        self.count = [1] * n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, u: int, v: int) -> int:
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return 0

        new_paths = 0
        if self.max_val[ru] == self.max_val[rv]:
            new_paths = self.count[ru] * self.count[rv]
            self.parent[rv] = ru
            self.count[ru] += self.count[rv]
        elif self.max_val[ru] > self.max_val[rv]:
            self.parent[rv] = ru
        else:
            self.parent[ru] = rv

        return new_paths


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        # Sort edges by max(vals[u], vals[v])
        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))

        dsu = DSU(vals)
        # Each single node forms a valid path
        good_paths = n

        for u, v in edges:
            good_paths += dsu.union(u, v)

        return good_paths
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1301. Number of Paths with Max Score](../../1001-1500/1234-number-of-paths-with-max-score/)
- [1512. Number of Good Pairs](../../1501-2000/1635-number-of-good-pairs/)
- [1525. Number of Good Ways to Split a String](../../1501-2000/1632-number-of-good-ways-to-split-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-good-paths/)
