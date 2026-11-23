# LeetCode 2673: Make Costs of Paths Equal in a Binary Tree

**LeetCode Problem #2673 — Make Costs of Paths Equal in a Binary Tree**
Solve LeetCode Make Costs of Paths Equal in a Binary Tree using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Costs of Paths Equal in a Binary Tree |
| LeetCode | #2673 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer  n  representing the number of nodes in a  perfect binary tree  consisting of nodes numbered from  1  to  n . The root of the tree is node  1  and each node  i  in the tree has two children where the left child is the node  2 * i  and the right child is  2 * i + 1 .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Make Costs of Paths Equal in a Binary Tree**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3475-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)
- [257. Binary Tree Paths](../../0001-0500/0257-binary-tree-paths/)
- [1457. Pseudo-Palindromic Paths in a Binary Tree](../../1501-2000/1568-pseudo-palindromic-paths-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/)
