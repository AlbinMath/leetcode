# LeetCode 2415: Reverse Odd Levels of Binary Tree

**LeetCode Problem #2415 — Reverse Odd Levels of Binary Tree**
Solve LeetCode Reverse Odd Levels of Binary Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Odd Levels of Binary Tree |
| LeetCode | #2415 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a **perfect** binary tree, reverse the node values at each **odd** level of the tree.

For example, suppose the node values at level 3 are `[2,1,3,4,7,11,29,18]`, then it should become `[18,29,11,7,4,3,1,2]`.

Return *the root of the reversed tree*.

A binary tree is **perfect** if all parent nodes have two children and all leaves are on the same level.

The **level** of a node is the number of edges along the path between it and the root node.

## Constraints
- The number of nodes in the tree is in the range `[1, 2^14]`.
- `0 <= Node.val <= 10^5`
- `root` is a **perfect** binary tree.

## Examples
### Example 1
- **Input:** `root = [2,3,5,8,13,21,34]`
- **Output:** `[2,5,3,8,13,21,34]`
- **Explanation:** The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

### Example 2
- **Input:** `root = [7,13,11]`
- **Output:** `[7,11,13]`
- **Explanation:** The nodes at level 1 are 13, 11, which are reversed and become 11, 13.

### Example 3
- **Input:** `root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]`
- **Output:** `[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]`
- **Explanation:** The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Reverse Odd Levels of Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [2,3,5,8,13,21,34]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,5,3,8,13,21,34]`.
4. **Verification:** The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(a, b, level):
            if not a:
                return
            if level % 2 == 1:
                a.val, b.val = b.val, a.val
            dfs(a.left, b.right, level + 1)
            dfs(a.right, b.left, level + 1)

        dfs(root.left, root.right, 1)
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
- [637. Average of Levels in Binary Tree](../../0501-1000/0637-average-of-levels-in-binary-tree/)
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/)
