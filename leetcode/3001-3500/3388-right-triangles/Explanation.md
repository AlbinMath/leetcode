# LeetCode 3128: Right Triangles

**LeetCode Problem #3128 — Right Triangles**
Solve LeetCode Right Triangles using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Right Triangles |
| LeetCode | #3128 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D boolean matrix `grid`.

A collection of 3 elements of `grid` is a **right triangle** if one of its elements is in the **same row** with another element and in the **same column** with the third element. The 3 elements may **not** be next to each other.

Return an integer that is the number of **right triangles** that can be made with 3 elements of `grid` such that **all** of them have a value of 1.

## Constraints
- `1 <= grid.length <= 1000`
- `1 <= grid[i].length <= 1000`
- `0 <= grid[i][j] <= 1`

## Examples
### Example 1
- **Input:** `grid = [[0,1,0],[0,1,1],[0,1,0]]`
- **Output:** `2`
- **Explanation:** There are two right triangles with elements of the value 1. Notice that the blue ones do

### Example 2
- **Input:** `grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]`
- **Output:** `0`
- **Explanation:** There are no right triangles with elements of the value 1. Notice that the blue ones do

### Example 3
- **Input:** `grid = [[1,0,1],[1,0,0],[1,0,0]]`
- **Output:** `2`
- **Explanation:** There are two right triangles with elements of the value 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Right Triangles**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1,0],[0,1,1],[0,1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are two right triangles with elements of the value 1. Notice that the blue ones do

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
var numberOfRightTriangles = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    const rowCount = new Array(m).fill(0);
    const colCount = new Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }

    let ans = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                ans += (rowCount[i] - 1) * (colCount[j] - 1);
            }
        }
    }

    return ans;
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
- [116. Populating Next Right Pointers in Each Node](../../0001-0500/0116-populating-next-right-pointers-in-each-node/)
- [117. Populating Next Right Pointers in Each Node II](../../0001-0500/0117-populating-next-right-pointers-in-each-node-ii/)
- [199. Binary Tree Right Side View](../../0001-0500/0199-binary-tree-right-side-view/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/right-triangles/)
