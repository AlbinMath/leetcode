# LeetCode 498: Diagonal Traverse

**LeetCode Problem #498 — Diagonal Traverse**
Solve LeetCode Diagonal Traverse using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Diagonal Traverse |
| LeetCode | #498 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an `m x n` matrix `mat`, return *an array of all the elements of the array in a diagonal order*.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `-10^5 <= mat[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `[1,2,4,7,5,3,6,8,9]`

### Example 2
- **Input:** `mat = [[1,2],[3,4]]`
- **Output:** `[1,2,3,4]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Diagonal Traverse**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,2,3],[4,5,6],[7,8,9]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,4,7,5,3,6,8,9]`.

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
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const res = new Array(m * n);
    let r = 0;
    let c = 0;
    let upRight = true;

    for (let i = 0; i < m * n; i++) {
        res[i] = mat[r][c];

        if (upRight) {
            if (c === n - 1) {
                r++;
                upRight = false;
            } else if (r === 0) {
                c++;
                upRight = false;
            } else {
                r--;
                c++;
            }
        } else {
            if (r === m - 1) {
                c++;
                upRight = true;
            } else if (c === 0) {
                r++;
                upRight = true;
            } else {
                r++;
                c--;
            }
        }
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
- [1572. Matrix Diagonal Sum](../../1501-2000/1677-matrix-diagonal-sum/)
- [2614. Prime In Diagonal](../../2501-3000/2722-prime-in-diagonal/)
- [3459. Length of Longest V-Shaped Diagonal Segment](../../3501-4000/3733-length-of-longest-v-shaped-diagonal-segment/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/diagonal-traverse/)
