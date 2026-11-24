# LeetCode 427: Construct Quad Tree

**LeetCode Problem #427 — Construct Quad Tree**
Solve LeetCode Construct Quad Tree using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Quad Tree |
| LeetCode | #427 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a `n * n` matrix `grid` of `0's` and `1's` only. We want to represent `grid` with a Quad-Tree.

Return *the root of the Quad-Tree representing *`grid`.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

`val`: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the `val` to True or False when `isLeaf` is False, and both are accepted in the answer. 
 `isLeaf`: True if the node is a leaf node on the tree or False if the node has four children.

class Node {
 public boolean val;
 public boolean isLeaf;
 public Node topLeft;
 public Node topRight;
 public Node bottomLeft;
 public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all `1's` or all `0's`) set `isLeaf` True and set `val` to the value of the grid and set the four children to Null and stop. 
 If the current grid has different values, set `isLeaf` to False and set `val` to any value and divide the current grid into four sub-grids as shown in the photo. 
 Recurse for each of the children with the proper sub-grid. 
 
 
 If you want to know more about the Quad-Tree, you can refer to the wiki .

**Quad-Tree format:**

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where `null` signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list `[isLeaf, val]`.

If the value of `isLeaf` or `val` is True we represent it as **1** in the list `[isLeaf, val]` and if the value of `isLeaf` or `val` is False we represent it as **0**.

## Constraints
- `n == grid.length == grid[i].length`
- `n == 2^x` where `0 <= x <= 6`

## Examples
### Example 1
- **Input:** `grid = [[0,1],[1,0]]`
- **Output:** `[[0,1],[1,0],[1,1],[1,1],[1,0]]`
- **Explanation:** The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

### Example 2
- **Input:** `grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]`
- **Output:** `[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]`
- **Explanation:** All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Construct Quad Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1],[1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,1],[1,0],[1,1],[1,1],[1,0]]`.
4. **Verification:** The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

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
var construct = function(grid) {
    const n = grid.length;

    function build(row, col, size) {
        const value = grid[row][col];
        let uniform = true;

        // Check whether this region contains only one value
        for (let r = row; r < row + size; r++) {
            for (let c = col; c < col + size; c++) {
                if (grid[r][c] !== value) {
                    uniform = false;
                    break;
                }
            }

            if (!uniform) break;
        }

        // A uniform region becomes a leaf
        if (uniform) {
            return new Node(value === 1, true);
        }

        const half = size / 2;

        // Divide into four quadrants
        const topLeft = build(row, col, half);
        const topRight = build(row, col + half, half);
        const bottomLeft = build(row + half, col, half);
        const bottomRight = build(
            row + half,
            col + half,
            half
        );

        return new Node(
            true,
            false,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
        );
    }

    return build(0, 0, n);
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
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../../0001-0500/0106-construct-binary-tree-from-inorder-and-postorder-traversal/)
- [606. Construct String from Binary Tree](../../0501-1000/0606-construct-string-from-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-quad-tree/)
