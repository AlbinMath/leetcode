# LeetCode 110: Balanced Binary Tree

**LeetCode Problem #110 — Balanced Binary Tree**
Solve LeetCode Balanced Binary Tree using PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Balanced Binary Tree |
| LeetCode | #110 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary tree, determine if it is **height-balanced** .

## Constraints
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Examples
### Example 1
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `true`

### Example 2
- **Input:** `root = [1,2,2,3,3,null,null,4,4]`
- **Output:** `false`

### Example 3
- **Input:** `root = []`
- **Output:** `true`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Balanced Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,9,20,null,null,15,7]`.
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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function isBalanced($root) {
        return $this->height($root) != -1;
    }

    function height($node) {
        // Empty tree has height 0
        if ($node === null) {
            return 0;
        }

        // Check left subtree
        $leftHeight = $this->height($node->left);

        if ($leftHeight == -1) {
            return -1;
        }

        // Check right subtree
        $rightHeight = $this->height($node->right);

        if ($rightHeight == -1) {
            return -1;
        }

        // Current node is unbalanced
        if (abs($leftHeight - $rightHeight) > 1) {
            return -1;
        }

        // Return height of current subtree
        return 1 + max($leftHeight, $rightHeight);
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
[View problem on LeetCode](https://leetcode.com/problems/balanced-binary-tree/)
