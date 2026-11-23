# LeetCode 1192: Critical Connections in a Network

**LeetCode Problem #1192 — Critical Connections in a Network**
Solve LeetCode Critical Connections in a Network using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Critical Connections in a Network |
| LeetCode | #1192 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are  n  servers numbered from  0  to  n - 1  connected by undirected server-to-server  connections  forming a network where  connections[i] = [a i , b i ]  represents a connection between servers  a i   and  b i  . Any server can reach other servers directly or indirectly through the network.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Critical Connections in a Network**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [743. Network Delay Time](../../0501-1000/0744-network-delay-time/)
- [1319. Number of Operations to Make Network Connected](../../1001-1500/1442-number-of-operations-to-make-network-connected/)
- [1615. Maximal Network Rank](../../1501-2000/1738-maximal-network-rank/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/)
