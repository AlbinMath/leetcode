# LeetCode 2316: Count Unreachable Pairs of Nodes in an Undirected Graph

**LeetCode Problem #2316 — Count Unreachable Pairs of Nodes in an Undirected Graph**
Solve LeetCode Count Unreachable Pairs of Nodes in an Undirected Graph using Python and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unreachable Pairs of Nodes in an Undirected Graph |
| LeetCode | #2316 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an integer  n . There is an  undirected  graph with  n  nodes, numbered from  0  to  n - 1 . You are given a 2D integer array  edges  where  edges[i] = [a i , b i ]  denotes that there exists an  undirected  edge connecting nodes  a i   and  b i  .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Pointer Traversal & Node Manipulation**. By maintaining state efficiently in a **Linked List**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Unreachable Pairs of Nodes in an Undirected Graph**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

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
- [1782. Count Pairs Of Nodes](../1891-count-pairs-of-nodes/)
- [2876. Count Visited Nodes in a Directed Graph](../3140-count-visited-nodes-in-a-directed-graph/)
- [222. Count Complete Tree Nodes](../0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
