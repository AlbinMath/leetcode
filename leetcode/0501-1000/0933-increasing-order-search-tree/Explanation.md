# LeetCode 897: Increasing Order Search Tree

**LeetCode Problem #897 — Increasing Order Search Tree**
Solve LeetCode Increasing Order Search Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Increasing Order Search Tree |
| LeetCode | #897 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

## Constraints
- The number of nodes in the given tree will be in the range `[1, 100]`.
- `0 <= Node.val <= 1000`

## Examples
### Example 1
- **Input:** `root = [5,3,6,2,4,null,8,1,null,null,null,7,9]`
- **Output:** `[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]`

### Example 2
- **Input:** `root = [5,1,7]`
- **Output:** `[1,null,5,null,7]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Increasing Order Search Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,3,6,2,4,null,8,1,null,null,null,7,9]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        current = dummy

        def inorder(node):
            nonlocal current

            if not node:
                return

            inorder(node.left)

            node.left = None
            current.right = node
            current = node

            inorder(node.right)

        inorder(root)
        return dummy.right
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [99. Recover Binary Search Tree](../../0001-0500/0099-recover-binary-search-tree/)
- [102. Binary Tree Level Order Traversal](../../0001-0500/0102-binary-tree-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/increasing-order-search-tree/)
