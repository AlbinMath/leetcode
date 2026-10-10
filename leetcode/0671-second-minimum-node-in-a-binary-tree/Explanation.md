# LeetCode 671: Second Minimum Node In a Binary Tree

**LeetCode Problem #671 — Second Minimum Node In a Binary Tree**
Solve LeetCode Second Minimum Node In a Binary Tree using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Second Minimum Node In a Binary Tree |
| LeetCode | #671 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly  two  or  zero  sub-node. If the node has two sub-nodes, then this node&#39;s value is the smaller value among its two sub-nodes. More formally, the property  root.val = min(root.left.val, root.right.val)  always holds.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Second Minimum Node In a Binary Tree**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Linked List**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [111. Minimum Depth of Binary Tree](../0111-minimum-depth-of-binary-tree/)
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../1498-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [94. Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/)
