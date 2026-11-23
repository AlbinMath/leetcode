# LeetCode 2257: Count Unguarded Cells in the Grid

**LeetCode Problem #2257 — Count Unguarded Cells in the Grid**
Solve LeetCode Count Unguarded Cells in the Grid using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Unguarded Cells in the Grid |
| LeetCode | #2257 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two integers  m  and  n  representing a  0-indexed   m x n  grid. You are also given two 2D integer arrays  guards  and  walls  where  guards[i] = [row i , col i ]  and  walls[j] = [row j , col j ]  represent the positions of the  i th   guard and  j th   wall respectively.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Unguarded Cells in the Grid**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3529. Count Cells in Overlapping Horizontal and Vertical Substrings](../../3501-4000/3821-count-cells-in-overlapping-horizontal-and-vertical-substrings/)
- [2617. Minimum Number of Visited Cells in a Grid](../../2501-3000/2697-minimum-number-of-visited-cells-in-a-grid/)
- [3276. Select Cells in Grid With Maximum Score](../../3501-4000/3563-select-cells-in-grid-with-maximum-score/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)
