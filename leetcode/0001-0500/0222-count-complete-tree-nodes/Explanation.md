# LeetCode 222: Count Complete Tree Nodes

**LeetCode Problem #222 — Count Complete Tree Nodes**
Solve LeetCode Count Complete Tree Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Complete Tree Nodes |
| LeetCode | #222 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a **complete** binary tree, return the number of the nodes in the tree.

According to ** Wikipedia **, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2^h` nodes inclusive at the last level `h`.

Design an algorithm that runs in less than O(n) time complexity.

## Constraints
- The number of nodes in the tree is in the range `[0, 5 * 10^4]`.
- `0 <= Node.val <= 5 * 10^4`
- The tree is guaranteed to be **complete**.

## Examples
### Example 1
- **Input:** `root = [1,2,3,4,5,6]`
- **Output:** `6`

### Example 2
- **Input:** `root = []`
- **Output:** `0`

### Example 3
- **Input:** `root = [1]`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Complete Tree Nodes**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3,4,5,6]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.

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
var countNodes = function(root) {
    if (root === null) {
        return 0;
    }

    let left = root.left;
    let right = root.right;
    let leftHeight = 0;
    let rightHeight = 0;

    while (left !== null) {
        leftHeight++;
        left = left.left;
    }

    while (right !== null) {
        rightHeight++;
        right = right.right;
    }

    // If both heights are equal, the tree is perfect
    if (leftHeight === rightHeight) {
        return Math.pow(2, leftHeight + 1) - 1;
    }

    // Otherwise, count recursively
    return 1 + countNodes(root.left) + countNodes(root.right);
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
- [1448. Count Good Nodes in Binary Tree](../../1001-1500/1448-count-good-nodes-in-binary-tree/)
- [3997. Count Dominant Nodes in a Binary Tree](../../3501-4000/3997-count-dominant-nodes-in-a-binary-tree/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1782-count-pairs-of-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/)
