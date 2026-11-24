# LeetCode 3127: Make a Square with the Same Color

**LeetCode Problem #3127 — Make a Square with the Same Color**
Solve LeetCode Make a Square with the Same Color using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make a Square with the Same Color |
| LeetCode | #3127 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D matrix `grid` of size `3 x 3` consisting only of characters `'B'` and `'W'`. Character `'W'` represents the white color , and character `'B'` represents the black color .

Your task is to change the color of **at most one** cell so that the matrix has a `2 x 2` square where all cells are of the same color.

Return `true` if it is possible to create a `2 x 2` square of the same color, otherwise, return `false`.

.grid-container {
 display: grid;
 grid-template-columns: 30px 30px 30px;
 padding: 10px;
}
.grid-item {
 background-color: black;
 border: 1px solid gray;
 height: 30px;
 font-size: 30px;
 text-align: center;
}
.grid-item-white {
 background-color: white;
}

## Constraints
- `grid.length == 3`
- `grid[i].length == 3`
- `grid[i][j]` is either `'W'` or `'B'`.

## Examples
### Example 1
- **Input:** `grid = [["B","W","B"],["B","W","W"],["B","W","B"]]`
- **Output:** `true`
- **Explanation:** It can be done by changing the color of the `grid[0][2]`.

### Example 2
- **Input:** `grid = [["B","W","B"],["W","B","W"],["B","W","B"]]`
- **Output:** `false`
- **Explanation:** It cannot be done by changing at most one cell.

### Example 3
- **Input:** `grid = [["B","W","B"],["B","W","W"],["B","W","W"]]`
- **Output:** `true`
- **Explanation:** The `grid` already contains a `2 x 2` square of the same color.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make a Square with the Same Color**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [["B","W","B"],["B","W","W"],["B","W","B"]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** It can be done by changing the color of the `grid[0][2]`.

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
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                blacks = sum(grid[r + dr][c + dc] == 'B'
                             for dr in (0, 1) for dc in (0, 1))
                if blacks != 2:
                    return True
        return False
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
- [1812. Determine Color of a Chessboard Square](../../1501-2000/1812-determine-color-of-a-chessboard-square/)
- [2038. Remove Colored Pieces if Both Neighbors are the Same Color](../../2001-2500/2038-remove-colored-pieces-if-both-neighbors-are-the-same-color/)
- [221. Maximal Square](../../0001-0500/0221-maximal-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-a-square-with-the-same-color/)
