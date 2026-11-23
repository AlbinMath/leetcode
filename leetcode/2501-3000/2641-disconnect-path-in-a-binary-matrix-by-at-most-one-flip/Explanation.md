# LeetCode 2556: Disconnect Path in a Binary Matrix by at Most One Flip

**LeetCode Problem #2556 — Disconnect Path in a Binary Matrix by at Most One Flip**
Solve LeetCode Disconnect Path in a Binary Matrix by at Most One Flip using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Disconnect Path in a Binary Matrix by at Most One Flip |
| LeetCode | #2556 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed   m x n   binary  matrix  grid . You can move from a cell  (row, col)  to any of the cells  (row + 1, col)  or  (row, col + 1)  that has the value  1 . The matrix is  disconnected  if there is no path from  (0, 0)  to  (m - 1, n - 1) .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Disconnect Path in a Binary Matrix by at Most One Flip**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1091. Shortest Path in Binary Matrix](../../1001-1500/1171-shortest-path-in-binary-matrix/)
- [1784. Check if Binary String Has at Most One Segment of Ones](../../1501-2000/1910-check-if-binary-string-has-at-most-one-segment-of-ones/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)
