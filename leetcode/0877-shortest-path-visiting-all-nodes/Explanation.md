# LeetCode 847: Shortest Path Visiting All Nodes

**LeetCode Problem #847 — Shortest Path Visiting All Nodes**
Solve LeetCode Shortest Path Visiting All Nodes using JavaScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path Visiting All Nodes |
| LeetCode | #847 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have an undirected, connected graph of  n  nodes labeled from  0  to  n - 1 . You are given an array  graph  where  graph[i]  is a list of all the nodes connected with node  i  by an edge.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Path Visiting All Nodes**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [864. Shortest Path to Get All Keys](../0895-shortest-path-to-get-all-keys/)
- [1091. Shortest Path in Binary Matrix](../1171-shortest-path-in-binary-matrix/)
- [1129. Shortest Path with Alternating Colors](../1229-shortest-path-with-alternating-colors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
