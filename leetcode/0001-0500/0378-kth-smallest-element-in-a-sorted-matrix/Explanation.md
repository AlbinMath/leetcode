# LeetCode 378: Kth Smallest Element in a Sorted Matrix

**LeetCode Problem #378 — Kth Smallest Element in a Sorted Matrix**
Solve LeetCode Kth Smallest Element in a Sorted Matrix using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Smallest Element in a Sorted Matrix |
| LeetCode | #378 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return *the* `k^th` *smallest element in the matrix*.

Note that it is the `k^th` smallest element **in the sorted order**, not the `k^th` **distinct** element.

You must find a solution with a memory complexity better than `O(n^2)`.

## Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the rows and columns of `matrix` are **guaranteed** to be sorted in **non-decreasing order**.
- `1 <= k <= n^2`
- Could you solve the problem with a constant memory (i.e., `O(1)` memory complexity)?
- Could you solve the problem in `O(n)` time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

## Examples
### Example 1
- **Input:** `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8`
- **Output:** `13`
- **Explanation:** The elements in the matrix are [1,5,9,10,11,12,13,

### Example 2
- **Input:** `matrix = [[-5]], k = 1`
- **Output:** `-5`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Kth Smallest Element in a Sorted Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The elements in the matrix are [1,5,9,10,11,12,13,

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
var kthSmallest = function(matrix, k) {
    const n = matrix.length;

    const countLessEqual = (target) => {
        let count = 0;
        let r = n - 1;
        let c = 0; // Start at bottom-left corner

        while (r >= 0 && c < n) {
            if (matrix[r][c] <= target) {
                // All elements in column c from row 0 to r are <= target
                count += r + 1;
                c++;
            } else {
                r--;
            }
        }
        return count;
    };

    let lo = matrix[0][0];
    let hi = matrix[n - 1][n - 1];

    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (countLessEqual(mid) < k) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    return lo;
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
- [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](../../1501-2000/1550-find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)
- [230. Kth Smallest Element in a BST](../../0001-0500/0230-kth-smallest-element-in-a-bst/)
- [668. Kth Smallest Number in Multiplication Table](../../0501-1000/0668-kth-smallest-number-in-multiplication-table/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
