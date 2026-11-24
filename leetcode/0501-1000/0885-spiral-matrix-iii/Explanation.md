# LeetCode 885: Spiral Matrix III

**LeetCode Problem #885 — Spiral Matrix III**
Solve LeetCode Spiral Matrix III using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Spiral Matrix III |
| LeetCode | #885 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You start at the cell `(rStart, cStart)` of an `rows x cols` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all `rows * cols` spaces of the grid.

Return *an array of coordinates representing the positions of the grid in the order you visited them*.

## Constraints
- `1 <= rows, cols <= 100`
- `0 <= rStart < rows`
- `0 <= cStart < cols`

## Examples
### Example 1
- **Input:** `rows = 1, cols = 4, rStart = 0, cStart = 0`
- **Output:** `[[0,0],[0,1],[0,2],[0,3]]`

### Example 2
- **Input:** `rows = 5, cols = 6, rStart = 1, cStart = 4`
- **Output:** `[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Spiral Matrix III**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rows = 1, cols = 4, rStart = 0, cStart = 0`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,0],[0,1],[0,2],[0,3]]`.

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
var spiralMatrixIII = function(rows, cols, rStart, cStart) {
    const totalCells = rows * cols;
    const res = [[rStart, cStart]];
    if (totalCells === 1) return res;

    // Clockwise directions: East, South, West, North
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let r = rStart;
    let c = cStart;
    let stepLen = 1;
    let d = 0; // Start facing East

    while (res.length < totalCells) {
        // Every two direction changes share the same step length
        for (let turn = 0; turn < 2; turn++) {
            const [dr, dc] = dirs[d];
            for (let s = 0; s < stepLen; s++) {
                r += dr;
                c += dc;
                if (r >= 0 && r < rows && c >= 0 && c < cols) {
                    res.push([r, c]);
                    if (res.length === totalCells) return res;
                }
            }
            d = (d + 1) % 4;
        }
        stepLen++;
    }

    return res;
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
- [54. Spiral Matrix](../../0001-0500/0054-spiral-matrix/)
- [59. Spiral Matrix II](../../0001-0500/0059-spiral-matrix-ii/)
- [2326. Spiral Matrix IV](../../2001-2500/2326-spiral-matrix-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/spiral-matrix-iii/)
