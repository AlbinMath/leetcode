# LeetCode 951: Flip Equivalent Binary Trees

**LeetCode Problem #951 — Flip Equivalent Binary Trees**
Solve LeetCode Flip Equivalent Binary Trees using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flip Equivalent Binary Trees |
| LeetCode | #951 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
For a binary tree **T**, we can define a **flip operation** as follows: choose any node, and swap the left and right child subtrees.

A binary tree **X** is *flip equivalent* to a binary tree **Y** if and only if we can make **X** equal to **Y** after some number of flip operations.

Given the roots of two binary trees `root1` and `root2`, return `true` if the two trees are flip equivalent or `false` otherwise.

## Constraints
- The number of nodes in each tree is in the range `[0, 100]`.
- Each tree will have **unique node values** in the range `[0, 99]`.

## Examples
### Example 1
- **Input:** `root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]`
- **Output:** `true`
- **Explanation:** We flipped at nodes with values 1, 3, and 5.

### Example 2
- **Input:** `root1 = [], root2 = []`
- **Output:** `true`

### Example 3
- **Input:** `root1 = [], root2 = [1]`
- **Output:** `false`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Flip Equivalent Binary Trees**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We flipped at nodes with values 1, 3, and 5.

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
from typing import Optional

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (
            (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
            or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        )
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
- [971. Flip Binary Tree To Match Preorder Traversal](../../1001-1500/1011-flip-binary-tree-to-match-preorder-traversal/)
- [2556. Disconnect Path in a Binary Matrix by at Most One Flip](../../2501-3000/2641-disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)
- [95. Unique Binary Search Trees II](../../0001-0500/0095-unique-binary-search-trees-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flip-equivalent-binary-trees/)
