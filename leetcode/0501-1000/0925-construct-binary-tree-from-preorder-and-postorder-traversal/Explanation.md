# LeetCode 889: Construct Binary Tree from Preorder and Postorder Traversal

**LeetCode Problem #889 — Construct Binary Tree from Preorder and Postorder Traversal**
Solve LeetCode Construct Binary Tree from Preorder and Postorder Traversal using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Binary Tree from Preorder and Postorder Traversal |
| LeetCode | #889 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integer arrays, `preorder` and `postorder` where `preorder` is the preorder traversal of a binary tree of **distinct** values and `postorder` is the postorder traversal of the same tree, reconstruct and return *the binary tree*.

If there exist multiple answers, you can **return any** of them.

## Constraints
- `1 <= preorder.length <= 30`
- `1 <= preorder[i] <= preorder.length`
- All the values of `preorder` are **unique**.
- `postorder.length == preorder.length`
- `1 <= postorder[i] <= postorder.length`
- All the values of `postorder` are **unique**.
- It is guaranteed that `preorder` and `postorder` are the preorder traversal and postorder traversal of the same binary tree.

## Examples
### Example 1
- **Input:** `preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]`
- **Output:** `[1,2,3,4,5,6,7]`

### Example 2
- **Input:** `preorder = [1], postorder = [1]`
- **Output:** `[1]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Construct Binary Tree from Preorder and Postorder Traversal**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4,5,6,7]`.

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
from typing import List, Optional


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(postorder)}

        def build(pl: int, pr: int, ql: int) -> Optional[TreeNode]:
            if pl > pr:
                return None
            root = TreeNode(preorder[pl])
            if pl == pr:
                return root
            idx = pos[preorder[pl + 1]]
            size = idx - ql + 1
            root.left = build(pl + 1, pl + size, ql)
            root.right = build(pl + size + 1, pr, idx + 1)
            return root

        return build(0, len(preorder) - 1, 0)
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
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../../0001-0500/0106-construct-binary-tree-from-inorder-and-postorder-traversal/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [1008. Construct Binary Search Tree from Preorder Traversal](../../1001-1500/1050-construct-binary-search-tree-from-preorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)
