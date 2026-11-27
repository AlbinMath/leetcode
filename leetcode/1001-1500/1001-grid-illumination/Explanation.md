# LeetCode 1001: Grid Illumination

**LeetCode Problem #1001 — Grid Illumination**
Solve LeetCode Grid Illumination using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Grid Illumination |
| LeetCode | #1001 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a 2D `grid` of size `n x n` where each cell of this grid has a lamp that is initially **turned off**.

You are given a 2D array of lamp positions `lamps`, where `lamps[i] = [row_i, col_i]` indicates that the lamp at `grid[row_i][col_i]` is **turned on**. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it **illuminates its cell** and **all other cells** in the same **row, column, or diagonal**.

You are also given another 2D array `queries`, where `queries[j] = [row_j, col_j]`. For the `j^th` query, determine whether `grid[row_j][col_j]` is illuminated or not. After answering the `j^th` query, **turn off** the lamp at `grid[row_j][col_j]` and its **8 adjacent lamps** if they exist. A lamp is adjacent if its cell shares either a side or corner with `grid[row_j][col_j]`.

Return *an array of integers *`ans`*,** where *`ans[j]`* should be *`1`* if the cell in the *`j^th`* query was illuminated, or *`0`* if the lamp was not.*

## Constraints
- `1 <= n <= 10^9`
- `0 <= lamps.length <= 20000`
- `0 <= queries.length <= 20000`
- `lamps[i].length == 2`
- `0 <= row_i, col_i < n`
- `queries[j].length == 2`
- `0 <= row_j, col_j < n`

## Examples
### Example 1
- **Input:** `n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]`
- **Output:** `[1,0]`
- **Explanation:** We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0^th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
 
The 1^st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

### Example 2
- **Input:** `n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]`
- **Output:** `[1,1]`

### Example 3
- **Input:** `n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]`
- **Output:** `[1,1,0]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Grid Illumination**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,0]`.
4. **Verification:** We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0^th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
 
The 1^st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

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
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        active_lamps = set()
        rows = defaultdict(int)
        cols = defaultdict(int)
        diag1 = defaultdict(int) 
        diag2 = defaultdict(int)
        for r, c in lamps:
            if (r, c) not in active_lamps:
                active_lamps.add((r, c))
                rows[r] += 1
                cols[c] += 1
                diag1[r - c] += 1
                diag2[r + c] += 1     
        ans = []
        for qr, qc in queries:
            if rows[qr] > 0 or cols[qc] > 0 or diag1[qr - qc] > 0 or diag2[qr + qc] > 0:
                ans.append(1)
            else:
                ans.append(0)
            for nr in (qr - 1, qr, qr + 1):
                for nc in (qc - 1, qc, qc + 1):
                    if (nr, nc) in active_lamps:
                        active_lamps.remove((nr, nc))
                        rows[nr] -= 1
                        cols[nc] -= 1
                        diag1[nr - nc] -= 1
                        diag2[nr + nc] -= 1 
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
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1260. Shift 2D Grid](../../1001-1500/1260-shift-2d-grid/)
- [1293. Shortest Path in a Grid with Obstacles Elimination](../../1001-1500/1293-shortest-path-in-a-grid-with-obstacles-elimination/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/grid-illumination/)
