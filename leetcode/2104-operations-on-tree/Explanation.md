# LeetCode 1993: Operations on Tree

**LeetCode Problem #1993 — Operations on Tree**
Solve LeetCode Operations on Tree using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Operations on Tree |
| LeetCode | #1993 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a tree with  n  nodes numbered from  0  to  n - 1  in the form of a parent array  parent  where  parent[i]  is the parent of the  i th   node. The root of the tree is node  0 , so  parent[0] = -1  since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Operations on Tree**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../2558-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [1319. Number of Operations to Make Network Connected](../1442-number-of-operations-to-make-network-connected/)
- [1441. Build an Array With Stack Operations](../1552-build-an-array-with-stack-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/operations-on-tree/)
