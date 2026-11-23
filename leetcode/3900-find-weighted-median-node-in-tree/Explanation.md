# LeetCode 3585: Find Weighted Median Node in Tree

**LeetCode Problem #3585 — Find Weighted Median Node in Tree**
Solve LeetCode Find Weighted Median Node in Tree using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Weighted Median Node in Tree |
| LeetCode | #3585 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n  and an  undirected, weighted  tree rooted at node 0 with  n  nodes numbered from 0 to  n - 1 . This is represented by a 2D array  edges  of length  n - 1 , where  edges[i] = [u i , v i , w i ]  indicates an edge from node  u i   to  v i   with weight  w i  .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Weighted Median Node in Tree**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../1498-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [3515. Shortest Path in a Weighted Tree](../3829-shortest-path-in-a-weighted-tree/)
- [501. Find Mode in Binary Search Tree](../0501-find-mode-in-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-weighted-median-node-in-tree/)
