# LeetCode 3537: Fill a Special Grid

**LeetCode Problem #3537 — Fill a Special Grid**
Solve LeetCode Fill a Special Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fill a Special Grid |
| LeetCode | #3537 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a non-negative integer ` n ` representing a `2^n x 2^n` grid. You must fill the grid with integers from 0 to `2^2n - 1` to make it **special**. A grid is **special** if it satisfies **all** the following conditions:

All numbers in the top-right quadrant are smaller than those in the bottom-right quadrant. 
 All numbers in the bottom-right quadrant are smaller than those in the bottom-left quadrant. 
 All numbers in the bottom-left quadrant are smaller than those in the top-left quadrant. 
 Each of its quadrants is also a special grid.

Return the **special** `2^n x 2^n` grid.

**Note**: Any 1x1 grid is special.

## Constraints
- `0 <= n <= 10`

## Examples
### Example 1
- **Input:** `n = 0`
- **Output:** `[[0]]`
- **Explanation:** The only number that can be placed is 0, and there is only one possible position in the grid.

### Example 2
- **Input:** `n = 1`
- **Output:** `[[3,0],[2,1]]`
- **Explanation:** The numbers in each quadrant are: 

 
 Top-right: 0 
 Bottom-right: 1 
 Bottom-left: 2 
 Top-left: 3 
 

 Since `0 < 1 < 2 < 3`, this satisfies the given

### Example 3
- **Input:** `n = 2`
- **Output:** `[[15,12,3,0],[14,13,2,1],[11,8,7,4],[10,9,6,5]]`
- **Explanation:** The numbers in each quadrant are: 

 
 Top-right: 3, 0, 2, 1 
 Bottom-right: 7, 4, 6, 5 
 Bottom-left: 11, 8, 10, 9 
 Top-left: 15, 12, 14, 13 
 `max(3, 0, 2, 1) < min(7, 4, 6, 5)` 
 `max(7, 4, 6, 5) < min(11, 8, 10, 9)` 
 `max(11, 8, 10, 9) < min(15, 12, 14, 13)` 
 

 This satisfies the first three requirements. Additionally, each quadrant is also a special grid. Thus, this is a special grid.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Fill a Special Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 0`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0]]`.
4. **Verification:** The only number that can be placed is 0, and there is only one possible position in the grid.

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
    def specialGrid(self, n):
        size = 1 << n
        grid = [[0] * size for _ in range(size)]

        def fill(r, c, s, base):
            if s == 1:
                grid[r][c] = base
                return
            if s == 2:
                grid[r][c + 1] = base
                grid[r + 1][c + 1] = base + 1
                grid[r + 1][c] = base + 2
                grid[r][c] = base + 3
                return
            h = s // 2
            q = h * h
            fill(r, c + h, h, base)
            fill(r + h, c + h, h, base + q)
            fill(r + h, c, h, base + 2 * q)
            fill(r, c, h, base + 3 * q)

        fill(0, 0, size, 0)
        return grid
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
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1001. Grid Illumination](../../1001-1500/1001-grid-illumination/)
- [1260. Shift 2D Grid](../../1001-1500/1260-shift-2d-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fill-a-special-grid/)
