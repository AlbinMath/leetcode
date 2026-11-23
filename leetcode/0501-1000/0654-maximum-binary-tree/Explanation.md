# LeetCode 654: Maximum Binary Tree

**LeetCode Problem #654 — Maximum Binary Tree**
Solve LeetCode Maximum Binary Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Binary Tree |
| LeetCode | #654 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` with no duplicates. A **maximum binary tree** can be built recursively from `nums` using the following algorithm:

Create a root node whose value is the maximum value in `nums`. 
 Recursively build the left subtree on the **subarray prefix** to the **left** of the maximum value. 
 Recursively build the right subtree on the **subarray suffix** to the **right** of the maximum value.

Return *the **maximum binary tree** built from *`nums`.

## Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
- All integers in `nums` are **unique**.

## Examples
### Example 1
- **Input:** `nums = [3,2,1,6,0,5]`
- **Output:** `[6,3,5,null,2,0,null,null,1]`
- **Explanation:** The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
 - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
 - Empty array, so no child.
 - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
 - Empty array, so no child.
 - Only one element, so child is a node with value 1.
 - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
 - Only one element, so child is a node with value 0.
 - Empty array, so no child.

### Example 2
- **Input:** `nums = [3,2,1]`
- **Output:** `[3,null,2,null,1]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Binary Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,1,6,0,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,3,5,null,2,0,null,null,1]`.
4. **Verification:** The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
 - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
 - Empty array, so no child.
 - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
 - Empty array, so no child.
 - Only one element, so child is a node with value 1.
 - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
 - Only one element, so child is a node with value 0.
 - Empty array, so no child.

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
from typing import List, Optional

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for x in nums:
            node = TreeNode(x)
            last = None
            while stack and stack[-1].val < x:
                last = stack.pop()
            node.left = last
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
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
- [662. Maximum Width of Binary Tree](../../0501-1000/0662-maximum-width-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-binary-tree/)
