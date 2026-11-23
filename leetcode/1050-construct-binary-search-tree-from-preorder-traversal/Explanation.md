# LeetCode 1008: Construct Binary Search Tree from Preorder Traversal

**LeetCode Problem #1008 — Construct Binary Search Tree from Preorder Traversal**
Solve LeetCode Construct Binary Search Tree from Preorder Traversal using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Binary Search Tree from Preorder Traversal |
| LeetCode | #1008 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of integers preorder, which represents the  preorder traversal  of a BST (i.e.,  binary search tree ), construct the tree and return  its root .

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Modified Binary Search**. By maintaining state efficiently in a **Sorted Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Construct Binary Search Tree from Preorder Traversal**. Applying **Modified Binary Search** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [105. Construct Binary Tree from Preorder and Inorder Traversal](../0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [889. Construct Binary Tree from Preorder and Postorder Traversal](../0925-construct-binary-tree-from-preorder-and-postorder-traversal/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](../0106-construct-binary-tree-from-inorder-and-postorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)
