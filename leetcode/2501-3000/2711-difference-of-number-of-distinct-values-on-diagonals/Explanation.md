# LeetCode 2711: Difference of Number of Distinct Values on Diagonals

**LeetCode Problem #2711 — Difference of Number of Distinct Values on Diagonals**
Solve LeetCode Difference of Number of Distinct Values on Diagonals using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Difference of Number of Distinct Values on Diagonals |
| LeetCode | #2711 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a 2D `grid` of size `m x n`, you should find the matrix `answer` of size `m x n`.

The cell `answer[r][c]` is calculated by looking at the diagonal values of the cell `grid[r][c]`:

Let `leftAbove[r][c]` be the number of **distinct** values on the diagonal to the left and above the cell `grid[r][c]` not including the cell `grid[r][c]` itself. 
 Let `rightBelow[r][c]` be the number of **distinct** values on the diagonal to the right and below the cell `grid[r][c]`, not including the cell `grid[r][c]` itself. 
 Then `answer[r][c] = |leftAbove[r][c] - rightBelow[r][c]|`.

A **matrix diagonal** is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until the end of the matrix is reached.

For example, in the below diagram the diagonal is highlighted using the cell with indices `(2, 3)` colored gray:

Red-colored cells are left and above the cell. 
 Blue-colored cells are right and below the cell.

Return the matrix `answer`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n, grid[i][j] <= 50`

## Examples
### Example 1
- **Input:** `grid = [[1,2,3],[3,1,5],[3,2,1]]`
- **Output:** `Output: [[1,1,0],[1,0,1],[0,1,1]]`
- **Explanation:** To calculate the `answer` cells: 

 
 
 
 answer 
 left-above elements 
 leftAbove 
 right-below elements 
 rightBelow 
 |leftAbove - rightBelow| 
 
 
 
 
 [0][0] 
 [] 
 0 
 [grid[1][1], grid[2][2]] 
 |{1, 1}| = 1 
 1 
 
 
 [0][1] 
 [] 
 0 
 [grid[1][2]] 
 |{5}| = 1 
 1 
 
 
 [0][2] 
 [] 
 0 
 [] 
 0 
 0 
 
 
 [1][0] 
 [] 
 0 
 [grid[2][1]] 
 |{2}| = 1 
 1 
 
 
 [1][1] 
 [grid[0][0]] 
 |{1}| = 1 
 [grid[2][2]] 
 |{1}| = 1 
 0 
 
 
 [1][2] 
 [grid[0][1]] 
 |{2}| = 1 
 [] 
 0 
 1 
 
 
 [2][0] 
 [] 
 0 
 [] 
 0 
 0 
 
 
 [2][1] 
 [grid[1][0]] 
 |{3}| = 1 
 [] 
 0 
 1 
 
 
 [2][2] 
 [grid[0][0], grid[1][1]] 
 |{1, 1}| = 1 
 [] 
 0 
 1

### Example 2
- **Input:** `grid = [[1]]`
- **Output:** `Output: [[0]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Difference of Number of Distinct Values on Diagonals**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,3],[3,1,5],[3,2,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `Output: [[1,1,0],[1,0,1],[0,1,1]]`.
4. **Verification:** To calculate the `answer` cells: 

 
 
 
 answer 
 left-above elements 
 leftAbove 
 right-below elements 
 rightBelow 
 |leftAbove - rightBelow| 
 
 
 
 
 [0][0] 
 [] 
 0 
 [grid[1][1], grid[2][2]] 
 |{1, 1}| = 1 
 1 
 
 
 [0][1] 
 [] 
 0 
 [grid[1][2]] 
 |{5}| = 1 
 1 
 
 
 [0][2] 
 [] 
 0 
 [] 
 0 
 0 
 
 
 [1][0] 
 [] 
 0 
 [grid[2][1]] 
 |{2}| = 1 
 1 
 
 
 [1][1] 
 [grid[0][0]] 
 |{1}| = 1 
 [grid[2][2]] 
 |{1}| = 1 
 0 
 
 
 [1][2] 
 [grid[0][1]] 
 |{2}| = 1 
 [] 
 0 
 1 
 
 
 [2][0] 
 [] 
 0 
 [] 
 0 
 0 
 
 
 [2][1] 
 [grid[1][0]] 
 |{3}| = 1 
 [] 
 0 
 1 
 
 
 [2][2] 
 [grid[0][0], grid[1][1]] 
 |{1, 1}| = 1 
 [] 
 0 
 1

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]

        # diagonals start in the top row or the left column
        starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(1, m)]

        for r0, c0 in starts:
            # collect the cells of this diagonal
            cells = []
            r, c = r0, c0
            while r < m and c < n:
                cells.append((r, c))
                r += 1
                c += 1

            seen = set()
            for r, c in cells:               # top-left -> bottom-right
                left[r][c] = len(seen)       # excludes the cell itself
                seen.add(grid[r][c])

            seen = set()
            for r, c in reversed(cells):     # bottom-right -> top-left
                right[r][c] = len(seen)
                seen.add(grid[r][c])

        return [[abs(left[i][j] - right[i][j]) for j in range(n)] for i in range(m)]
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
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../../1001-1500/1467-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [2318. Number of Distinct Roll Sequences](../../2001-2500/2318-number-of-distinct-roll-sequences/)
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/)
