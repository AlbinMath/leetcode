# LeetCode 2812: Find the Safest Path in a Grid

**LeetCode Problem #2812 — Find the Safest Path in a Grid**
Solve LeetCode Find the Safest Path in a Grid using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Safest Path in a Grid |
| LeetCode | #2812 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D matrix `grid` of size `n x n`, where `(r, c)` represents:

A cell containing a thief if `grid[r][c] = 1` 
 An empty cell if `grid[r][c] = 0`

You are initially positioned at cell `(0, 0)`. In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The **safeness factor** of a path on the grid is defined as the **minimum** manhattan distance from any cell in the path to any thief in the grid.

Return *the **maximum safeness factor** of all paths leading to cell *`(n - 1, n - 1)`*.*

An **adjacent** cell of cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)` and `(r - 1, c)` if it exists.

The **Manhattan distance** between two cells `(a, b)` and `(x, y)` is equal to `|a - x| + |b - y|`, where `|val|` denotes the absolute value of val.

## Constraints
- `1 <= grid.length == n <= 400`
- `grid[i].length == n`
- `grid[i][j]` is either `0` or `1`.
- There is at least one thief in the `grid`.

## Examples
### Example 1
- **Input:** `grid = [[1,0,0],[0,0,0],[0,0,1]]`
- **Output:** `0`
- **Explanation:** All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

### Example 2
- **Input:** `grid = [[0,0,1],[0,0,0],[0,0,0]]`
- **Output:** `2`
- **Explanation:** The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

### Example 3
- **Input:** `grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]`
- **Output:** `2`
- **Explanation:** The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Safest Path in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,0,0],[0,0,0],[0,0,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

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
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.*;

class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();

        // dist[r][c] = distance to the nearest thief
        int[][] dist = new int[n][n];
        for (int[] row : dist) {
            Arrays.fill(row, -1);
        }

        Queue<int[]> queue = new LinkedList<>();

        // Start BFS from all thieves simultaneously
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid.get(r).get(c) == 1) {
                    dist[r][c] = 0;
                    queue.offer(new int[]{r, c});
                }
            }
        }

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        // Multi-source BFS
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n
                        && dist[nr][nc] == -1) {

                    dist[nr][nc] = dist[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }

        // Maximize the minimum safeness along the path
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[2], a[2])
        );

        boolean[][] visited = new boolean[n][n];

        // {row, col, current safeness}
        pq.offer(new int[]{0, 0, dist[0][0]});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();

            int r = cur[0];
            int c = cur[1];
            int safe = cur[2];

            if (visited[r][c]) {
                continue;
            }

            visited[r][c] = true;

            if (r == n - 1 && c == n - 1) {
                return safe;
            }

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n
                        && !visited[nr][nc]) {

                    int newSafe = Math.min(safe, dist[nr][nc]);

                    pq.offer(new int[]{nr, nc, newSafe});
                }
            }
        }

        return -1;
    }
}
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
- [1293. Shortest Path in a Grid with Obstacles Elimination](../../1001-1500/1414-shortest-path-in-a-grid-with-obstacles-elimination/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [1391. Check if There is a Valid Path in a Grid](../../1501-2000/1507-check-if-there-is-a-valid-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/)
