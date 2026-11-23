# LeetCode 3112: Minimum Time to Visit Disappearing Nodes

**LeetCode Problem #3112 — Minimum Time to Visit Disappearing Nodes**
Solve LeetCode Minimum Time to Visit Disappearing Nodes using JavaScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Visit Disappearing Nodes |
| LeetCode | #3112 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an undirected graph of  n  nodes. You are given a 2D array  edges , where  edges[i] = [u i , v i , length i ]  describes an edge between node  u i   and node  v i   with a traversal time of  length i   units.

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Time to Visit Disappearing Nodes**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [2577. Minimum Time to Visit a Cell In a Grid](../2711-minimum-time-to-visit-a-cell-in-a-grid/)
- [539. Minimum Time Difference](../0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../1395-minimum-time-visiting-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/)
