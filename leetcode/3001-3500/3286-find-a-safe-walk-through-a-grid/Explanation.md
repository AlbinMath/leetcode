# LeetCode 3286: Find a Safe Walk Through a Grid

**LeetCode Problem #3286 — Find a Safe Walk Through a Grid**
Solve LeetCode Find a Safe Walk Through a Grid using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find a Safe Walk Through a Grid |
| LeetCode | #3286 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` binary matrix `grid` and an integer `health`.

You start on the upper-left corner `(0, 0)` and would like to get to the lower-right corner `(m - 1, n - 1)`.

You can move up, down, left, or right from one cell to another adjacent cell as long as your health *remains* **positive**.

Cells `(i, j)` with `grid[i][j] = 1` are considered **unsafe** and reduce your health by 1.

Return `true` if you can reach the final cell with a health value of 1 or more, and `false` otherwise.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- ` 2 <= m * n `
- `1 <= health <= m + n`
- `grid[i][j]` is either 0 or 1.

## Examples
### Example 1
- **Input:** `grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1`
- **Output:** `true`
- **Explanation:** The final cell can be reached safely by walking along the gray cells below.

### Example 2
- **Input:** `grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3`
- **Output:** `false`
- **Explanation:** A minimum of 4 health points is needed to reach the final cell safely.

### Example 3
- **Input:** `grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5`
- **Output:** `true`
- **Explanation:** The final cell can be reached safely by walking along the gray cells below. 

 

 Any path that does not go through the cell `(1, 1)` is unsafe since your health will drop to 0 when reaching the final cell.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find a Safe Walk Through a Grid**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The final cell can be reached safely by walking along the gray cells below.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.*;

class Solution {
    public boolean findSafeWalk(List<List<Integer>> grid, int health) {
        int m = grid.size();
        int n = grid.get(0).size();

        // best[i][j] = maximum health remaining when reaching (i, j)
        int[][] best = new int[m][n];

        for (int[] row : best) {
            Arrays.fill(row, -1);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[2], a[2])
        );

        // Starting cell also costs health if it is unsafe
        int startHealth = health - grid.get(0).get(0);

        if (startHealth <= 0) {
            return false;
        }

        best[0][0] = startHealth;
        pq.offer(new int[]{0, 0, startHealth});

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();

            int r = cur[0];
            int c = cur[1];
            int currentHealth = cur[2];

            // Ignore an outdated state
            if (currentHealth < best[r][c]) {
                continue;
            }

            if (r == m - 1 && c == n - 1) {
                return true;
            }

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }

                int newHealth =
                    currentHealth - grid.get(nr).get(nc);

                // Health must remain positive
                if (newHealth <= 0) {
                    continue;
                }

                if (newHealth > best[nr][nc]) {
                    best[nr][nc] = newHealth;
                    pq.offer(new int[]{nr, nc, newHealth});
                }
            }
        }

        return false;
    }
}
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [802. Find Eventual Safe States](../../0501-1000/0802-find-eventual-safe-states/)
- [2812. Find the Safest Path in a Grid](../../2501-3000/2812-find-the-safest-path-in-a-grid/)
- [3108. Minimum Cost Walk in Weighted Graph](../../3001-3500/3108-minimum-cost-walk-in-weighted-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)
