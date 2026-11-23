# LeetCode 2642: Design Graph With Shortest Path Calculator

**LeetCode Problem #2642 — Design Graph With Shortest Path Calculator**
Solve LeetCode Design Graph With Shortest Path Calculator using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Graph With Shortest Path Calculator |
| LeetCode | #2642 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is a  directed weighted  graph that consists of  n  nodes numbered from  0  to  n - 1 . The edges of the graph are initially represented by the given array  edges  where  edges[i] = [from i , to i , edgeCost i ]  meaning that there is an edge from  from i   to  to i   with the cost  edgeCost i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Design Graph With Shortest Path Calculator**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0877-shortest-path-visiting-all-nodes/)
- [864. Shortest Path to Get All Keys](../../0501-1000/0895-shortest-path-to-get-all-keys/)
- [1091. Shortest Path in Binary Matrix](../../1001-1500/1171-shortest-path-in-binary-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-graph-with-shortest-path-calculator/)
