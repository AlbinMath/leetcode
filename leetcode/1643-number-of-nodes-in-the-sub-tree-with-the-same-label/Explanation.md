# LeetCode 1519: Number of Nodes in the Sub-Tree With the Same Label

**LeetCode Problem #1519 — Number of Nodes in the Sub-Tree With the Same Label**
Solve LeetCode Number of Nodes in the Sub-Tree With the Same Label using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Nodes in the Sub-Tree With the Same Label |
| LeetCode | #1519 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of  n  nodes numbered from  0  to  n - 1  and exactly  n - 1   edges . The  root  of the tree is the node  0 , and each node of the tree has  a label  which is a lower-case character given in the string  labels  (i.e. The node with the number  i  has the label  labels[i] ).

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Nodes in the Sub-Tree With the Same Label**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [100. Same Tree](../0100-same-tree/)
- [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](../1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../1692-number-of-ways-to-reorder-array-to-get-same-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)
