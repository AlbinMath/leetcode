# LeetCode 101: Symmetric Tree

**LeetCode Problem #101 — Symmetric Tree**
Solve LeetCode Symmetric Tree using JavaScript, PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Symmetric Tree |
| LeetCode | #101 |
| Difficulty | Easy |
| Language | JavaScript, PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,2,2,3,4,4,3]`
- **Output:** `true`

### Example 2
- **Input:** `root = [1,2,2,null,3,null,3]`
- **Output:** `false`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Symmetric Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,2,3,4,4,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
var isSymmetric = function(root) {
    function isMirror(left, right) {
        if (left === null && right === null) {
            return true;
        }

        if (left === null || right === null) {
            return false;
        }

        if (left.val !== right.val) {
            return false;
        }

        return isMirror(left.left, right.right) &&
               isMirror(left.right, right.left);
    }

    return isMirror(root.left, root.right);
};
```

### PHP
```php
class Solution {
    function isSymmetric($root) {
        return $this->isMirror($root->left, $root->right);
    }

    function isMirror($left, $right) {

        // Both are empty
        if ($left === null && $right === null) {
            return true;
        }

        // One is empty
        if ($left === null || $right === null) {
            return false;
        }

        // Values are different
        if ($left->val != $right->val) {
            return false;
        }

        // Compare opposite sides
        return $this->isMirror($left->left, $right->right)
            && $this->isMirror($left->right, $right->left);
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
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [99. Recover Binary Search Tree](../../0001-0500/0099-recover-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/symmetric-tree/)
