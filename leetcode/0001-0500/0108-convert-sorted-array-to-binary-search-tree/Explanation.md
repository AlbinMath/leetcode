# LeetCode 108: Convert Sorted Array to Binary Search Tree

**LeetCode Problem #108 — Convert Sorted Array to Binary Search Tree**
Solve LeetCode Convert Sorted Array to Binary Search Tree using JavaScript, PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert Sorted Array to Binary Search Tree |
| LeetCode | #108 |
| Difficulty | Easy |
| Language | JavaScript, PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a * ***height-balanced*** *binary search tree*.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in a **strictly increasing** order.

## Examples
### Example 1
- **Input:** `nums = [-10,-3,0,5,9]`
- **Output:** `[0,-3,9,-10,null,5]`
- **Explanation:** [0,-10,5,null,-3,null,9] is also accepted:

### Example 2
- **Input:** `nums = [1,3]`
- **Output:** `[3,1]`
- **Explanation:** [1,null,3] and [3,1] are both height-balanced BSTs.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Convert Sorted Array to Binary Search Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-10,-3,0,5,9]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,-3,9,-10,null,5]`.
4. **Verification:** [0,-10,5,null,-3,null,9] is also accepted:

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
var sortedArrayToBST = function(nums) {
    function buildTree(left, right) {
        if (left > right) {
            return null;
        }

        // Choose the middle element as the root.
        const mid = Math.floor((left + right) / 2);
        const root = new TreeNode(nums[mid]);

        // Build the left and right subtrees.
        root.left = buildTree(left, mid - 1);
        root.right = buildTree(mid + 1, right);

        return root;
    }

    return buildTree(0, nums.length - 1);
};
```

### PHP
```php
class Solution {
    function sortedArrayToBST($nums) {
        return $this->buildTree($nums, 0, count($nums) - 1);
    }

    function buildTree($nums, $left, $right) {
        // No elements
        if ($left > $right) {
            return null;
        }

        // Choose middle element
        $mid = intdiv($left + $right, 2);

        // Create root
        $root = new TreeNode($nums[$mid]);

        // Build left subtree
        $root->left = $this->buildTree(
            $nums,
            $left,
            $mid - 1
        );

        // Build right subtree
        $root->right = $this->buildTree(
            $nums,
            $mid + 1,
            $right
        );

        return $root;
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
- [109. Convert Sorted List to Binary Search Tree](../../0001-0500/0109-convert-sorted-list-to-binary-search-tree/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [99. Recover Binary Search Tree](../../0001-0500/0099-recover-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
