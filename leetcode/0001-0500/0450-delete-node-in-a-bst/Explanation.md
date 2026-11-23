# LeetCode 450: Delete Node in a BST

**LeetCode Problem #450 — Delete Node in a BST**
Solve LeetCode Delete Node in a BST using JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Node in a BST |
| LeetCode | #450 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return *the **root node reference** (possibly updated) of the BST*.

Basically, the deletion can be divided into two stages:

Search for a node to remove. 
 If the node is found, delete the node.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- Each node has a **unique** value.
- `root` is a valid binary search tree.
- `-10^5 <= key <= 10^5`

## Examples
### Example 1
- **Input:** `root = [5,3,6,2,4,null,7], key = 3`
- **Output:** `[5,4,6,2,null,null,7]`
- **Explanation:** Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

### Example 2
- **Input:** `root = [5,3,6,2,4,null,7], key = 0`
- **Output:** `[5,3,6,2,4,null,7]`
- **Explanation:** The tree does not contain a node with value = 0.

### Example 3
- **Input:** `root = [], key = 0`
- **Output:** `[]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Delete Node in a BST**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,3,6,2,4,null,7], key = 3`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,4,6,2,null,null,7]`.
4. **Verification:** Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var deleteNode = function(root, key) {
    if (root === null) {
        return null;
    }

    if (key < root.val) {
        root.left = deleteNode(root.left, key);
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key);
    } else {
        // Case 1: No left child
        if (root.left === null) {
            return root.right;
        }

        // Case 2: No right child
        if (root.right === null) {
            return root.left;
        }

        // Case 3: Two children
        let successor = root.right;

        while (successor.left !== null) {
            successor = successor.left;
        }

        root.val = successor.val;
        root.right = deleteNode(root.right, successor.val);
    }

    return root;
};
```

### Python
```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
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
- [237. Delete Node in a Linked List](../../0001-0500/0237-delete-node-in-a-linked-list/)
- [2095. Delete the Middle Node of a Linked List](../../2001-2500/2216-delete-the-middle-node-of-a-linked-list/)
- [196. Delete Duplicate Emails](../../0001-0500/0196-delete-duplicate-emails/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)
