# LeetCode 1329: Sort the Matrix Diagonally

**LeetCode Problem #1329 — Sort the Matrix Diagonally**
Solve LeetCode Sort the Matrix Diagonally using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort the Matrix Diagonally |
| LeetCode | #1329 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **matrix diagonal** is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the **matrix diagonal** starting from `mat[2][0]`, where `mat` is a `6 x 3` matrix, includes cells `mat[2][0]`, `mat[3][1]`, and `mat[4][2]`.

Given an `m x n` matrix `mat` of integers, sort each **matrix diagonal** in ascending order and return *the resulting matrix*.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `1 <= mat[i][j] <= 100`

## Examples
### Example 1
- **Input:** `mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]`
- **Output:** `[[1,1,1,1],[1,2,2,2],[1,2,3,3]]`

### Example 2
- **Input:** `mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]`
- **Output:** `[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sort the Matrix Diagonally**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,1,1,1],[1,2,2,2],[1,2,3,3]]`.

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
var diagonalSort = function(mat) {
    const m = mat.length;
    const n = mat[0].length;

    const sortDiagonal = (startR, startC) => {
        const diag = [];
        let r = startR;
        let c = startC;
        while (r < m && c < n) {
            diag.push(mat[r][c]);
            r++;
            c++;
        }
        diag.sort((a, b) => a - b);
        r = startR;
        c = startC;
        for (const val of diag) {
            mat[r][c] = val;
            r++;
            c++;
        }
    };
    for (let c = 0; c < n; c++) {
        sortDiagonal(0, c);
    }
    for (let r = 1; r < m; r++) {
        sortDiagonal(r, 0);
    }

    return mat;
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
- [3446. Sort Matrix by Diagonals](../../3001-3500/3446-sort-matrix-by-diagonals/)
- [75. Sort Colors](../../0001-0500/0075-sort-colors/)
- [147. Insertion Sort List](../../0001-0500/0147-insertion-sort-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-the-matrix-diagonally/)
