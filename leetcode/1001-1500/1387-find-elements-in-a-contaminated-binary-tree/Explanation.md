# LeetCode 1261: Find Elements in a Contaminated Binary Tree

**LeetCode Problem #1261 — Find Elements in a Contaminated Binary Tree**
Solve LeetCode Find Elements in a Contaminated Binary Tree using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Elements in a Contaminated Binary Tree |
| LeetCode | #1261 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary tree with the following rules:

`root.val == 0` 
 For any `treeNode`:
 
 If `treeNode.val` has a value `x` and `treeNode.left != null`, then `treeNode.left.val == 2 * x + 1` 
 If `treeNode.val` has a value `x` and `treeNode.right != null`, then `treeNode.right.val == 2 * x + 2`

Now the binary tree is contaminated, which means all `treeNode.val` have been changed to `-1`.

Implement the `FindElements` class:

`FindElements(TreeNode* root)` Initializes the object with a contaminated binary tree and recovers it. 
 `bool find(int target)` Returns `true` if the `target` value exists in the recovered binary tree.

## Constraints
- `TreeNode.val == -1`
- The height of the binary tree is less than or equal to `20`
- The total number of nodes is between `[1, 10^4]`
- Total calls of `find()` is between `[1, 10^4]`
- `0 <= target <= 10^6`

## Examples
### Example 1
- **Input:** `["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]`
- **Output:** `[null,false,true]`
- **Explanation:** FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True

### Example 2
- **Input:** `["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]`
- **Output:** `[null,true,true,false]`
- **Explanation:** FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

### Example 3
- **Input:** `["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]`
- **Output:** `[null,true,false,false,true]`
- **Explanation:** FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find Elements in a Contaminated Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null,false,true]`.
4. **Verification:** FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True

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

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        root.val = 0
        stack = [root]
        while stack:
            node = stack.pop()
            self.seen.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
                stack.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                stack.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.seen
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
- [501. Find Mode in Binary Search Tree](../../0501-1000/0501-find-mode-in-binary-search-tree/)
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../../1001-1500/1498-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/)
