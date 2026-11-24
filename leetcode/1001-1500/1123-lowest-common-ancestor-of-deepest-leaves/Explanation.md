# LeetCode 1123: Lowest Common Ancestor of Deepest Leaves

**LeetCode Problem #1123 — Lowest Common Ancestor of Deepest Leaves**
Solve LeetCode Lowest Common Ancestor of Deepest Leaves using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lowest Common Ancestor of Deepest Leaves |
| LeetCode | #1123 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, return *the lowest common ancestor of its deepest leaves*.

Recall that:

The node of a binary tree is a leaf if and only if it has no children 
 The depth of the root of the tree is `0`. if the depth of a node is `d`, the depth of each of its children is `d + 1`. 
 The lowest common ancestor of a set `S` of nodes, is the node `A` with the largest depth such that every node in `S` is in the subtree with root `A`.

## Constraints
- The number of nodes in the tree will be in the range `[1, 1000]`.
- `0 <= Node.val <= 1000`
- The values of the nodes in the tree are **unique**.

## Examples
### Example 1
- **Input:** `root = [3,5,1,6,2,0,8,null,null,7,4]`
- **Output:** `[2,7,4]`
- **Explanation:** We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

### Example 2
- **Input:** `root = [1]`
- **Output:** `[1]`
- **Explanation:** The root is the deepest node in the tree, and it's the lca of itself.

### Example 3
- **Input:** `root = [0,1,3,null,2]`
- **Output:** `[2]`
- **Explanation:** The deepest leaf node in the tree is 2, the lca of one node is itself.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Lowest Common Ancestor of Deepest Leaves**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,5,1,6,2,0,8,null,null,7,4]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,7,4]`.
4. **Verification:** We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

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
var lcaDeepestLeaves = function(root) {
    function dfs(node) {
        if (node === null) {
            return [0, null];
        }

        const [leftDepth, leftNode] = dfs(node.left);
        const [rightDepth, rightNode] = dfs(node.right);

        if (leftDepth > rightDepth) {
            return [leftDepth + 1, leftNode];
        }

        if (rightDepth > leftDepth) {
            return [rightDepth + 1, rightNode];
        }

        return [leftDepth + 1, node];
    }

    return dfs(root)[1];
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
- [236. Lowest Common Ancestor of a Binary Tree](../../0001-0500/0236-lowest-common-ancestor-of-a-binary-tree/)
- [1302. Deepest Leaves Sum](../../1001-1500/1302-deepest-leaves-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)
