# LeetCode 863: All Nodes Distance K in Binary Tree

**LeetCode Problem #863 — All Nodes Distance K in Binary Tree**
Solve LeetCode All Nodes Distance K in Binary Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Nodes Distance K in Binary Tree |
| LeetCode | #863 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given the  root  of a binary tree, the value of a target node  target , and an integer  k , return  an array of the values of all nodes that have a distance   k   from the target node.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **All Nodes Distance K in Binary Tree**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1361. Validate Binary Tree Nodes](../../1001-1500/1275-validate-binary-tree-nodes/)
- [1448. Count Good Nodes in Binary Tree](../../1501-2000/1544-count-good-nodes-in-binary-tree/)
- [2476. Closest Nodes Queries in a Binary Search Tree](../../2501-3000/2567-closest-nodes-queries-in-a-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
