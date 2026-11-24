# LeetCode 2577: Minimum Time to Visit a Cell In a Grid

**LeetCode Problem #2577 — Minimum Time to Visit a Cell In a Grid**
Solve LeetCode Minimum Time to Visit a Cell In a Grid using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Visit a Cell In a Grid |
| LeetCode | #2577 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a `m x n` matrix `grid` consisting of non-negative integers where `grid[row][col]` represents the **minimum** time required to be able to visit the cell `(row, col)`, which means you can visit the cell `(row, col)` only when the time you visit it is greater than or equal to `grid[row][col]`.

You are standing in the **top-left** cell of the matrix in the `0^th` second, and you must move to **any** adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return *the **minimum** time required in which you can visit the bottom-right cell of the matrix*. If you cannot visit the bottom-right cell, then return `-1`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10^5`
- `0 <= grid[i][j] <= 10^5`
- `grid[0][0] == 0`

## Examples
### Example 1
- **Input:** `grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]`
- **Output:** `7`
- **Explanation:** One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.

### Example 2
- **Input:** `grid = [[0,2,4],[3,2,1],[1,0,4]]`
- **Output:** `-1`
- **Explanation:** There is no path from the top left to the bottom-right cell.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Visit a Cell In a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.

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
var minimumTime = function (grid) {
    const m = grid.length, n = grid[0].length;
    if (grid[0][1] > 1 && grid[1][0] > 1) return -1;

    // Minimal binary heap storing [time, index]
    const heap = [];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            const len = heap.length;
            while (true) {
                let l = 2 * i + 1, r = l + 1, s = i;
                if (l < len && heap[l][0] < heap[s][0]) s = l;
                if (r < len && heap[r][0] < heap[s][0]) s = r;
                if (s === i) break;
                [heap[s], heap[i]] = [heap[i], heap[s]];
                i = s;
            }
        }
        return top;
    };

    const dist = new Array(m * n).fill(Infinity);
    dist[0] = 0;
    push([0, 0]);
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    while (heap.length) {
        const [t, idx] = pop();
        if (t > dist[idx]) continue;
        const r = (idx / n) | 0, c = idx % n;
        if (r === m - 1 && c === n - 1) return t;

        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nc < 0 || nr >= m || nc >= n) continue;
            let nt = t + 1;
            const need = grid[nr][nc];
            if (nt < need) {
                nt = need + ((need - nt) % 2);
            }
            const ni = nr * n + nc;
            if (nt < dist[ni]) {
                dist[ni] = nt;
                push([nt, ni]);
            }
        }
    }
    return -1;
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
- [3112. Minimum Time to Visit Disappearing Nodes](../../3001-3500/3112-minimum-time-to-visit-disappearing-nodes/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [1536. Minimum Swaps to Arrange a Binary Grid](../../1501-2000/1536-minimum-swaps-to-arrange-a-binary-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/)
