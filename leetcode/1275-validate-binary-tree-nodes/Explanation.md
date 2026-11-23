# LeetCode 1361: Validate Binary Tree Nodes

**LeetCode Problem #1361 — Validate Binary Tree Nodes**
Solve LeetCode Validate Binary Tree Nodes using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Validate Binary Tree Nodes |
| LeetCode | #1361 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have  n  binary tree nodes numbered from  0  to  n - 1  where node  i  has two children  leftChild[i]  and  rightChild[i] , return  true  if and only if  all  the given nodes form  exactly one  valid binary tree.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Validate Binary Tree Nodes**. Applying **Modified Binary Search** yields the target result step by step.

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
- [98. Validate Binary Search Tree](../0098-validate-binary-search-tree/)
- [863. All Nodes Distance K in Binary Tree](../0893-all-nodes-distance-k-in-binary-tree/)
- [1448. Count Good Nodes in Binary Tree](../1544-count-good-nodes-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/validate-binary-tree-nodes/)
