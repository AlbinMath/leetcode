# LeetCode 1253: Reconstruct a 2-Row Binary Matrix

**LeetCode Problem #1253 — Reconstruct a 2-Row Binary Matrix**
Solve LeetCode Reconstruct a 2-Row Binary Matrix using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reconstruct a 2-Row Binary Matrix |
| LeetCode | #1253 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the following details of a matrix with `n` columns and `2` rows :

The matrix is a binary matrix, which means each element in the matrix can be `0` or `1`. 
 The sum of elements of the 0-th(upper) row is given as `upper`. 
 The sum of elements of the 1-st(lower) row is given as `lower`. 
 The sum of elements in the i-th column(0-indexed) is `colsum[i]`, where `colsum` is given as an integer array with length `n`.

Your task is to reconstruct the matrix with `upper`, `lower` and `colsum`.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

## Constraints
- `1 <= colsum.length <= 10^5`
- `0 <= upper, lower <= colsum.length`
- `0 <= colsum[i] <= 2`

## Examples
### Example 1
- **Input:** `upper = 2, lower = 1, colsum = [1,1,1]`
- **Output:** `[[1,1,0],[0,0,1]]`
- **Explanation:** [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

### Example 2
- **Input:** `upper = 2, lower = 3, colsum = [2,2,1,1]`
- **Output:** `[]`

### Example 3
- **Input:** `upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]`
- **Output:** `[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reconstruct a 2-Row Binary Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `upper = 2, lower = 1, colsum = [1,1,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,1,0],[0,0,1]]`.
4. **Verification:** [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

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
var reconstructMatrix = function(upper, lower, colsum) {
    const n = colsum.length;
    let totalSum = 0;
    for (let i = 0; i < n; i++) {
        totalSum += colsum[i];
    }
    if (upper + lower !== totalSum) {
        return [];
    }

    const row0 = new Array(n).fill(0);
    const row1 = new Array(n).fill(0);

    // Pass 1: Place mandatory 1s for columns with colsum[i] === 2
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 2) {
            if (upper === 0 || lower === 0) {
                return [];
            }
            row0[i] = 1;
            row1[i] = 1;
            upper--;
            lower--;
        }
    }

    // Pass 2: Distribute remaining upper and lower budgets across colsum[i] === 1
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 1) {
            if (upper > 0) {
                row0[i] = 1;
                upper--;
            } else {
                row1[i] = 1;
                lower--;
            }
        }
    }

    return [row0, row1];
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
- [1091. Shortest Path in Binary Matrix](../../1001-1500/1171-shortest-path-in-binary-matrix/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1409-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1582. Special Positions in a Binary Matrix](../../1501-2000/1704-special-positions-in-a-binary-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/)
