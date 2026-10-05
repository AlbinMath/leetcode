# LeetCode 2492: Minimum Score of a Path Between Two Cities

**LeetCode Problem #2492 — Minimum Score of a Path Between Two Cities**
Solve LeetCode Minimum Score of a Path Between Two Cities using Java and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Score of a Path Between Two Cities |
| LeetCode | #2492 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a positive integer  n  representing  n  cities numbered from  1  to  n . You are also given a  2D  array  roads  where  roads[i] = [a i , b i , distance i ]  indicates that there is a  bidirectional  road between cities  a i   and  b i   with a distance equal to  distance i  . The cities graph is not necessarily connected.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Since you can traverse any edge multiple times, the answer is the minimum edge weight in the connected component containing cities 1 and n. Use **BFS/DFS** or **Union-Find** to find all reachable nodes from city 1 and track the minimum edge weight.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Score of a Path Between Two Cities**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [3742. Maximum Path Score in a Grid](../3986-maximum-path-score-in-a-grid/)
- [1. Two Sum](../0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)
