# LeetCode 797: All Paths From Source to Target

**LeetCode Problem #797 — All Paths From Source to Target**
Solve LeetCode All Paths From Source to Target using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Paths From Source to Target |
| LeetCode | #797 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

## Constraints
- `n == graph.length`
- `2 <= n <= 15`
- `0 <= graph[i][j] < n`
- `graph[i][j] != i` (i.e., there will be no self-loops).
- All the elements of `graph[i]` are **unique**.
- The input graph is **guaranteed** to be a **DAG**.

## Examples
### Example 1
- **Input:** `graph = [[1,2],[3],[3],[]]`
- **Output:** `[[0,1,3],[0,2,3]]`
- **Explanation:** There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

### Example 2
- **Input:** `graph = [[4,3,1],[3,2,4],[3],[4],[]]`
- **Output:** `[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **All Paths From Source to Target**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `graph = [[1,2],[3],[3],[]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,1,3],[0,2,3]]`.
4. **Verification:** There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1

        def dfs(node, path):
            if node == target:
                res.append(path[:])
                return

            for nxt in graph[node]:
                path.append(nxt)
                dfs(nxt, path)
                path.pop()

        dfs(0, [0])
        return res
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1786. Number of Restricted Paths From First to Last Node](../../1501-2000/1786-number-of-restricted-paths-from-first-to-last-node/)
- [2115. Find All Possible Recipes from Given Supplies](../../2001-2500/2115-find-all-possible-recipes-from-given-supplies/)
- [2920. Maximum Points After Collecting Coins From All Nodes](../../2501-3000/2920-maximum-points-after-collecting-coins-from-all-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/)
