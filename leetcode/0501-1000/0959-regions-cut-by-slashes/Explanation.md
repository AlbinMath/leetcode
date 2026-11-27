# LeetCode 959: Regions Cut By Slashes

**LeetCode Problem #959 — Regions Cut By Slashes**
Solve LeetCode Regions Cut By Slashes using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Regions Cut By Slashes |
| LeetCode | #959 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An `n x n` grid is composed of `1 x 1` squares where each `1 x 1` square consists of a `'/'`, `'\'`, or blank space `' '`. These characters divide the square into contiguous regions.

Given the grid `grid` represented as a string array, return *the number of regions*.

Note that backslash characters are escaped, so a `'\'` is represented as `'\\'`.

## Constraints
- `n == grid.length == grid[i].length`
- `1 <= n <= 30`
- `grid[i][j]` is either `'/'`, `'\'`, or `' '`.

## Examples
### Example 1
- **Input:** `grid = [" /","/ "]`
- **Output:** `2`

### Example 2
- **Input:** `grid = [" /"," "]`
- **Output:** `1`

### Example 3
- **Input:** `grid = ["/\\","\\/"]`
- **Output:** `5`
- **Explanation:** Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Regions Cut By Slashes**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [" /","/ "]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.count -= 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(4 * n * n)

        def get_index(r: int, c: int, k: int) -> int:
            return (r * n + c) * 4 + k

        for r in range(n):
            for c in range(n):
                ch = grid[r][c]
                # 1. Connect within the current square
                if ch == ' ':
                    dsu.union(get_index(r, c, 0), get_index(r, c, 1))
                    dsu.union(get_index(r, c, 1), get_index(r, c, 2))
                    dsu.union(get_index(r, c, 2), get_index(r, c, 3))
                elif ch == '/':
                    dsu.union(get_index(r, c, 0), get_index(r, c, 3))
                    dsu.union(get_index(r, c, 1), get_index(r, c, 2))
                elif ch == '\\':
                    dsu.union(get_index(r, c, 0), get_index(r, c, 1))
                    dsu.union(get_index(r, c, 2), get_index(r, c, 3))

                # 2. Connect with adjacent squares
                # North-South connection
                if r + 1 < n:
                    dsu.union(get_index(r, c, 2), get_index(r + 1, c, 0))
                # East-West connection
                if c + 1 < n:
                    dsu.union(get_index(r, c, 1), get_index(r, c + 1, 3))

        return dsu.count
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
- [130. Surrounded Regions](../../0001-0500/0130-surrounded-regions/)
- [675. Cut Off Trees for Golf Event](../../0501-1000/0675-cut-off-trees-for-golf-event/)
- [1547. Minimum Cost to Cut a Stick](../../1501-2000/1547-minimum-cost-to-cut-a-stick/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/regions-cut-by-slashes/)
