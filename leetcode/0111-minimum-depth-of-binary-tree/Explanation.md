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

## Problem
Given a binary tree, find its minimum depth.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Depth of Binary Tree**. Applying **Modified Binary Search** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [104. Maximum Depth of Binary Tree](../0104-maximum-depth-of-binary-tree/)
- [94. Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/)
- [108. Convert Sorted Array to Binary Search Tree](../0108-convert-sorted-array-to-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
