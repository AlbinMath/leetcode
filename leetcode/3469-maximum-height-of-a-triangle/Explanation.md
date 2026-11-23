# LeetCode 3200: Maximum Height of a Triangle

**LeetCode Problem #3200 — Maximum Height of a Triangle**
Solve LeetCode Maximum Height of a Triangle using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Height of a Triangle |
| LeetCode | #3200 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two integers  red  and  blue  representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1 st  row will have 1 ball, the 2 nd  row will have 2 balls, the 3 rd  row will have 3 balls, and so on.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Mathematical Simulation & Modular Arithmetic**. By maintaining state efficiently in a **Primitive Types**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Height of a Triangle**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3588. Find Maximum Area of a Triangle](../3868-find-maximum-area-of-a-triangle/)
- [1840. Maximum Building Height](../1968-maximum-building-height/)
- [118. Pascal's Triangle](../0118-pascals-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-height-of-a-triangle/)
