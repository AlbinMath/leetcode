# LeetCode 3986: Number of Elapsed Seconds Between Two Times

**LeetCode Problem #3986 — Number of Elapsed Seconds Between Two Times**
Solve LeetCode Number of Elapsed Seconds Between Two Times using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Elapsed Seconds Between Two Times |
| LeetCode | #3986 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  grid where each cell contains one of the values 0, 1, or 2. You are also given an integer  k .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Elapsed Seconds Between Two Times**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [2582. Pass the Pillow](../2582-minimum-score-of-a-path-between-two-cities/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../2914-find-the-safest-path-in-a-grid/)
- [3562. Maximum Profit from Trading Stocks with Discounts](../3562-maximum-score-of-non-overlapping-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-path-score-in-a-grid/)
