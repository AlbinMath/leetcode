# LeetCode 2326: Spiral Matrix IV

**LeetCode Problem #2326 — Spiral Matrix IV**
Solve LeetCode Spiral Matrix IV using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Spiral Matrix IV |
| LeetCode | #2326 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `m` and `n`, which represent the dimensions of a matrix.

You are also given the `head` of a linked list of integers.

Generate an `m x n` matrix that contains the integers in the linked list presented in **spiral** order **(clockwise)**, starting from the **top-left** of the matrix. If there are remaining empty spaces, fill them with `-1`.

Return *the generated matrix*.

## Constraints
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- The number of nodes in the list is in the range `[1, m * n]`.
- `0 <= Node.val <= 1000`

## Examples
### Example 1
- **Input:** `m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]`
- **Output:** `[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]`
- **Explanation:** The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

### Example 2
- **Input:** `m = 1, n = 4, head = [0,1,2]`
- **Output:** `[[0,1,2,-1]]`
- **Explanation:** The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Spiral Matrix IV**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]`.
4. **Verification:** The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

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
var spiralMatrix = function(m, n, head) {
    // Step 1: Initialize matrix with -1
    let matrix = Array.from(
        { length: m },
        () => Array(n).fill(-1)
    );

    // Step 2: Initialize boundaries
    let top = 0;
    let bottom = m - 1;
    let left = 0;
    let right = n - 1;

    let current = head;

    // Step 3: Fill matrix in spiral order
    while (current && top <= bottom && left <= right) {

        // Move right
        for (let col = left; col <= right && current; col++) {
            matrix[top][col] = current.val;
            current = current.next;
        }
        top++;

        // Move down
        for (let row = top; row <= bottom && current; row++) {
            matrix[row][right] = current.val;
            current = current.next;
        }
        right--;

        // Move left
        for (let col = right; col >= left && current; col--) {
            matrix[bottom][col] = current.val;
            current = current.next;
        }
        bottom--;

        // Move up
        for (let row = bottom; row >= top && current; row--) {
            matrix[row][left] = current.val;
            current = current.next;
        }
        left++;
    }

    return matrix;
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
- [885. Spiral Matrix III](../../0501-1000/0921-spiral-matrix-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/spiral-matrix-iv/)
