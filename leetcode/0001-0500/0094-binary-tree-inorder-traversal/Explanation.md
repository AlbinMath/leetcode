# LeetCode 94: Binary Tree Inorder Traversal

**LeetCode Problem #94 — Binary Tree Inorder Traversal**
Solve LeetCode Binary Tree Inorder Traversal using JavaScript, PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Tree Inorder Traversal |
| LeetCode | #94 |
| Difficulty | Easy |
| Language | JavaScript, PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,null,2,3]`
- **Output:** `[1,3,2]`

### Example 2
- **Input:** `root = [1,2,3,4,5,null,8,null,null,6,7,9]`
- **Output:** `[4,2,6,5,7,1,3,9,8]`

### Example 3
- **Input:** `root = []`
- **Output:** `[]`

### Example 4
- **Input:** `root = [1]`
- **Output:** `[1]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Binary Tree Inorder Traversal**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,null,2,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,2]`.

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
JavaScript, PHP

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)


### JavaScript
```javascript
var inorderTraversal = function(root) {
    const result = [];
    const stack = [];
    let current = root;

    while (current !== null || stack.length > 0) {
        // Go as far left as possible
        while (current !== null) {
            stack.push(current);
            current = current.left;
        }

        // Visit the node
        current = stack.pop();
        result.push(current.val);

        // Explore the right subtree
        current = current.right;
    }

    return result;
};
```

### PHP
```php
class Solution {
    function inorderTraversal($root) {
        $result = [];
        $stack = [];
        $current = $root;

        while ($current !== null || !empty($stack)) {

            // Go as far left as possible
            while ($current !== null) {
                $stack[] = $current;
                $current = $current->left;
            }

            // Process the node
            $current = array_pop($stack);
            $result[] = $current->val;

            // Move to the right subtree
            $current = $current->right;
        }

        return $result;
    }
}
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
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../../0001-0500/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../../0001-0500/0106-construct-binary-tree-from-inorder-and-postorder-traversal/)
- [102. Binary Tree Level Order Traversal](../../0001-0500/0102-binary-tree-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/)
