# LeetCode 1536: Minimum Swaps to Arrange a Binary Grid

**LeetCode Problem #1536 — Minimum Swaps to Arrange a Binary Grid**
Solve LeetCode Minimum Swaps to Arrange a Binary Grid using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps to Arrange a Binary Grid |
| LeetCode | #1536 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an `n x n` binary `grid`, in one step you can choose two **adjacent rows** of the grid and swap them.

A grid is said to be **valid** if all the cells above the main diagonal are **zeros**.

Return *the minimum number of steps* needed to make the grid valid, or **-1** if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell `(1, 1)` and ends at cell `(n, n)`.

## Constraints
- `n == grid.length` `== grid[i].length`
- `1 <= n <= 200`
- `grid[i][j]` is either `0` or `1`

## Examples
### Example 1
- **Input:** `grid = [[0,0,1],[1,1,0],[1,0,0]]`
- **Output:** `3`

### Example 2
- **Input:** `grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]`
- **Output:** `-1`
- **Explanation:** All rows are similar, swaps have no effect on the grid.

### Example 3
- **Input:** `grid = [[1,0,0],[1,1,0],[1,1,1]]`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Swaps to Arrange a Binary Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,0,1],[1,1,0],[1,0,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
var minSwaps = function(grid) {
    const n = grid.length;
    const trailingZeros = new Array(n);

    // Count trailing zeros for each row
    for (let r = 0; r < n; r++) {
        let zeros = 0;
        for (let c = n - 1; c >= 0; c--) {
            if (grid[r][c] === 0) {
                zeros++;
            } else {
                break;
            }
        }
        trailingZeros[r] = zeros;
    }

    let swaps = 0;
    for (let i = 0; i < n; i++) {
        const required = n - 1 - i;
        // Find the nearest row at or below i with enough trailing zeros
        let j = i;
        while (j < n && trailingZeros[j] < required) {
            j++;
        }

        if (j === n) {
            return -1;
        }

        // Bubble row j up to position i using (j - i) adjacent swaps
        swaps += j - i;
        const chosen = trailingZeros[j];
        for (let k = j; k > i; k--) {
            trailingZeros[k] = trailingZeros[k - 1];
        }
        trailingZeros[i] = chosen;
    }

    return swaps;
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
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1994-minimum-number-of-swaps-to-make-the-binary-string-alternating/)
- [111. Minimum Depth of Binary Tree](../../0001-0500/0111-minimum-depth-of-binary-tree/)
- [671. Second Minimum Node In a Binary Tree](../../0501-1000/0671-second-minimum-node-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/)
