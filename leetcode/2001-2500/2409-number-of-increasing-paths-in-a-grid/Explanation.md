# LeetCode 2328: Number of Increasing Paths in a Grid

**LeetCode Problem #2328 — Number of Increasing Paths in a Grid**
Solve LeetCode Number of Increasing Paths in a Grid using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Increasing Paths in a Grid |
| LeetCode | #2328 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  integer matrix  grid , where you can move from a cell to any adjacent cell in all  4  directions.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Increasing Paths in a Grid**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [673. Number of Longest Increasing Subsequence](../../0501-1000/0673-number-of-longest-increasing-subsequence/)
- [1301. Number of Paths with Max Score](../../1001-1500/1234-number-of-paths-with-max-score/)
- [1786. Number of Restricted Paths From First to Last Node](../../1501-2000/1912-number-of-restricted-paths-from-first-to-last-node/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/)
