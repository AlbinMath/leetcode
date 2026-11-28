# LeetCode 236: Lowest Common Ancestor of a Binary Tree

**LeetCode Problem #236 — Lowest Common Ancestor of a Binary Tree**
Solve LeetCode Lowest Common Ancestor of a Binary Tree using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lowest Common Ancestor of a Binary Tree |
| LeetCode | #236 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia : &ldquo;The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself ).&rdquo;

## Constraints
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

## Examples
### Example 1
- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
- **Output:** `3`
- **Explanation:** The LCA of nodes 5 and 1 is 3.

### Example 2
- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
- **Output:** `5`
- **Explanation:** The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

### Example 3
- **Input:** `root = [1,2], p = 1, q = 2`
- **Output:** `1`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Lowest Common Ancestor of a Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The LCA of nodes 5 and 1 is 3.

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
var lowestCommonAncestor = function(root, p, q) {
    // Base case: empty node or either target found.
    if (root === null || root === p || root === q) {
        return root;
    }

    // Search for p and q in both subtrees.
    const left = lowestCommonAncestor(root.left, p, q);
    const right = lowestCommonAncestor(root.right, p, q);

    // Targets found in separate subtrees.
    if (left !== null && right !== null) {
        return root;
    }

    // Otherwise, return whichever subtree found a target.
    return left !== null ? left : right;
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
- [235. Lowest Common Ancestor of a Binary Search Tree](../../0001-0500/0235-lowest-common-ancestor-of-a-binary-search-tree/)
- [1123. Lowest Common Ancestor of Deepest Leaves](../../1001-1500/1123-lowest-common-ancestor-of-deepest-leaves/)
- [1483. Kth Ancestor of a Tree Node](../../1001-1500/1483-kth-ancestor-of-a-tree-node/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
