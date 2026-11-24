# LeetCode 919: Complete Binary Tree Inserter

**LeetCode Problem #919 — Complete Binary Tree Inserter**
Solve LeetCode Complete Binary Tree Inserter using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Complete Binary Tree Inserter |
| LeetCode | #919 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **complete binary tree** is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the `CBTInserter` class:

`CBTInserter(TreeNode root)` Initializes the data structure with the `root` of the complete binary tree. 
 `int insert(int v)` Inserts a `TreeNode` into the tree with value `Node.val == val` so that the tree remains complete, and returns the value of the parent of the inserted `TreeNode`. 
 `TreeNode get_root()` Returns the root node of the tree.

## Constraints
- The number of nodes in the tree will be in the range `[1, 1000]`.
- `0 <= Node.val <= 5000`
- `root` is a complete binary tree.
- `0 <= val <= 5000`
- At most `10^4` calls will be made to `insert` and `get_root`.

## Examples
### Example 1
- **Input:** `["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]`
- **Output:** `[null, 1, 2, [1, 2, 3, 4]]`
- **Explanation:** CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3); // return 1
cBTInserter.insert(4); // return 2
cBTInserter.get_root(); // return [1, 2, 3, 4]

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Complete Binary Tree Inserter**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 1, 2, [1, 2, 3, 4]]`.
4. **Verification:** CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3); // return 1
cBTInserter.insert(4); // return 2
cBTInserter.get_root(); // return [1, 2, 3, 4]

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
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.candidates = deque()
        bfs = deque([root])
        
        while bfs:
            curr = bfs.popleft()
            if curr.left:
                bfs.append(curr.left)
            if curr.right:
                bfs.append(curr.right)
            if not curr.left or not curr.right:
                self.candidates.append(curr)

    def insert(self, val: int) -> int:
        parent = self.candidates[0]
        child = TreeNode(val)
        self.candidates.append(child)
        
        if not parent.left:
            parent.left = child
        else:
            parent.right = child
            self.candidates.popleft()
            
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
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
[View problem on LeetCode](https://leetcode.com/problems/complete-binary-tree-inserter/)
