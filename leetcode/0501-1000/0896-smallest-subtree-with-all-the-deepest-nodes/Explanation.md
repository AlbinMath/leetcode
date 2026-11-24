# LeetCode 865: Smallest Subtree with all the Deepest Nodes

**LeetCode Problem #865 — Smallest Subtree with all the Deepest Nodes**
Solve LeetCode Smallest Subtree with all the Deepest Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Subtree with all the Deepest Nodes |
| LeetCode | #865 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, the depth of each node is **the shortest distance to the root**.

Return *the smallest subtree* such that it contains **all the deepest nodes** in the original tree.

A node is called **the deepest** if it has the largest depth possible among any node in the entire tree.

The **subtree** of a node is a tree consisting of that node, plus the set of all descendants of that node.

## Constraints
- The number of nodes in the tree will be in the range `[1, 500]`.
- `0 <= Node.val <= 500`
- The values of the nodes in the tree are **unique**.

## Examples
### Example 1
- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4]`
- **Output:** `[2,7,4]`
- **Explanation:** We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

### Example 2
- **Input:** `root = [1]`
- **Output:** `[1]`
- **Explanation:** The root is the deepest node in the tree.

### Example 3
- **Input:** `root = [0,1,3,null,2]`
- **Output:** `[2]`
- **Explanation:** The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest Subtree with all the Deepest Nodes**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,5,1,6,2,0,8,null,null,7,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,7,4]`.
4. **Verification:** We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

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
var subtreeWithAllDeepest = function(root) {
    function dfs(node) {
        if (node === null) {
            return [0, null];
        }

        const [leftDepth, leftNode] = dfs(node.left);
        const [rightDepth, rightNode] = dfs(node.right);

        if (leftDepth > rightDepth) {
            return [leftDepth + 1, leftNode];
        }

        if (rightDepth > leftDepth) {
            return [rightDepth + 1, rightNode];
        }

        return [leftDepth + 1, node];
    }

    return dfs(root)[1];
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
- [2003. Smallest Missing Genetic Value in Each Subtree](../../2001-2500/2131-smallest-missing-genetic-value-in-each-subtree/)
- [3370. Smallest Number With All Set Bits](../../3501-4000/3676-smallest-number-with-all-set-bits/)
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0877-shortest-path-visiting-all-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)
