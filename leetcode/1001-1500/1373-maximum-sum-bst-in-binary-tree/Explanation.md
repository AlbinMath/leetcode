# LeetCode 1373: Maximum Sum BST in Binary Tree

**LeetCode Problem #1373 — Maximum Sum BST in Binary Tree**
Solve LeetCode Maximum Sum BST in Binary Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum BST in Binary Tree |
| LeetCode | #1373 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **binary tree** `root`, return *the maximum sum of all keys of **any** sub-tree which is also a Binary Search Tree (BST)*.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys **less than** the node's key. 
 The right subtree of a node contains only nodes with keys **greater than** the node's key. 
 Both the left and right subtrees must also be binary search trees.

## Constraints
- The number of nodes in the tree is in the range `[1, 4 * 10^4]`.
- `-4 * 10^4 <= Node.val <= 4 * 10^4`

## Examples
### Example 1
- **Input:** `root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]`
- **Output:** `20`
- **Explanation:** Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

### Example 2
- **Input:** `root = [4,3,null,1,2]`
- **Output:** `2`
- **Explanation:** Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

### Example 3
- **Input:** `root = [-4,-2,-5]`
- **Output:** `0`
- **Explanation:** All values are negatives. Return an empty BST.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Maximum Sum BST in Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def traverse(node):
            nonlocal max_sum
            if not node:
                # is_bst, min_val, max_val, sum_val
                return True, float('inf'), float('-inf'), 0

            left_is_bst, left_min, left_max, left_sum = traverse(node.left)
            right_is_bst, right_min, right_max, right_sum = traverse(node.right)

            # Check BST condition
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, curr_sum)
                
                curr_min = min(left_min, node.val)
                curr_max = max(right_max, node.val)
                return True, curr_min, curr_max, curr_sum

            # Not a BST
            return False, 0, 0, 0

        traverse(root)
        return max_sum
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [1161. Maximum Level Sum of a Binary Tree](../../1001-1500/1161-maximum-level-sum-of-a-binary-tree/)
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/)
