# LeetCode 1591: Strange Printer II

**LeetCode Problem #1591 — Strange Printer II**
Solve LeetCode Strange Printer II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Strange Printer II |
| LeetCode | #1591 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a strange printer with the following two special requirements:

On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle. 
 Once the printer has used a color for the above operation, **the same color cannot be used again**.

You are given a `m x n` matrix `targetGrid`, where `targetGrid[row][col]` is the color in the position `(row, col)` of the grid.

Return `true`* if it is possible to print the matrix *`targetGrid`*,** otherwise, return *`false`.

## Constraints
- `m == targetGrid.length`
- `n == targetGrid[i].length`
- `1 <= m, n <= 60`
- `1 <= targetGrid[row][col] <= 60`

## Examples
### Example 1
- **Input:** `targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]`
- **Output:** `true`

### Example 2
- **Input:** `targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]`
- **Output:** `true`

### Example 3
- **Input:** `targetGrid = [[1,2,1],[2,1,2],[1,2,1]]`
- **Output:** `false`
- **Explanation:** It is impossible to form targetGrid because it is not allowed to print the same color in different turns.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Strange Printer II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
/**
 * @param {number[][]} targetGrid
 * @return {boolean}
 */
var isPrintable = function (targetGrid) {
    const m = targetGrid.length, n = targetGrid[0].length;
    const C = 61;
    const top = new Array(C).fill(Infinity);
    const bot = new Array(C).fill(-1);
    const left = new Array(C).fill(Infinity);
    const right = new Array(C).fill(-1);
    const present = new Array(C).fill(false);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const c = targetGrid[i][j];
            present[c] = true;
            if (i < top[c]) top[c] = i;
            if (i > bot[c]) bot[c] = i;
            if (j < left[c]) left[c] = j;
            if (j > right[c]) right[c] = j;
        }
    }

    const adj = Array.from({ length: C }, () => new Set());
    const indeg = new Array(C).fill(0);

    for (let c = 1; c < C; c++) {
        if (!present[c]) continue;
        for (let i = top[c]; i <= bot[c]; i++) {
            for (let j = left[c]; j <= right[c]; j++) {
                const d = targetGrid[i][j];
                if (d !== c && !adj[c].has(d)) {
                    adj[c].add(d);
                    indeg[d]++;
                }
            }
        }
    }

    const q = [];
    let total = 0;
    for (let c = 1; c < C; c++) {
        if (!present[c]) continue;
        total++;
        if (indeg[c] === 0) q.push(c);
    }

    let head = 0;
    while (head < q.length) {
        const u = q[head++];
        for (const v of adj[u]) if (--indeg[v] === 0) q.push(v);
    }
    return q.length === total;
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
- [664. Strange Printer](../../0501-1000/0664-strange-printer/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/strange-printer-ii/)
