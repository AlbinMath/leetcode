# LeetCode 114: Flatten Binary Tree to Linked List

**LeetCode Problem #114 — Flatten Binary Tree to Linked List**
Solve LeetCode Flatten Binary Tree to Linked List using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Flatten Binary Tree to Linked List |
| LeetCode | #114 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`. 
 The "linked list" should be in the same order as a **pre-order**** traversal** of the binary tree.

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,2,5,3,4,null,6]`
- **Output:** `[1,null,2,null,3,null,4,null,5,null,6]`

### Example 2
- **Input:** `root = []`
- **Output:** `[]`

### Example 3
- **Input:** `root = [0]`
- **Output:** `[0]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Flatten Binary Tree to Linked List**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,5,3,4,null,6]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,null,2,null,3,null,4,null,5,null,6]`.

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
var flatten = function(root) {
    let current = root;

    while (current !== null) {
        if (current.left !== null) {
            // Find the rightmost node of the left subtree
            let predecessor = current.left;

            while (predecessor.right !== null) {
                predecessor = predecessor.right;
            }

            // Connect the original right subtree
            // to the rightmost node of the left subtree
            predecessor.right = current.right;

            // Move the left subtree to the right
            current.right = current.left;
            current.left = null;
        }

        // Move to the next node
        current = current.right;
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
- [1367. Linked List in Binary Tree](../../1001-1500/1367-linked-list-in-binary-tree/)
- [109. Convert Sorted List to Binary Search Tree](../../0001-0500/0109-convert-sorted-list-to-binary-search-tree/)
- [1290. Convert Binary Number in a Linked List to Integer](../../1001-1500/1290-convert-binary-number-in-a-linked-list-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
