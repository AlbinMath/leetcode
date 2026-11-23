# LeetCode 2577: Minimum Time to Visit a Cell In a Grid

**LeetCode Problem #2577 — Minimum Time to Visit a Cell In a Grid**
Solve LeetCode Minimum Time to Visit a Cell In a Grid using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Visit a Cell In a Grid |
| LeetCode | #2577 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  m x n  matrix  grid  consisting of  non-negative  integers where  grid[row][col]  represents the  minimum  time required to be able to visit the cell  (row, col) , which means you can visit the cell  (row, col)  only when the time you visit it is greater than or equal to  grid[row][col] .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Time to Visit a Cell In a Grid**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3112. Minimum Time to Visit Disappearing Nodes](../3389-minimum-time-to-visit-disappearing-nodes/)
- [539. Minimum Time Difference](../0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../1395-minimum-time-visiting-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/)
