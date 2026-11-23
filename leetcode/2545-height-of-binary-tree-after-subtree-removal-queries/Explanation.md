# LeetCode 2458: Height of Binary Tree After Subtree Removal Queries

**LeetCode Problem #2458 — Height of Binary Tree After Subtree Removal Queries**
Solve LeetCode Height of Binary Tree After Subtree Removal Queries using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Height of Binary Tree After Subtree Removal Queries |
| LeetCode | #2458 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given the  root  of a  binary tree  with  n  nodes. Each node is assigned a unique value from  1  to  n . You are also given an array  queries  of size  m .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Height of Binary Tree After Subtree Removal Queries**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3319. K-th Largest Perfect Subtree Size in Binary Tree](../3509-k-th-largest-perfect-subtree-size-in-binary-tree/)
- [2476. Closest Nodes Queries in a Binary Search Tree](../2567-closest-nodes-queries-in-a-binary-search-tree/)
- [572. Subtree of Another Tree](../0572-subtree-of-another-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/)
