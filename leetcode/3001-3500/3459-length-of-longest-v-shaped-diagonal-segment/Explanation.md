# LeetCode 3459: Length of Longest V-Shaped Diagonal Segment

**LeetCode Problem #3459 — Length of Longest V-Shaped Diagonal Segment**
Solve LeetCode Length of Longest V-Shaped Diagonal Segment using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Length of Longest V-Shaped Diagonal Segment |
| LeetCode | #3459 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer matrix `grid` of size `n x m`, where each element is either `0`, `1`, or `2`.

A **V-shaped diagonal segment** is defined as:

The segment starts with `1`. 
 The subsequent elements follow this infinite sequence: `2, 0, 2, 0, ...`. 
 The segment:
 
 Starts **along** a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right). 
 Continues the** sequence** in the same diagonal direction. 
 Makes** at most one clockwise 90-degree**** turn** to another diagonal direction while **maintaining** the sequence.

Return the **length** of the **longest** **V-shaped diagonal segment**. If no valid segment *exists*, return 0.

## Constraints
- `n == grid.length`
- `m == grid[i].length`
- `1 <= n, m <= 500`
- `grid[i][j]` is either `0`, `1` or `2`.

## Examples
### Example 1
- **Input:** `grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]`
- **Output:** `5`
- **Explanation:** The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: `(0,2) &rarr; (1,3) &rarr; (2,4)`, takes a

### Example 2
- **Input:** `grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]`
- **Output:** `4`

### Example 3
- **Input:** `grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]`
- **Output:** `5`

### Example 4
- **Input:** `grid = [[1]]`
- **Output:** `1`
- **Explanation:** The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: `(0,0)`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Length of Longest V-Shaped Diagonal Segment**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: `(0,2) &rarr; (1,3) &rarr; (2,4)`, takes a

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
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        def order(dx, dy):
            # visit cells so that (i+dx, j+dy) is processed before (i, j)
            rows = range(n - 1, -1, -1) if dx == 1 else range(n)
            cols = range(m - 1, -1, -1) if dy == 1 else range(m)
            return rows, cols

        straight = [[0] * (n * m) for _ in range(4)]
        turn = [[0] * (n * m) for _ in range(4)]

        for d in range(4):
            dx, dy = dirs[d]
            rows, cols = order(dx, dy)
            S = straight[d]
            for i in rows:
                for j in cols:
                    need = 2 if grid[i][j] != 2 else 0
                    best = 1
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == need:
                        best = 1 + S[x * m + y]
                    S[i * m + j] = best

        for d in range(4):
            dx, dy = dirs[d]
            nd = (d + 1) % 4
            ndx, ndy = dirs[nd]
            rows, cols = order(dx, dy)
            T = turn[d]
            SN = straight[nd]
            for i in rows:
                for j in cols:
                    need = 2 if grid[i][j] != 2 else 0
                    best = 1
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == need:
                        best = 1 + T[x * m + y]
                    x, y = i + ndx, j + ndy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == need:
                        best = max(best, 1 + SN[x * m + y])
                    T[i * m + j] = best

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, turn[d][i * m + j])
        return ans
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
- [2781. Length of the Longest Valid Substring](../../2501-3000/2781-length-of-the-longest-valid-substring/)
- [2958. Length of Longest Subarray With at Most K Frequency](../../2501-3000/2958-length-of-longest-subarray-with-at-most-k-frequency/)
- [3043. Find the Length of the Longest Common Prefix](../../3001-3500/3043-find-the-length-of-the-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/)
