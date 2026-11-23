# LeetCode 2045: Second Minimum Time to Reach Destination

**LeetCode Problem #2045 — Second Minimum Time to Reach Destination**
Solve LeetCode Second Minimum Time to Reach Destination using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Second Minimum Time to Reach Destination |
| LeetCode | #2045 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A city is represented as a  bi-directional connected  graph with  n  vertices where each vertex is labeled from  1  to  n  ( inclusive ). The edges in the graph are represented as a 2D integer array  edges , where each  edges[i] = [u i , v i ]  denotes a bi-directional edge between vertex  u i   and vertex  v i  . Every vertex pair is connected by  at most one  edge, and no vertex has an edge to itself. The time taken to traverse any edge is  time  minutes.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Second Minimum Time to Reach Destination**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1928. Minimum Cost to Reach Destination in Time](../../2001-2500/2040-minimum-cost-to-reach-destination-in-time/)
- [3604. Minimum Time to Reach Destination in Directed Graph](../../3501-4000/3916-minimum-time-to-reach-destination-in-directed-graph/)
- [3341. Find Minimum Time to Reach Last Room I](../../3501-4000/3627-find-minimum-time-to-reach-last-room-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/second-minimum-time-to-reach-destination/)
