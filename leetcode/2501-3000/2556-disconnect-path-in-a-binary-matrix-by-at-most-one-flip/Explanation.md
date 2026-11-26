# LeetCode 2556: Disconnect Path in a Binary Matrix by at Most One Flip

**LeetCode Problem #2556 — Disconnect Path in a Binary Matrix by at Most One Flip**
Solve LeetCode Disconnect Path in a Binary Matrix by at Most One Flip using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Disconnect Path in a Binary Matrix by at Most One Flip |
| LeetCode | #2556 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** `m x n` **binary** matrix `grid`. You can move from a cell `(row, col)` to any of the cells `(row + 1, col)` or `(row, col + 1)` that has the value `1`. The matrix is **disconnected** if there is no path from `(0, 0)` to `(m - 1, n - 1)`.

You can flip the value of **at most one** (possibly none) cell. You **cannot flip** the cells `(0, 0)` and `(m - 1, n - 1)`.

Return `true` *if it is possible to make the matrix disconnect or *`false`* otherwise*.

**Note** that flipping a cell changes its value from `0` to `1` or from `1` to `0`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 1000`
- `1 <= m * n <= 10^5`
- `grid[i][j]` is either `0` or `1`.
- `grid[0][0] == grid[m - 1][n - 1] == 1`

## Examples
### Example 1
- **Input:** `grid = [[1,1,1],[1,0,0],[1,1,1]]`
- **Output:** `true`
- **Explanation:** We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.

### Example 2
- **Input:** `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- **Output:** `false`
- **Explanation:** It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Disconnect Path in a Binary Matrix by at Most One Flip**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,1,1],[1,0,0],[1,1,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def find_path():
            # returns list of cells on a path, or None
            parent = {}
            stack = [(0, 0)]
            seen = {(0, 0)}
            while stack:
                r, c = stack.pop()
                if r == m - 1 and c == n - 1:
                    path = []
                    cur = (r, c)
                    while cur != (0, 0):
                        path.append(cur)
                        cur = parent[cur]
                    return path
                # push right first so down is popped first (down preferred)
                for nr, nc in ((r, c + 1), (r + 1, c)):
                    if nr < m and nc < n and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        parent[(nr, nc)] = (r, c)
                        stack.append((nr, nc))
            return None

        path = find_path()
        if path is None:
            return True
        for r, c in path:
            if (r, c) != (m - 1, n - 1):
                grid[r][c] = 0
        return find_path() is None
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
- [1784. Check if Binary String Has at Most One Segment of Ones](../../1501-2000/1784-check-if-binary-string-has-at-most-one-segment-of-ones/)
- [1091. Shortest Path in Binary Matrix](../../1001-1500/1091-shortest-path-in-binary-matrix/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)
