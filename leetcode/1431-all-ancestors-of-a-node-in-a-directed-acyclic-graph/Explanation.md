# LeetCode 2192: All Ancestors of a Node in a Directed Acyclic Graph

**LeetCode Problem #2192 — All Ancestors of a Node in a Directed Acyclic Graph**
Solve LeetCode All Ancestors of a Node in a Directed Acyclic Graph using JavaScript and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Ancestors of a Node in a Directed Acyclic Graph |
| LeetCode | #2192 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given a positive integer  n  representing the number of nodes of a  Directed Acyclic Graph  (DAG). The nodes are numbered from  0  to  n - 1  ( inclusive ).

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **All Ancestors of a Node in a Directed Acyclic Graph**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [1857. Largest Color Value in a Directed Graph](../1986-largest-color-value-in-a-directed-graph/)
- [2876. Count Visited Nodes in a Directed Graph](../3140-count-visited-nodes-in-a-directed-graph/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../3916-minimum-time-to-reach-destination-in-directed-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)
