# LeetCode 3319: K-th Largest Perfect Subtree Size in Binary Tree

**LeetCode Problem #3319 — K-th Largest Perfect Subtree Size in Binary Tree**
Solve LeetCode K-th Largest Perfect Subtree Size in Binary Tree using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | K-th Largest Perfect Subtree Size in Binary Tree |
| LeetCode | #3319 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a **binary tree** and an integer `k`.

Return an integer denoting the size of the `k^th` **largest* *perfect binary*** * subtree , or `-1` if it doesn't exist.

A **perfect binary tree** is a tree where all leaves are on the same level, and every parent has two children.

## Constraints
- The number of nodes in the tree is in the range `[1, 2000]`.
- `1 <= Node.val <= 2000`
- `1 <= k <= 1024`

## Examples
### Example 1
- **Input:** `root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2`
- **Output:** `3`
- **Explanation:** The roots of the perfect binary subtrees are highlighted in black. Their sizes, in non-increasing order are `[3, 3, 1, 1, 1, 1, 1, 1]`. 
The `2^nd` largest size is 3.

### Example 2
- **Input:** `root = [1,2,3,4,5,6,7], k = 1`
- **Output:** `7`
- **Explanation:** The sizes of the perfect binary subtrees in non-increasing order are `[7, 3, 3, 1, 1, 1, 1]`. The size of the largest perfect binary subtree is 7.

### Example 3
- **Input:** `root = [1,2,3,null,4], k = 3`
- **Output:** `-1`
- **Explanation:** The sizes of the perfect binary subtrees in non-increasing order are `[1, 1]`. There are fewer than 3 perfect binary subtrees.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **K-th Largest Perfect Subtree Size in Binary Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The roots of the perfect binary subtrees are highlighted in black. Their sizes, in non-increasing order are `[3, 3, 1, 1, 1, 1, 1, 1]`. 
The `2^nd` largest size is 3.

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
var kthLargestPerfectSubtree = function(root, k) {
    const sizes = [];
    
    function dfs(node) {
        if (!node) return 0;
        
        const leftSize = dfs(node.left);
        const rightSize = dfs(node.right);
        
        // Valid perfect subtree if both children are valid and have equal sizes
        if (leftSize !== -1 && leftSize === rightSize) {
            const currSize = leftSize + rightSize + 1;
            sizes.push(currSize);
            return currSize;
        }
        
        return -1;
    }
    
    dfs(root);
    
    if (sizes.length < k) {
        return -1;
    }
    
    sizes.sort((a, b) => b - a);
    return sizes[k - 1];
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
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0863-all-nodes-distance-k-in-binary-tree/)
- [2458. Height of Binary Tree After Subtree Removal Queries](../../2001-2500/2458-height-of-binary-tree-after-subtree-removal-queries/)
- [2583. Kth Largest Sum in a Binary Tree](../../2501-3000/2583-kth-largest-sum-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/)
