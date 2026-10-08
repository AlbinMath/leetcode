# LeetCode 2196: Create Binary Tree From Descriptions

**LeetCode Problem #2196 — Create Binary Tree From Descriptions**
Solve LeetCode Create Binary Tree From Descriptions using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Binary Tree From Descriptions |
| LeetCode | #2196 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a 2D integer array  descriptions  where  descriptions[i] = [parent i , child i , isLeft i ]  indicates that  parent i   is the  parent  of  child i   in a  binary  tree of  unique  values. Furthermore,

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. Create all nodes in a hash map (value → TreeNode).
2. Process each description: link parent to child as left or right child. Track which nodes are children.
3. The root is the only node that never appears as a child.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Create Binary Tree From Descriptions**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)

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
- [94. Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/)
- [104. Maximum Depth of Binary Tree](../0104-maximum-depth-of-binary-tree/)
- [108. Convert Sorted Array to Binary Search Tree](../0108-convert-sorted-array-to-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions/)
