# LeetCode 1129: Shortest Path with Alternating Colors

**LeetCode Problem #1129 — Shortest Path with Alternating Colors**
Solve LeetCode Shortest Path with Alternating Colors using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path with Alternating Colors |
| LeetCode | #1129 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer  n , the number of nodes in a directed graph where the nodes are labeled from  0  to  n - 1 . Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Path with Alternating Colors**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [4003. Minimum Cost Path with Alternating Directions III](../../3501-4000/3926-minimum-cost-path-with-alternating-directions-iii/)
- [847. Shortest Path Visiting All Nodes](../../0501-1000/0877-shortest-path-visiting-all-nodes/)
- [864. Shortest Path to Get All Keys](../../0501-1000/0895-shortest-path-to-get-all-keys/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-with-alternating-colors/)
