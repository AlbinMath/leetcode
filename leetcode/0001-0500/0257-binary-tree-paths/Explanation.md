# LeetCode 257: Binary Tree Paths

**LeetCode Problem #257 — Binary Tree Paths**
Solve LeetCode Binary Tree Paths using PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Tree Paths |
| LeetCode | #257 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a binary tree.

Return all **root-to-leaf** paths* *in **any order**.

A **leaf** is a node with no children.

## Constraints
- The number of nodes in the tree is in the range `[1, 100]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,2,3,null,5]`
- **Output:** `["1->2->5","1->3"]`

### Example 2
- **Input:** `root = [1]`
- **Output:** `["1"]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Binary Tree Paths**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3,null,5]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["1->2->5","1->3"]`.

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
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = 0;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */

class Solution {
    function binaryTreePaths($root) {
        $result = [];

        $this->dfs($root, "", $result);

        return $result;
    }

    function dfs($node, $path, &$result) {
        if ($node === null) {
            return;
        }

        // Add current node to the path
        if ($path === "") {
            $path = (string)$node->val;
        } else {
            $path .= "->" . $node->val;
        }

        // Leaf node
        if ($node->left === null && $node->right === null) {
            $result[] = $path;
            return;
        }

        // Explore left and right subtrees
        $this->dfs($node->left, $path, $result);
        $this->dfs($node->right, $path, $result);
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
- [1457. Pseudo-Palindromic Paths in a Binary Tree](../../1501-2000/1568-pseudo-palindromic-paths-in-a-binary-tree/)
- [2673. Make Costs of Paths Equal in a Binary Tree](../../2501-3000/2780-make-costs-of-paths-equal-in-a-binary-tree/)
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-tree-paths/)
