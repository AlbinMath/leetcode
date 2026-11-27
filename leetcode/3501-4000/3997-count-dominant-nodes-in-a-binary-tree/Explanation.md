# LeetCode 3997: Count Dominant Nodes in a Binary Tree

**LeetCode Problem #3997 — Count Dominant Nodes in a Binary Tree**
Solve LeetCode Count Dominant Nodes in a Binary Tree using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Dominant Nodes in a Binary Tree |
| LeetCode | #3997 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a complete binary tree .

A node `x` is called **dominant** if its value is equal to the maximum value among all nodes in the subtree rooted at `x`.

Return the number of dominant nodes in the tree.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^9`
- The tree is guaranteed to be a complete binary tree.

## Examples
### Example 1
- **Input:** `root = [5,3,8,2,4,7,1]`
- **Output:** `5`
- **Explanation:** The leaf nodes with values 2, 4, 7, and 1 are dominant. 
 The node with value 8 is dominant because its value is the maximum value in its subtree `[8, 7, 1]`. 
 Thus, the answer is 5.

### Example 2
- **Input:** `root = [1,2,3,1,2]`
- **Output:** `4`
- **Explanation:** The leaf nodes with values 1, 2, and 3 are dominant. 
 The node with value 2 whose subtree is `[2, 1, 2]` is dominant because its value is the maximum value in its subtree. 
 Thus, the answer is 4.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Dominant Nodes in a Binary Tree**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,3,8,2,4,7,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The leaf nodes with values 2, 4, 7, and 1 are dominant. 
 The node with value 8 is dominant because its value is the maximum value in its subtree `[8, 7, 1]`. 
 Thus, the answer is 5.

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
var countDominantNodes = function(root) {
    let dominantCount = 0;
    
    function dfs(node) {
        if (!node) return 0;
        
        const leftMax = dfs(node.left);
        const rightMax = dfs(node.right);
        
        const currMax = Math.max(node.val, leftMax, rightMax);
        if (currMax === node.val) {
            dominantCount++;
        }
        
        return currMax;
    }
    
    dfs(root);
    return dominantCount;
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
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0863-all-nodes-distance-k-in-binary-tree/)
- [1361. Validate Binary Tree Nodes](../../1001-1500/1361-validate-binary-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/)
