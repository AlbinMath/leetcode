# LeetCode 882: Reachable Nodes In Subdivided Graph

**LeetCode Problem #882 — Reachable Nodes In Subdivided Graph**
Solve LeetCode Reachable Nodes In Subdivided Graph using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reachable Nodes In Subdivided Graph |
| LeetCode | #882 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an undirected graph (the  "original graph" ) with  n  nodes labeled from  0  to  n - 1 . You decide to  subdivide  each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reachable Nodes In Subdivided Graph**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [24. Swap Nodes in Pairs](../0024-swap-nodes-in-pairs/)
- [25. Reverse Nodes in k-Group](../0025-reverse-nodes-in-k-group/)
- [133. Clone Graph](../0133-clone-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)
