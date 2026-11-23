# LeetCode 2713: Maximum Strictly Increasing Cells in a Matrix

**LeetCode Problem #2713 — Maximum Strictly Increasing Cells in a Matrix**
Solve LeetCode Maximum Strictly Increasing Cells in a Matrix using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Strictly Increasing Cells in a Matrix |
| LeetCode | #2713 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a  1-indexed   m x n  integer matrix  mat , you can select any cell in the matrix as your  starting cell .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Strictly Increasing Cells in a Matrix**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1909. Remove One Element to Make the Array Strictly Increasing](../../2001-2500/2020-remove-one-element-to-make-the-array-strictly-increasing/)
- [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](../../3001-3500/3372-longest-strictly-increasing-or-strictly-decreasing-subarray/)
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../../4001-4500/4032-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/)
