# LeetCode 2257: Count Unguarded Cells in the Grid

**LeetCode Problem #2257 — Count Unguarded Cells in the Grid**
Solve LeetCode Count Unguarded Cells in the Grid using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unguarded Cells in the Grid |
| LeetCode | #2257 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. You are also given two 2D integer arrays `guards` and `walls` where `guards[i] = [row_i, col_i]` and `walls[j] = [row_j, col_j]` represent the positions of the `i^th` guard and `j^th` wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless **obstructed** by a wall or another guard. A cell is **guarded** if there is **at least** one guard that can see it.

Return* the number of unoccupied cells that are **not** **guarded**.*

## Constraints
- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- `1 <= guards.length, walls.length <= 5 * 10^4`
- `2 <= guards.length + walls.length <= m * n`
- `guards[i].length == walls[j].length == 2`
- `0 <= row_i, row_j < m`
- `0 <= col_i, col_j < n`
- All the positions in `guards` and `walls` are **unique**.

## Examples
### Example 1
- **Input:** `m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]`
- **Output:** `7`
- **Explanation:** The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

### Example 2
- **Input:** `m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]`
- **Output:** `4`
- **Explanation:** The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Unguarded Cells in the Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countUnguarded = function(m, n, guards, walls) {
    // 0 = unguarded, 1 = guard, 2 = wall, 3 = guarded
    const grid = Array.from({ length: m }, () => new Uint8Array(n));
    
    for (const [r, c] of guards) grid[r][c] = 1;
    for (const [r, c] of walls) grid[r][c] = 2;
    
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    
    for (const [r, c] of guards) {
        for (const [dr, dc] of directions) {
            let nr = r + dr;
            let nc = c + dc;
            while (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                if (grid[nr][nc] === 1 || grid[nr][nc] === 2) {
                    break;
                }
                grid[nr][nc] = 3;
                nr += dr;
                nc += dc;
            }
        }
    }
    
    let unguarded = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 0) unguarded++;
        }
    }
    
    return unguarded;
};
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
- [2617. Minimum Number of Visited Cells in a Grid](../../2501-3000/2617-minimum-number-of-visited-cells-in-a-grid/)
- [3276. Select Cells in Grid With Maximum Score](../../3001-3500/3276-select-cells-in-grid-with-maximum-score/)
- [3797. Count Routes to Climb a Rectangular Grid](../../3501-4000/3797-count-routes-to-climb-a-rectangular-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)
