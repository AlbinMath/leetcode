# LeetCode 3933: Largest Local Values in a Matrix II

**LeetCode Problem #3933 — Largest Local Values in a Matrix II**
Solve LeetCode Largest Local Values in a Matrix II using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Local Values in a Matrix II |
| LeetCode | #3933 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `n x m` integer matrix `matrix` containing non-negative integers.

A **non-zero **cell `(row, col)` checks the cells near it as follows:

Let `x = matrix[row][col]`. 
 Consider every cell within `x` rows and `x` columns of `(row, col)`. 
 Ignore cells that are outside the matrix. 
 Ignore the cells where both the row distance and column distance are exactly `x`.

The cell `(row, col)` is a **local maximum** if it is **non-zero** and no considered cell has a value **greater than** `x`.

Return an integer denoting the number of **local maximums** in `matrix`.

​​​​​​​

## Constraints
- `1 <= n == matrix.length <= 200`
- `1 <= m == matrix[i].length <= 200`
- `0 <= matrix[i][j] <= 200`

## Examples
### Example 1
- **Input:** `matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]`
- **Output:** `1`
- **Explanation:** For the non-zero cell `(3, 3)`, `x = matrix[3][3] = 2`. 
 The highlighted cells are the considered cells within `x` rows and `x` columns of `(3, 3)`. 
 The four cells with both row and column distances equal to `x = 2` are ignored. 
 No considered cell has a value greater than 2, so `(3, 3)` is a local maximum. 
 There are no other non-zero cells, so the answer is 1.

### Example 2
- **Input:** `matrix = [[1,2],[3,4]]`
- **Output:** `1`
- **Explanation:** Only the cell with value 4 is a local maximum. Every other non-zero cell considers a cell with a greater value.

### Example 3
- **Input:** `matrix = [[1,0,1],[0,1,0],[1,0,1]]`
- **Output:** `5`
- **Explanation:** For a cell with value 1, the considered cells are the cell itself and its 4-directionally adjacent cells that are inside the matrix. 
 Each of the five cells with value 1 only considers cells with values 0 or 1, so all five of them are local maximums.

### Example 4
- **Input:** `matrix = [[1,1],[1,1]]`
- **Output:** `4`
- **Explanation:** All cells have the same value. Therefore, no cell considers another cell with a greater value, so all 4 cells are local maximums.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Local Values in a Matrix II**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** For the non-zero cell `(3, 3)`, `x = matrix[3][3] = 2`. 
 The highlighted cells are the considered cells within `x` rows and `x` columns of `(3, 3)`. 
 The four cells with both row and column distances equal to `x = 2` are ignored. 
 No considered cell has a value greater than 2, so `(3, 3)` is a local maximum. 
 There are no other non-zero cells, so the answer is 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        groups = {}
        for i in range(n):
            for j in range(m):
                x = matrix[i][j]
                if x > 0:
                    groups.setdefault(x, []).append((i, j))

        res = 0
        for x, cells in groups.items():
            # prefix sums of indicator (matrix > x)
            P = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n):
                row = matrix[i]
                Pi, Pn = P[i], P[i + 1]
                run = 0
                for j in range(m):
                    if row[j] > x:
                        run += 1
                    Pn[j + 1] = Pi[j + 1] + run

            for r, c in cells:
                r1, r2 = max(0, r - x), min(n - 1, r + x)
                c1, c2 = max(0, c - x), min(m - 1, c + x)
                s = P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]
                if s:
                    for dr in (-x, x):
                        for dc in (-x, x):
                            rr, cc = r + dr, c + dc
                            if 0 <= rr < n and 0 <= cc < m and matrix[rr][cc] > x:
                                s -= 1
                if s == 0:
                    res += 1

        return res
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2373. Largest Local Values in a Matrix](../../2001-2500/2373-largest-local-values-in-a-matrix/)
- [1090. Largest Values From Labels](../../1001-1500/1090-largest-values-from-labels/)
- [1252. Cells with Odd Values in a Matrix](../../1001-1500/1252-cells-with-odd-values-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/)
