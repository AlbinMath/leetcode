# LeetCode 538: Convert BST to Greater Tree

**LeetCode Problem #538 — Convert BST to Greater Tree**
Solve LeetCode Convert BST to Greater Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert BST to Greater Tree |
| LeetCode | #538 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a *binary search tree* is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys **less than** the node's key. 
 The right subtree of a node contains only nodes with keys **greater than** the node's key. 
 Both the left and right subtrees must also be binary search trees.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- All the values in the tree are **unique**.
- `root` is guaranteed to be a valid binary search tree.

## Examples
### Example 1
- **Input:** `root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]`
- **Output:** `[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]`

### Example 2
- **Input:** `root = [0,null,1]`
- **Output:** `[1,null,1]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Convert BST to Greater Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]`.

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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0
        
        def reverse_inorder(node: Optional[TreeNode]):
            nonlocal running_sum
            if not node:
                return
            
            # 1. Visit all greater nodes first
            reverse_inorder(node.right)
            
            # 2. Update current node
            running_sum += node.val
            node.val = running_sum
            
            # 3. Visit smaller nodes
            reverse_inorder(node.left)
            
        reverse_inorder(root)
        return root
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
- [1373. Maximum Sum BST in Binary Tree](../../1001-1500/1475-maximum-sum-bst-in-binary-tree/)
- [1038. Binary Search Tree to Greater Sum Tree](../../1001-1500/1114-binary-search-tree-to-greater-sum-tree/)
- [108. Convert Sorted Array to Binary Search Tree](../../0001-0500/0108-convert-sorted-array-to-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-bst-to-greater-tree/)
