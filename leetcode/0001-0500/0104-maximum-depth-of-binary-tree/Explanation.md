# LeetCode 104: Maximum Depth of Binary Tree

**LeetCode Problem #104 — Maximum Depth of Binary Tree**
Solve LeetCode Maximum Depth of Binary Tree using JavaScript, PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Depth of Binary Tree |
| LeetCode | #104 |
| Difficulty | Easy |
| Language | JavaScript, PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `3`

### Example 2
- **Input:** `root = [1,null,2]`
- **Output:** `2`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Maximum Depth of Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

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
3. **Result:** Arrive at the expected output `3`.

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
var maxDepth = function(root) {
    if (root === null) {
        return 0;
    }

    const leftDepth = maxDepth(root.left);
    const rightDepth = maxDepth(root.right);

    return 1 + Math.max(leftDepth, rightDepth);
};
```

### PHP
```php
class Solution {
    function maxDepth($root) {
        // Empty tree
        if ($root === null) {
            return 0;
        }

        // Calculate left and right depths
        $leftDepth = $this->maxDepth($root->left);
        $rightDepth = $this->maxDepth($root->right);

        // Current node + deeper subtree
        return 1 + max($leftDepth, $rightDepth);
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [559. Maximum Depth of N-ary Tree](../../0501-1000/0559-maximum-depth-of-n-ary-tree/)
- [654. Maximum Binary Tree](../../0501-1000/0654-maximum-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
