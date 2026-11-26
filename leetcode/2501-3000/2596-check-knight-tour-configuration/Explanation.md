# LeetCode 2596: Check Knight Tour Configuration

**LeetCode Problem #2596 — Check Knight Tour Configuration**
Solve LeetCode Check Knight Tour Configuration using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check Knight Tour Configuration |
| LeetCode | #2596 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a knight on an `n x n` chessboard. In a valid configuration, the knight starts **at the top-left cell** of the board and visits every cell on the board **exactly once**.

You are given an `n x n` integer matrix `grid` consisting of distinct integers from the range `[0, n * n - 1]` where `grid[row][col]` indicates that the cell `(row, col)` is the `grid[row][col]^th` cell that the knight visited. The moves are **0-indexed**.

Return `true` *if* `grid` *represents a valid configuration of the knight's movements or* `false` *otherwise*.

**Note** that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.

## Constraints
- `n == grid.length == grid[i].length`
- `3 <= n <= 7`
- `0 <= grid[row][col] < n * n`
- All integers in `grid` are **unique**.

## Examples
### Example 1
- **Input:** `grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]`
- **Output:** `true`
- **Explanation:** The above diagram represents the grid. It can be shown that it is a valid configuration.

### Example 2
- **Input:** `grid = [[0,3,6],[5,8,1],[2,7,4]]`
- **Output:** `false`
- **Explanation:** The above diagram represents the grid. The 8^th move of the knight is not valid considering its position after the 7^th move.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check Knight Tour Configuration**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The above diagram represents the grid. It can be shown that it is a valid configuration.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False

        pos = [None] * (n * n)
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)

        for v in range(n * n - 1):
            r1, c1 = pos[v]
            r2, c2 = pos[v + 1]
            if abs(r1 - r2) * abs(c1 - c2) != 2:
                return False
        return True
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [688. Knight Probability in Chessboard](../../0501-1000/0688-knight-probability-in-chessboard/)
- [958. Check Completeness of a Binary Tree](../../0501-1000/0958-check-completeness-of-a-binary-tree/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-knight-tour-configuration/)
