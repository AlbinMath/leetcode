# LeetCode 111: Minimum Depth of Binary Tree

**LeetCode Problem #111 — Minimum Depth of Binary Tree**
Solve LeetCode Minimum Depth of Binary Tree using PHP and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Depth of Binary Tree |
| LeetCode | #111 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^5]`.
- `-1000 <= Node.val <= 1000`

## Examples
### Example 1
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `2`

### Example 2
- **Input:** `root = [2,null,3,null,4,null,5,null,6]`
- **Output:** `5`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Depth of Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

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
3. **Result:** Arrive at the expected output `2`.

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
    function minDepth($root) {
        if ($root === null) {
            return 0;
        }

        $queue = [$root];
        $front = 0;
        $depth = 1;

        while ($front < count($queue)) {
            $levelSize = count($queue) - $front;

            for ($i = 0; $i < $levelSize; $i++) {
                $node = $queue[$front++];

                // First leaf found = minimum depth
                if ($node->left === null && $node->right === null) {
                    return $depth;
                }

                if ($node->left !== null) {
                    $queue[] = $node->left;
                }

                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }

            $depth++;
        }

        return $depth;
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
- [671. Second Minimum Node In a Binary Tree](../../0501-1000/0671-second-minimum-node-in-a-binary-tree/)
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2001-2500/2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
