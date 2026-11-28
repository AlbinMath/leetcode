# LeetCode 3552: Grid Teleportation Traversal

**LeetCode Problem #3552 — Grid Teleportation Traversal**
Solve LeetCode Grid Teleportation Traversal using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Grid Teleportation Traversal |
| LeetCode | #3552 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D character grid `matrix` of size `m x n`, represented as an array of strings, where `matrix[i][j]` represents the cell at the intersection of the `i^th` row and `j^th` column. Each cell is one of the following:

`'.'` representing an empty cell. 
 `'#'` representing an obstacle. 
 An uppercase letter (`'A'`-`'Z'`) representing a teleportation portal.

You start at the top-left cell `(0, 0)`, and your goal is to reach the bottom-right cell `(m - 1, n - 1)`. You can move from the current cell to any adjacent cell (up, down, left, right) as long as the destination cell is within the grid bounds and is not an obstacle**.**

If you step on a cell containing a portal letter and you haven't used that portal letter before, you may instantly teleport to any other cell in the grid with the same letter. This teleportation does not count as a move, but each portal letter can be used** at most **once during your journey.

Return the **minimum** number of moves required to reach the bottom-right cell. If it is not possible to reach the destination, return `-1`.

## Constraints
- `1 <= m == matrix.length <= 10^3`
- `1 <= n == matrix[i].length <= 10^3`
- `matrix[i][j]` is either `'#'`, `'.'`, or an uppercase English letter.
- `matrix[0][0]` is not an obstacle.

## Examples
### Example 1
- **Input:** `matrix = ["A..",".A.","..."]`
- **Output:** `2`
- **Explanation:** Before the first move, teleport from `(0, 0)` to `(1, 1)`. 
 In the first move, move from `(1, 1)` to `(1, 2)`. 
 In the second move, move from `(1, 2)` to `(2, 2)`.

### Example 2
- **Input:** `matrix = [".#...",".#.#.",".#.#.","...#."]`
- **Output:** `13`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Grid Teleportation Traversal**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = ["A..",".A.","..."]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Before the first move, teleport from `(0, 0)` to `(1, 1)`. 
 In the first move, move from `(1, 1)` to `(1, 2)`. 
 In the second move, move from `(1, 2)` to `(2, 2)`.

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
from collections import deque, defaultdict
from typing import List

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        portals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                ch = matrix[i][j]
                if ch.isupper():
                    portals[ch].append((i, j))

        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        used = set()
        dq = deque([(0, 0, 0)])  # (r, c, d)

        while dq:
            r, c, d = dq.popleft()
            if d > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return d

            ch = matrix[r][c]
            if ch.isupper() and ch not in used:
                used.add(ch)
                for pr, pc in portals[ch]:
                    if dist[pr][pc] > d:
                        dist[pr][pc] = d
                        dq.appendleft((pr, pc, d))

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#' and dist[nr][nc] > d + 1:
                    dist[nr][nc] = d + 1
                    dq.append((nr, nc, d + 1))
        return -1
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
- [3417. Zigzag Grid Traversal With Skip](../../3001-3500/3417-zigzag-grid-traversal-with-skip/)
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1001. Grid Illumination](../../1001-1500/1001-grid-illumination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/grid-teleportation-traversal/)
