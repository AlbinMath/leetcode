# LeetCode 3820: Pythagorean Distance Nodes in a Tree

**LeetCode Problem #3820 — Pythagorean Distance Nodes in a Tree**
Solve LeetCode Pythagorean Distance Nodes in a Tree using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pythagorean Distance Nodes in a Tree |
| LeetCode | #3820 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n  and an undirected tree with  n  nodes numbered from 0 to  n - 1 . The tree is represented by a 2D array  edges  of length  n - 1 , where  edges[i] = [u i , v i ]  indicates an undirected edge between  u i   and  v i  .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Pythagorean Distance Nodes in a Tree**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [863. All Nodes Distance K in Binary Tree](../0893-all-nodes-distance-k-in-binary-tree/)
- [783. Minimum Distance Between BST Nodes](../0799-minimum-distance-between-bst-nodes/)
- [222. Count Complete Tree Nodes](../0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/)
