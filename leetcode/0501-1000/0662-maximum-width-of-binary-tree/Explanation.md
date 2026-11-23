# LeetCode 662: Maximum Width of Binary Tree

**LeetCode Problem #662 — Maximum Width of Binary Tree**
Solve LeetCode Maximum Width of Binary Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Width of Binary Tree |
| LeetCode | #662 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, return *the **maximum width** of the given tree*.

The **maximum width** of a tree is the maximum **width** among all levels.

The **width** of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is **guaranteed** that the answer will in the range of a **32-bit** signed integer.

## Constraints
- The number of nodes in the tree is in the range `[1, 3000]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,3,2,5,3,null,9]`
- **Output:** `4`
- **Explanation:** The maximum width exists in the third level with length 4 (5,3,null,9).

### Example 2
- **Input:** `root = [1,3,2,5,null,null,9,6,null,7]`
- **Output:** `7`
- **Explanation:** The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

### Example 3
- **Input:** `root = [1,3,2,5]`
- **Output:** `2`
- **Explanation:** The maximum width exists in the second level with length 2 (3,2).

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Width of Binary Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,3,2,5,3,null,9]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The maximum width exists in the third level with length 4 (5,3,null,9).

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import Optional
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            start_idx = queue[0][1]
            end_idx = start_idx
            for _ in range(len(queue)):
                curr, idx = queue.popleft()
                end_idx = idx
                norm_idx = idx - start_idx
                if curr.left:
                    queue.append((curr.left, norm_idx << 1))
                if curr.right:
                    queue.append((curr.right, (norm_idx << 1) | 1))
                    
            if end_idx - start_idx + 1 > max_width:
                max_width = end_idx - start_idx + 1
                
        return max_width
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
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [654. Maximum Binary Tree](../../0501-1000/0654-maximum-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-width-of-binary-tree/)
