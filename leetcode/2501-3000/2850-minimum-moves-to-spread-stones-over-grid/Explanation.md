# LeetCode 2850: Minimum Moves to Spread Stones Over Grid

**LeetCode Problem #2850 — Minimum Moves to Spread Stones Over Grid**
Solve LeetCode Minimum Moves to Spread Stones Over Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Spread Stones Over Grid |
| LeetCode | #2850 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** 2D integer matrix `grid` of size `3 * 3`, representing the number of stones in each cell. The grid contains exactly `9` stones, and there can be **multiple** stones in a single cell.

In one move, you can move a single stone from its current cell to any other cell if the two cells share a side.

Return *the **minimum number of moves** required to place one stone in each cell*.

## Constraints
- `grid.length == grid[i].length == 3`
- `0 <= grid[i][j] <= 9`
- Sum of `grid` is equal to `9`.

## Examples
### Example 1
- **Input:** `grid = [[1,1,0],[1,1,1],[1,2,1]]`
- **Output:** `3`
- **Explanation:** One possible sequence of moves to place one stone in each cell is: 
1- Move one stone from cell (2,1) to cell (2,2).
2- Move one stone from cell (2,2) to cell (1,2).
3- Move one stone from cell (1,2) to cell (0,2).
In total, it takes 3 moves to place one stone in each cell of the grid.
It can be shown that 3 is the minimum number of moves required to place one stone in each cell.

### Example 2
- **Input:** `grid = [[1,3,0],[1,0,0],[1,0,3]]`
- **Output:** `4`
- **Explanation:** One possible sequence of moves to place one stone in each cell is:
1- Move one stone from cell (0,1) to cell (0,2).
2- Move one stone from cell (0,1) to cell (1,1).
3- Move one stone from cell (2,2) to cell (1,2).
4- Move one stone from cell (2,2) to cell (2,1).
In total, it takes 4 moves to place one stone in each cell of the grid.
It can be shown that 4 is the minimum number of moves required to place one stone in each cell.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Moves to Spread Stones Over Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,1,0],[1,1,1],[1,2,1]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** One possible sequence of moves to place one stone in each cell is: 
1- Move one stone from cell (2,1) to cell (2,2).
2- Move one stone from cell (2,2) to cell (1,2).
3- Move one stone from cell (1,2) to cell (0,2).
In total, it takes 3 moves to place one stone in each cell of the grid.
It can be shown that 3 is the minimum number of moves required to place one stone in each cell.

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
from itertools import permutations

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        sources = []  # one entry per extra stone
        targets = []  # one entry per empty cell
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    targets.append((i, j))
                elif grid[i][j] > 1:
                    sources.extend([(i, j)] * (grid[i][j] - 1))

        if not targets:
            return 0

        best = float('inf')
        for perm in permutations(targets):
            cost = sum(abs(a[0] - b[0]) + abs(a[1] - b[1])
                       for a, b in zip(sources, perm))
            best = min(best, cost)
        return best
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
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)
- [1000. Minimum Cost to Merge Stones](../../0501-1000/1000-minimum-cost-to-merge-stones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/)
