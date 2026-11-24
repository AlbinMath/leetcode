# LeetCode 100: Same Tree

**LeetCode Problem #100 — Same Tree**
Solve LeetCode Same Tree using PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Same Tree |
| LeetCode | #100 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Constraints
- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Examples
### Example 1
- **Input:** `p = [1,2,3], q = [1,2,3]`
- **Output:** `true`

### Example 2
- **Input:** `p = [1,2], q = [1,null,2]`
- **Output:** `false`

### Example 3
- **Input:** `p = [1,2,1], q = [1,1,2]`
- **Output:** `false`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Same Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `p = [1,2,3], q = [1,2,3]`.
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
    function isSameTree($p, $q) {

        // Both nodes are empty
        if ($p === null && $q === null) {
            return true;
        }

        // One is empty, the other is not
        if ($p === null || $q === null) {
            return false;
        }

        // Values are different
        if ($p->val != $q->val) {
            return false;
        }

        // Check left and right subtrees
        return $this->isSameTree($p->left, $q->left)
            && $this->isSameTree($p->right, $q->right);
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
- [1519. Number of Nodes in the Sub-Tree With the Same Label](../../1501-2000/1643-number-of-nodes-in-the-sub-tree-with-the-same-label/)
- [805. Split Array With Same Average](../../0501-1000/0823-split-array-with-same-average/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0984-most-stones-removed-with-same-row-or-column/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/same-tree/)
