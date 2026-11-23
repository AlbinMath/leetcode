# LeetCode 3241: Time Taken to Mark All Nodes

**LeetCode Problem #3241 — Time Taken to Mark All Nodes**
Solve LeetCode Time Taken to Mark All Nodes using JavaScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Time Taken to Mark All Nodes |
| LeetCode | #3241 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There exists an  undirected  tree with  n  nodes numbered  0  to  n - 1 . You are given a 2D integer array  edges  of length  n - 1 , where  edges[i] = [u i , v i ]  indicates that there is an edge between nodes  u i   and  v i   in the tree.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Time Taken to Mark All Nodes**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [847. Shortest Path Visiting All Nodes](../0877-shortest-path-visiting-all-nodes/)
- [863. All Nodes Distance K in Binary Tree](../0893-all-nodes-distance-k-in-binary-tree/)
- [865. Smallest Subtree with all the Deepest Nodes](../0896-smallest-subtree-with-all-the-deepest-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/time-taken-to-mark-all-nodes/)
