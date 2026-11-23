# LeetCode 1139: Largest 1-Bordered Square

**LeetCode Problem #1139 — Largest 1-Bordered Square**
Solve LeetCode Largest 1-Bordered Square using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest 1-Bordered Square |
| LeetCode | #1139 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a 2D `grid` of `0`s and `1`s, return the number of elements in the largest **square** subgrid that has all `1`s on its **border**, or `0` if such a subgrid doesn't exist in the `grid`.

## Constraints
- `1 <= grid.length <= 100`
- `1 <= grid[0].length <= 100`
- `grid[i][j]` is `0` or `1`

## Examples
### Example 1
- **Input:** `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- **Output:** `9`

### Example 2
- **Input:** `grid = [[1,1,0,0]]`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Largest 1-Bordered Square**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,1,1],[1,0,1],[1,1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.

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
var largest1BorderedSquare = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    // Consecutive 1s ending at (r, c) horizontally (left) and vertically (up)
    const left = Array.from({ length: rows }, () => new Int32Array(cols));
    const up = Array.from({ length: rows }, () => new Int32Array(cols));

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === 1) {
                left[r][c] = (c > 0 ? left[r][c - 1] : 0) + 1;
                up[r][c] = (r > 0 ? up[r - 1][c] : 0) + 1;
            }
        }
    }

    let maxLen = 0;
    for (let r = rows - 1; r >= 0; r--) {
        for (let c = cols - 1; c >= 0; c--) {
            // Bottom and right edges already have at least `side` 1s
            let side = Math.min(left[r][c], up[r][c]);
            while (side > maxLen) {
                // Verify top edge and left edge also have at least `side` 1s
                if (left[r - side + 1][c] >= side && up[r][c - side + 1] >= side) {
                    maxLen = side;
                    break;
                }
                side--;
            }
        }
    }

    return maxLen * maxLen;
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
- [1725. Number Of Rectangles That Can Form The Largest Square](../../1501-2000/1843-number-of-rectangles-that-can-form-the-largest-square/)
- [3047. Find the Largest Area of Square Inside Two Rectangles](../../3001-3500/3325-find-the-largest-area-of-square-inside-two-rectangles/)
- [191. Number of 1 Bits](../../0001-0500/0191-number-of-1-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-1-bordered-square/)
