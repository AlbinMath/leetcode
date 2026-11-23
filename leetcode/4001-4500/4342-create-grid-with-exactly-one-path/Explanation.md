# LeetCode 3963: Create Grid With Exactly One Path

**LeetCode Problem #3963 — Create Grid With Exactly One Path**
Solve LeetCode Create Grid With Exactly One Path using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Grid With Exactly One Path |
| LeetCode | #3963 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `m` and `n`, representing the number of rows and columns of a grid.

Construct **any** `m x n` grid consisting only of the characters `'.'` and `'#'`, where:

`'.'` represents a free cell. 
 `'#'` represents an obstacle cell.

A **valid path** is a sequence of free cells that:

Starts at the top-left cell `(0, 0)`. 
 Ends at the bottom-right cell `(m - 1, n - 1)`. 
 Moves only:
 
 Right, from `(i, j)` to `(i, j + 1)`, or 
 Down, from `(i, j)` to `(i + 1, j)`.

Return any grid such that there is **exactly one valid path** from the top-left cell to the bottom-right cell.

## Constraints
- `1 <= m, n <= 25`

## Examples
### Example 1
- **Input:** `m = 2, n = 3`
- **Output:** `["..#","#.."]`
- **Explanation:** The only valid path is: `(0,0) &rarr; (0,1) &rarr; (1,1) &rarr; (1,2)`

### Example 2
- **Input:** `m = 3, n = 3`
- **Output:** `["..#","#..","##."]`
- **Explanation:** The only valid path is: `(0,0) &rarr; (0,1) &rarr; (1,1) &rarr; (1,2) &rarr; (2,2)`

### Example 3
- **Input:** `m = 1, n = 4`
- **Output:** `["...."]`
- **Explanation:** The only valid path is: `(0,0) &rarr; (0,1) &rarr; (0,2) &rarr; (0,3)`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Create Grid With Exactly One Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 2, n = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["..#","#.."]`.
4. **Verification:** The only valid path is: `(0,0) &rarr; (0,1) &rarr; (1,1) &rarr; (1,2)`

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
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = [['#'] * n for _ in range(m)]

        for i in range(m):
            grid[i][0] = '.'

        for j in range(n):
            grid[m - 1][j] = '.'

        return [''.join(row) for row in grid]
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
- [3988. Create Grid With Exactly K Paths I](../../4001-4500/4343-create-grid-with-exactly-k-paths-i/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [3950. Exactly One Consecutive Set Bits Pair](../../4001-4500/4307-exactly-one-consecutive-set-bits-pair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-grid-with-exactly-one-path/)
