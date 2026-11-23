# LeetCode 3123: Find Edges in Shortest Paths

**LeetCode Problem #3123 — Find Edges in Shortest Paths**
Solve LeetCode Find Edges in Shortest Paths using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Edges in Shortest Paths |
| LeetCode | #3123 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an undirected weighted graph of  n  nodes numbered from 0 to  n - 1 . The graph consists of  m  edges represented by a 2D array  edges , where  edges[i] = [a i , b i , w i ]  indicates that there is an edge between nodes  a i   and  b i   with weight  w i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Edges in Shortest Paths**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [943. Find the Shortest Superstring](../../0501-1000/0980-find-the-shortest-superstring/)
- [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](../../1501-2000/1613-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
- [62. Unique Paths](../../0001-0500/0062-unique-paths/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-edges-in-shortest-paths/)
