# LeetCode 3071: Minimum Operations to Write the Letter Y on a Grid

**LeetCode Problem #3071 — Minimum Operations to Write the Letter Y on a Grid**
Solve LeetCode Minimum Operations to Write the Letter Y on a Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Write the Letter Y on a Grid |
| LeetCode | #3071 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** `n x n` grid where `n` is odd, and `grid[r][c]` is `0`, `1`, or `2`.

We say that a cell belongs to the Letter **Y** if it belongs to one of the following:

The diagonal starting at the top-left cell and ending at the center cell of the grid. 
 The diagonal starting at the top-right cell and ending at the center cell of the grid. 
 The vertical line starting at the center cell and ending at the bottom border of the grid.

The Letter **Y** is written on the grid if and only if:

All values at cells belonging to the Y are equal. 
 All values at cells not belonging to the Y are equal. 
 The values at cells belonging to the Y are different from the values at cells not belonging to the Y.

Return *the **minimum** number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to* `0`*,* `1`*,* *or* `2`*.*

## Constraints
- `3 <= n <= 49 `
- `n == grid.length == grid[i].length`
- `0 <= grid[i][j] <= 2`
- `n` is odd.

## Examples
### Example 1
- **Input:** `grid = [[1,2,2],[1,1,0],[0,1,0]]`
- **Output:** `3`
- **Explanation:** We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.
It can be shown that 3 is the minimum number of operations needed to write Y on the grid.

### Example 2
- **Input:** `grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]`
- **Output:** `12`
- **Explanation:** We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 0 while those that do not belong to Y are equal to 2. 
It can be shown that 12 is the minimum number of operations needed to write Y on the grid.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Write the Letter Y on a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,2],[1,1,0],[0,1,0]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.
It can be shown that 3 is the minimum number of operations needed to write Y on the grid.

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
class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        n = len(grid)
        mid = n // 2
        
        y_counts = [0, 0, 0]
        bg_counts = [0, 0, 0]
        
        for r in range(n):
            for c in range(n):
                is_y = (r <= mid and (r == c or r + c == n - 1)) or (r > mid and c == mid)
                if is_y:
                    y_counts[grid[r][c]] += 1
                else:
                    bg_counts[grid[r][c]] += 1
                    
        total_y = sum(y_counts)
        total_bg = sum(bg_counts)
        min_ops = n * n
        
        for y_val in range(3):
            for bg_val in range(3):
                if y_val != bg_val:
                    ops = (total_y - y_counts[y_val]) + (total_bg - bg_counts[bg_val])
                    min_ops = min(min_ops, ops)
                    
        return min_ops
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
- [2033. Minimum Operations to Make a Uni-Value Grid](../../2001-2500/2033-minimum-operations-to-make-a-uni-value-grid/)
- [2998. Minimum Number of Operations to Make X and Y Equal](../../2501-3000/2998-minimum-number-of-operations-to-make-x-and-y-equal/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/)
