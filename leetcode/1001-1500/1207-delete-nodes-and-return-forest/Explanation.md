# LeetCode 1110: Delete Nodes And Return Forest

**LeetCode Problem #1110 — Delete Nodes And Return Forest**
Solve LeetCode Delete Nodes And Return Forest using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Nodes And Return Forest |
| LeetCode | #1110 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

## Constraints
- The number of nodes in the given tree is at most `1000`.
- Each node has a distinct value between `1` and `1000`.
- `to_delete.length <= 1000`
- `to_delete` contains distinct values between `1` and `1000`.

## Examples
### Example 1
- **Input:** `root = [1,2,3,4,5,6,7], to_delete = [3,5]`
- **Output:** `[[1,2,null,4],[6],[7]]`

### Example 2
- **Input:** `root = [1,2,4,null,3], to_delete = [3]`
- **Output:** `[[1,2,4]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Delete Nodes And Return Forest**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3,4,5,6,7], to_delete = [3,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,null,4],[6],[7]]`.

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
var delNodes = function(root, to_delete) {
    const deleteSet = new Set(to_delete);
    const forest = [];
    
    function dfs(node, isRoot) {
        if (!node) return null;
        
        const deleted = deleteSet.has(node.val);
        
        // If this node survives and has no parent, it is a root in the forest
        if (!deleted && isRoot) {
            forest.push(node);
        }
        
        // If current node is deleted, its children become new roots
        node.left = dfs(node.left, deleted);
        node.right = dfs(node.right, deleted);
        
        return deleted ? null : node;
    }
    
    dfs(root, true);
    return forest;
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
- [3217. Delete Nodes From Linked List Present in Array](../../3501-4000/3501-delete-nodes-from-linked-list-present-in-array/)
- [657. Robot Return to Origin](../../0501-1000/0657-robot-return-to-origin/)
- [2703. Return Length of Arguments Passed](../../2501-3000/2820-return-length-of-arguments-passed/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-nodes-and-return-forest/)
