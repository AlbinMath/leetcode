# LeetCode 99: Recover Binary Search Tree

**LeetCode Problem #99 — Recover Binary Search Tree**
Solve LeetCode Recover Binary Search Tree using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Recover Binary Search Tree |
| LeetCode | #99 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a binary search tree (BST), where the values of **exactly** two nodes of the tree were swapped by mistake. *Recover the tree without changing its structure*.

## Constraints
- The number of nodes in the tree is in the range `[2, 1000]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `root = [1,3,null,null,2]`
- **Output:** `[3,1,null,null,2]`
- **Explanation:** 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

### Example 2
- **Input:** `root = [3,1,4,null,null,2]`
- **Output:** `[2,1,4,null,null,3]`
- **Explanation:** 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Recover Binary Search Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,3,null,null,2]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1,null,null,2]`.
4. **Verification:** 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var recoverTree = function(root) {
    let first = null;
    let second = null;
    let prev = null;
    let curr = root;

    // Morris inorder traversal: O(1) extra space
    while (curr !== null) {
        if (curr.left === null) {
            // Visit current node
            if (prev !== null && prev.val > curr.val) {
                if (first === null) {
                    first = prev;
                }
                second = curr;
            }

            prev = curr;
            curr = curr.right;
        } else {
            // Find inorder predecessor
            let pred = curr.left;

            while (pred.right !== null && pred.right !== curr) {
                pred = pred.right;
            }

            if (pred.right === null) {
                // Create temporary thread
                pred.right = curr;
                curr = curr.left;
            } else {
                // Remove temporary thread
                pred.right = null;

                // Visit current node
                if (prev !== null && prev.val > curr.val) {
                    if (first === null) {
                        first = prev;
                    }
                    second = curr;
                }

                prev = curr;
                curr = curr.right;
            }
        }
    }

    // Restore the two swapped values
    if (first !== null && second !== null) {
        [first.val, second.val] = [second.val, first.val];
    }
};
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
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [108. Convert Sorted Array to Binary Search Tree](../../0001-0500/0108-convert-sorted-array-to-binary-search-tree/)
- [109. Convert Sorted List to Binary Search Tree](../../0001-0500/0109-convert-sorted-list-to-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/recover-binary-search-tree/)
