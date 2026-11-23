# LeetCode 1926: Nearest Exit from Entrance in Maze

**LeetCode Problem #1926 — Nearest Exit from Entrance in Maze**
Solve LeetCode Nearest Exit from Entrance in Maze using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Nearest Exit from Entrance in Maze |
| LeetCode | #1926 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` matrix `maze` (**0-indexed**) with empty cells (represented as `'.'`) and walls (represented as `'+'`). You are also given the `entrance` of the maze, where `entrance = [entrance_row, entrance_col]` denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell **up**, **down**, **left**, or **right**. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the **nearest exit** from the `entrance`. An **exit** is defined as an **empty cell** that is at the **border** of the `maze`. The `entrance` **does not count** as an exit.

Return *the **number of steps** in the shortest path from the *`entrance`* to the nearest exit, or *`-1`* if no such path exists*.

## Constraints
- `maze.length == m`
- `maze[i].length == n`
- `1 <= m, n <= 100`
- `maze[i][j]` is either `'.'` or `'+'`.
- `entrance.length == 2`
- `0 <= entrance_row < m`
- `0 <= entrance_col < n`
- `entrance` will always be an empty cell.

## Examples
### Example 1
- **Input:** `maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]`
- **Output:** `1`
- **Explanation:** There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

### Example 2
- **Input:** `maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]`
- **Output:** `2`
- **Explanation:** There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

### Example 3
- **Input:** `maze = [[".","+"]], entrance = [0,0]`
- **Output:** `-1`
- **Explanation:** There are no exits in this maze.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Nearest Exit from Entrance in Maze**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var nearestExit = function(maze, entrance) {
    const m = maze.length;
    const n = maze[0].length;

    const queue = [[entrance[0], entrance[1], 0]];
    let front = 0;

    // Mark entrance as visited
    maze[entrance[0]][entrance[1]] = '+';

    const directions = [
        [-1, 0], // Up
        [1, 0],  // Down
        [0, -1], // Left
        [0, 1]   // Right
    ];

    while (front < queue.length) {
        const [row, col, steps] = queue[front++];

        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;

            // Check boundaries
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                continue;
            }

            // Skip walls and visited cells
            if (maze[nr][nc] === '+') {
                continue;
            }

            // Check whether this cell is an exit
            if (
                nr === 0 ||
                nr === m - 1 ||
                nc === 0 ||
                nc === n - 1
            ) {
                return steps + 1;
            }

            // Mark as visited and add to queue
            maze[nr][nc] = '+';
            queue.push([nr, nc, steps + 1]);
        }
    }

    return -1;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](../../1501-2000/1888-find-nearest-point-that-has-the-same-x-or-y-coordinate/)
- [4024. Nearest Available Drone](../../4001-4500/4378-nearest-available-drone/)
- [1036. Escape a Large Maze](../../1001-1500/1106-escape-a-large-maze/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)
