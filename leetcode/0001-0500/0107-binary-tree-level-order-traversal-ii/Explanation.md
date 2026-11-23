# LeetCode 107: Binary Tree Level Order Traversal II

**LeetCode Problem #107 — Binary Tree Level Order Traversal II**
Solve LeetCode Binary Tree Level Order Traversal II using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Tree Level Order Traversal II |
| LeetCode | #107 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the  root  of a binary tree, return  the bottom-up level order traversal of its nodes&#39; values . (i.e., from left to right, level by level from leaf to root).

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Binary Tree Level Order Traversal II**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [102. Binary Tree Level Order Traversal](../../0001-0500/0102-binary-tree-level-order-traversal/)
- [103. Binary Tree Zigzag Level Order Traversal](../../0001-0500/0103-binary-tree-zigzag-level-order-traversal/)
- [429. N-ary Tree Level Order Traversal](../../0501-1000/0764-n-ary-tree-level-order-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
