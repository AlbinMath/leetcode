# LeetCode 3844: Longest Almost-Palindromic Substring

**LeetCode Problem #3844 — Longest Almost-Palindromic Substring**
Solve LeetCode Longest Almost-Palindromic Substring using Java and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Almost-Palindromic Substring |
| LeetCode | #3844 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an undirected tree with  n  nodes labeled from 1 to  n , rooted at node 1. The tree is represented by a 2D integer array  edges  of length  n - 1 , where  edges[i] = [u i , v i ]  indicates that there is an edge between nodes  u i   and  v i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Almost-Palindromic Substring**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [3842. Toggle Light Bulbs](../3842-number-of-ways-to-assign-edge-weights-ii/)
- [3275. K-th Nearest Obstacle Queries](../3275-minimum-number-of-pushes-to-type-word-i/)
- [3408. Design Task Manager](../3408-count-the-number-of-special-characters-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/)
