# LeetCode 1080: Insufficient Nodes in Root to Leaf Paths

**LeetCode Problem #1080 — Insufficient Nodes in Root to Leaf Paths**
Solve LeetCode Insufficient Nodes in Root to Leaf Paths using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insufficient Nodes in Root to Leaf Paths |
| LeetCode | #1080 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree and an integer `limit`, delete all **insufficient nodes** in the tree simultaneously, and return *the root of the resulting binary tree*.

A node is **insufficient** if every root to **leaf** path intersecting this node has a sum strictly less than `limit`.

A **leaf** is a node with no children.

## Constraints
- The number of nodes in the tree is in the range `[1, 5000]`.
- `-10^5 <= Node.val <= 10^5`
- `-10^9 <= limit <= 10^9`

## Examples
### Example 1
- **Input:** `root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1`
- **Output:** `[1,2,3,4,null,null,7,8,9,null,14]`

### Example 2
- **Input:** `root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22`
- **Output:** `[5,4,8,11,null,17,4,7,null,null,null,5]`

### Example 3
- **Input:** `root = [1,2,-3,-5,null,4,null], limit = -1`
- **Output:** `[1,null,-3,4]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Insufficient Nodes in Root to Leaf Paths**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4,null,null,7,8,9,null,14]`.

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
var sufficientSubset = function(root, limit) {
    if (!root) return null;
    
    // Original leaf: check if path sum meets the limit
    if (!root.left && !root.right) {
        return root.val < limit ? null : root;
    }
    
    // Recursively prune children with remaining required sum
    root.left = sufficientSubset(root.left, limit - root.val);
    root.right = sufficientSubset(root.right, limit - root.val);
    
    // If both subtrees were completely pruned, no valid path passes through root
    if (!root.left && !root.right) {
        return null;
    }
    
    return root;
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
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1653-number-of-good-leaf-nodes-pairs/)
- [129. Sum Root to Leaf Numbers](../../0001-0500/0129-sum-root-to-leaf-numbers/)
- [1022. Sum of Root To Leaf Binary Numbers](../../1001-1500/1079-sum-of-root-to-leaf-binary-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/)
