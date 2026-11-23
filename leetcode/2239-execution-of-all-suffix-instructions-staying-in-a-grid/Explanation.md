# LeetCode 2120: Execution of All Suffix Instructions Staying in a Grid

**LeetCode Problem #2120 — Execution of All Suffix Instructions Staying in a Grid**
Solve LeetCode Execution of All Suffix Instructions Staying in a Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Execution of All Suffix Instructions Staying in a Grid |
| LeetCode | #2120 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an  n x n  grid, with the top-left cell at  (0, 0)  and the bottom-right cell at  (n - 1, n - 1) . You are given the integer  n  and an integer array  startPos  where  startPos = [start row , start col ]  indicates that a robot is initially at cell  (start row , start col ) .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Execution of All Suffix Instructions Staying in a Grid**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1643. Kth Smallest Instructions](../0489-kth-smallest-instructions/)
- [1649. Create Sorted Array through Instructions](../1772-create-sorted-array-through-instructions/)
- [3522. Calculate Score After Performing Instructions](../3732-calculate-score-after-performing-instructions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/)
