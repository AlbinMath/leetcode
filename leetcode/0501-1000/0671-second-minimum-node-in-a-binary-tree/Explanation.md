# LeetCode 671: Second Minimum Node In a Binary Tree

**LeetCode Problem #671 — Second Minimum Node In a Binary Tree**
Solve LeetCode Second Minimum Node In a Binary Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Second Minimum Node In a Binary Tree |
| LeetCode | #671 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `two` or `zero` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

## Constraints
- The number of nodes in the tree is in the range `[1, 25]`.
- `1 <= Node.val <= 2^31 - 1`
- `root.val == min(root.left.val, root.right.val)` for each internal node of the tree.

## Examples
### Example 1
- **Input:** `root = [2,2,5,null,null,5,7]`
- **Output:** `5`
- **Explanation:** The smallest value is 2, the second smallest value is 5.

### Example 2
- **Input:** `root = [2,2,2]`
- **Output:** `-1`
- **Explanation:** The smallest value is 2, but there isn't any second smallest value.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Second Minimum Node In a Binary Tree**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [2,2,5,null,null,5,7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The smallest value is 2, the second smallest value is 5.

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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root):
        minimum = root.val
        second_min = float('inf')

        def dfs(node):
            nonlocal second_min

            if not node:
                return

            if minimum < node.val < second_min:
                second_min = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return second_min if second_min != float('inf') else -1
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
- [111. Minimum Depth of Binary Tree](../../0001-0500/0111-minimum-depth-of-binary-tree/)
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2001-2500/2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../../1001-1500/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/)
