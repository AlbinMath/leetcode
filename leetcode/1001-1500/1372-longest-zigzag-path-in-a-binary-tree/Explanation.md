# LeetCode 1372: Longest ZigZag Path in a Binary Tree

**LeetCode Problem #1372 — Longest ZigZag Path in a Binary Tree**
Solve LeetCode Longest ZigZag Path in a Binary Tree using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest ZigZag Path in a Binary Tree |
| LeetCode | #1372 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose **any **node in the binary tree and a direction (right or left). 
 If the current direction is right, move to the right child of the current node; otherwise, move to the left child. 
 Change the direction from right to left or from left to right. 
 Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return *the longest **ZigZag** path contained in that tree*.

## Constraints
- The number of nodes in the tree is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]`
- **Output:** `3`
- **Explanation:** Longest ZigZag path in blue nodes (right -> left -> right).

### Example 2
- **Input:** `root = [1,1,1,null,1,null,null,1,1,null,1]`
- **Output:** `4`
- **Explanation:** Longest ZigZag path in blue nodes (left -> right -> left -> right).

### Example 3
- **Input:** `root = [1]`
- **Output:** `0`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Longest ZigZag Path in a Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Longest ZigZag path in blue nodes (right -> left -> right).

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
var longestZigZag = function(root) {
    let maxLength = 0;

    function dfs(node, leftLength, rightLength) {
        if (node === null) {
            return;
        }

        maxLength = Math.max(maxLength, leftLength, rightLength);

        if (node.left) {
            dfs(node.left, rightLength + 1, 0);
        }

        if (node.right) {
            dfs(node.right, 0, leftLength + 1);
        }
    }

    dfs(root, 0, 0);

    return maxLength;
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
- [1104. Path In Zigzag Labelled Binary Tree](../../1001-1500/1104-path-in-zigzag-labelled-binary-tree/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [103. Binary Tree Zigzag Level Order Traversal](../../0001-0500/0103-binary-tree-zigzag-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)
