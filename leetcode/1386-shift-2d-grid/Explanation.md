# LeetCode 1260: Shift 2D Grid

**LeetCode Problem #1260 — Shift 2D Grid**
Solve LeetCode Shift 2D Grid using Racket and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shift 2D Grid |
| LeetCode | #1260 |
| Difficulty | Easy |
| Language | Racket |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a 2D  grid  of size  m x n  and an integer  k . You need to shift the  grid   k  times.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code (in Racket) uses a **flatten-shift-reshape** approach:
1. **Flatten:** Convert the 2D grid into a 1D list.
2. **Shift:** Compute `shift = k % total` to avoid redundant full rotations. Split the flat list at `total - shift` and swap the two halves (move the last `shift` elements to the front).
3. **Reshape:** Convert the shifted 1D list back into a 2D grid with `m` rows and `n` columns.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shift 2D Grid**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
Racket

## Source Code
- [solution.rkt](./solution.rkt)

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
- [74. Search a 2D Matrix](../0074-search-a-2d-matrix/)
- [1914. Cyclically Rotating a Grid](../2043-cyclically-rotating-a-grid/)
- [2812. Find the Safest Path in a Grid](../2914-find-the-safest-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shift-2d-grid/)
