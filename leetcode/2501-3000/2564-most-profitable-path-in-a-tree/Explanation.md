# LeetCode 2467: Most Profitable Path in a Tree

**LeetCode Problem #2467 — Most Profitable Path in a Tree**
Solve LeetCode Most Profitable Path in a Tree using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Profitable Path in a Tree |
| LeetCode | #2467 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an undirected tree with  n  nodes labeled from  0  to  n - 1 , rooted at node  0 . You are given a 2D integer array  edges  of length  n - 1  where  edges[i] = [a i , b i ]  indicates that there is an edge between nodes  a i   and  b i   in the tree.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Most Profitable Path in a Tree**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2556. Disconnect Path in a Binary Matrix by at Most One Flip](../../2501-3000/2641-disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)
- [3970. Shortest Path With At Most K Consecutive Identical Characters](../../4001-4500/4104-shortest-path-with-at-most-k-consecutive-identical-characters/)
- [4046. Minimum Cost Path With At Most K Turns](../../4001-4500/4367-minimum-cost-path-with-at-most-k-turns/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-profitable-path-in-a-tree/)
