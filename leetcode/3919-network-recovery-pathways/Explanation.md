# LeetCode 3919: Minimum Cost to Move Between Indices

**LeetCode Problem #3919 — Minimum Cost to Move Between Indices**
Solve LeetCode Minimum Cost to Move Between Indices using PHP and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Move Between Indices |
| LeetCode | #3919 |
| Difficulty | Medium |
| Language | PHP |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a directed acyclic graph of  n  nodes numbered from 0 to  n &minus; 1 . This is represented by a 2D array  edges  of length   m  , where  edges[i] = [u i , v i , cost i ]  indicates a one‑way communication from node  u i   to node  v i   with a recovery cost of  cost i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost to Move Between Indices**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [3932. Count K-th Roots in a Range](../3932-find-covid-recovery-patients/)
- [909. Snakes and Ladders](../0909-stone-game/)
- [1182. Shortest Distance to Target Color](../1182-game-play-analysis-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/network-recovery-pathways/)
