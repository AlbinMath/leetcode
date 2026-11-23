# LeetCode 1489: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

**LeetCode Problem #1489 — Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree**
Solve LeetCode Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree |
| LeetCode | #1489 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a weighted undirected connected graph with  n  vertices numbered from  0  to  n - 1 , and an array  edges  where  edges[i] = [a i , b i , weight i ]  represents a bidirectional and weighted edge between nodes  a i   and  b i  . A minimum spanning tree (MST) is a subset of the graph&#39;s edges that connects all vertices without cycles and with the minimum possible total edge weight.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [3123. Find Edges in Shortest Paths](../3386-find-edges-in-shortest-paths/)
- [3924. Minimum Threshold Path With Limited Heavy Edges](../4102-minimum-threshold-path-with-limited-heavy-edges/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
