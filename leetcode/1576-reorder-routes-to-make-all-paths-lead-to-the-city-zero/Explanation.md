# LeetCode 1466: Reorder Routes to Make All Paths Lead to the City Zero

**LeetCode Problem #1466 — Reorder Routes to Make All Paths Lead to the City Zero**
Solve LeetCode Reorder Routes to Make All Paths Lead to the City Zero using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reorder Routes to Make All Paths Lead to the City Zero |
| LeetCode | #1466 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are  n  cities numbered from  0  to  n - 1  and  n - 1  roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reorder Routes to Make All Paths Lead to the City Zero**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1897. Redistribute Characters to Make All Strings Equal](../2025-redistribute-characters-to-make-all-strings-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2749. Minimum Operations to Make the Integer Zero](../2837-minimum-operations-to-make-the-integer-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)
