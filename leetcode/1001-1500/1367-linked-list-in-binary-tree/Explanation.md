# LeetCode 1367: Linked List in Binary Tree

**LeetCode Problem #1367 — Linked List in Binary Tree**
Solve LeetCode Linked List in Binary Tree using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Linked List in Binary Tree |
| LeetCode | #1367 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary tree `root` and a linked list with `head` as the first node.

Return True if all the elements in the linked list starting from the `head` correspond to some *downward path* connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

## Constraints
- The number of nodes in the tree will be in the range `[1, 2500]`.
- The number of nodes in the list will be in the range `[1, 100]`.
- `1 <= Node.val <= 100` for each node in the linked list and binary tree.

## Examples
### Example 1
- **Input:** `head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
- **Output:** `true`
- **Explanation:** Nodes in blue form a subpath in the binary Tree.

### Example 2
- **Input:** `head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
- **Output:** `true`

### Example 3
- **Input:** `head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`
- **Output:** `false`
- **Explanation:** There is no path in the binary tree that contains all the elements of the linked list from `head`.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Linked List in Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Nodes in blue form a subpath in the binary Tree.

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
var isSubPath = function(head, root) {

    // Check whether the linked list matches
    // a downward path starting at this tree node
    function dfs(head, root) {
        if (!head) return true;

        if (!root) return false;

        if (head.val !== root.val) {
            return false;
        }

        return (
            dfs(head.next, root.left) ||
            dfs(head.next, root.right)
        );
    }

    // Try starting the linked list from every tree node
    function search(root) {
        if (!root) return false;

        return (
            dfs(head, root) ||
            search(root.left) ||
            search(root.right)
        );
    }

    return search(root);
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
- [114. Flatten Binary Tree to Linked List](../../0001-0500/0114-flatten-binary-tree-to-linked-list/)
- [1290. Convert Binary Number in a Linked List to Integer](../../1001-1500/1290-convert-binary-number-in-a-linked-list-to-integer/)
- [109. Convert Sorted List to Binary Search Tree](../../0001-0500/0109-convert-sorted-list-to-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/linked-list-in-binary-tree/)
