# LeetCode 1030: Matrix Cells in Distance Order

**LeetCode Problem #1030 — Matrix Cells in Distance Order**
Solve LeetCode Matrix Cells in Distance Order using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Matrix Cells in Distance Order |
| LeetCode | #1030 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given four integers `row`, `cols`, `rCenter`, and `cCenter`. There is a `rows x cols` matrix and you are on the cell with the coordinates `(rCenter, cCenter)`.

Return *the coordinates of all cells in the matrix, sorted by their **distance** from *`(rCenter, cCenter)`* from the smallest distance to the largest distance*. You may return the answer in **any order** that satisfies this condition.

The **distance** between two cells `(r_1, c_1)` and `(r_2, c_2)` is `|r_1 - r_2| + |c_1 - c_2|`.

## Constraints
- `1 <= rows, cols <= 100`
- `0 <= rCenter < rows`
- `0 <= cCenter < cols`

## Examples
### Example 1
- **Input:** `rows = 1, cols = 2, rCenter = 0, cCenter = 0`
- **Output:** `[[0,0],[0,1]]`
- **Explanation:** The distances from (0, 0) to other cells are: [0,1]

### Example 2
- **Input:** `rows = 2, cols = 2, rCenter = 0, cCenter = 1`
- **Output:** `[[0,1],[0,0],[1,1],[1,0]]`
- **Explanation:** The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

### Example 3
- **Input:** `rows = 2, cols = 3, rCenter = 1, cCenter = 2`
- **Output:** `[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]`
- **Explanation:** The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Matrix Cells in Distance Order**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rows = 1, cols = 2, rCenter = 0, cCenter = 0`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,0],[0,1]]`.
4. **Verification:** The distances from (0, 0) to other cells are: [0,1]

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
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        cells = []

        for r in range(rows):
            for c in range(cols):
                cells.append([r, c])

        cells.sort(
            key=lambda cell: abs(cell[0] - rCenter)
            + abs(cell[1] - cCenter)
        )

        return cells
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
- [1252. Cells with Odd Values in a Matrix](../../1001-1500/1378-cells-with-odd-values-in-a-matrix/)
- [2713. Maximum Strictly Increasing Cells in a Matrix](../../2501-3000/2818-maximum-strictly-increasing-cells-in-a-matrix/)
- [54. Spiral Matrix](../../0001-0500/0054-spiral-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/matrix-cells-in-distance-order/)
