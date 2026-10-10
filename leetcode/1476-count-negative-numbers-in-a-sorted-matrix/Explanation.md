# LeetCode 1351: Count Negative Numbers in a Sorted Matrix

**LeetCode Problem #1351 — Count Negative Numbers in a Sorted Matrix**
Solve LeetCode Count Negative Numbers in a Sorted Matrix using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Negative Numbers in a Sorted Matrix |
| LeetCode | #1351 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a  m x n  matrix  grid  which is sorted in non-increasing order both row-wise and column-wise, return  the number of  negative  numbers in   grid .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Negative Numbers in a Sorted Matrix**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1380. Lucky Numbers in a Matrix](../1496-lucky-numbers-in-a-matrix/)
- [1523. Count Odd Numbers in an Interval Range](../1630-count-odd-numbers-in-an-interval-range/)
- [2. Add Two Numbers](../0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
