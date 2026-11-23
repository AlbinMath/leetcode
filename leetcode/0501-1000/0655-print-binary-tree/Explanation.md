# LeetCode 655: Print Binary Tree

**LeetCode Problem #655 — Print Binary Tree**
Solve LeetCode Print Binary Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print Binary Tree |
| LeetCode | #655 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, construct a **0-indexed** `m x n` string matrix `res` that represents a **formatted layout** of the tree. The formatted layout matrix should be constructed using the following rules:

The **height** of the tree is `height` and the number of rows `m` should be equal to `height + 1`. 
 The number of columns `n` should be equal to `2^height+1 - 1`. 
 Place the **root node** in the **middle** of the **top row** (more formally, at location `res[0][(n-1)/2]`). 
 For each node that has been placed in the matrix at position `res[r][c]`, place its **left child** at `res[r+1][c-2^height-r-1]` and its **right child** at `res[r+1][c+2^height-r-1]`. 
 Continue this process until all the nodes in the tree have been placed. 
 Any empty cells should contain the empty string `""`.

Return *the constructed matrix *`res`.

## Constraints
- The number of nodes in the tree is in the range `[1, 2^10]`.
- `-99 <= Node.val <= 99`
- The depth of the tree will be in the range `[1, 10]`.

## Examples
### Example 1
- **Input:** `root = [1,2]`
- **Output:** `[["","1",""],
 ["2","",""]]`

### Example 2
- **Input:** `root = [1,2,3,null,4]`
- **Output:** `[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Print Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["","1",""],
 ["2","",""]]`.

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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))
            
        height = get_height(root)
        m = height + 1
        n = (1 << (height + 1)) - 1
        res = [[""] * n for _ in range(m)]
        
        def fill(node: Optional[TreeNode], r: int, c: int) -> None:
            if not node:
                return
            res[r][c] = str(node.val)
            if r < height:
                offset = 1 << (height - r - 1)
                if node.left:
                    fill(node.left, r + 1, c - offset)
                if node.right:
                    fill(node.right, r + 1, c + offset)
                    
        fill(root, 0, (n - 1) >> 1)
        return res
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
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [99. Recover Binary Search Tree](../../0001-0500/0099-recover-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-binary-tree/)
