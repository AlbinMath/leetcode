# LeetCode 1253: Reconstruct a 2-Row Binary Matrix

**LeetCode Problem #1253 — Reconstruct a 2-Row Binary Matrix**
Solve LeetCode Reconstruct a 2-Row Binary Matrix using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reconstruct a 2-Row Binary Matrix |
| LeetCode | #1253 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given the following details of a matrix with  n  columns and  2  rows :

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reconstruct a 2-Row Binary Matrix**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1091. Shortest Path in Binary Matrix](../1171-shortest-path-in-binary-matrix/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../1409-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1582. Special Positions in a Binary Matrix](../1704-special-positions-in-a-binary-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/)
