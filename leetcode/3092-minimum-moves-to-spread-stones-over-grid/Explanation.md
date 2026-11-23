# LeetCode 2850: Minimum Moves to Spread Stones Over Grid

**LeetCode Problem #2850 — Minimum Moves to Spread Stones Over Grid**
Solve LeetCode Minimum Moves to Spread Stones Over Grid using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Spread Stones Over Grid |
| LeetCode | #2850 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  2D integer matrix  grid  of size  3 * 3 , representing the number of stones in each cell. The grid contains exactly  9  stones, and there can be  multiple  stones in a single cell.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Moves to Spread Stones Over Grid**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [453. Minimum Moves to Equal Array Elements](../0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../0462-minimum-moves-to-equal-array-elements-ii/)
- [1210. Minimum Moves to Reach Target with Rotations](../1322-minimum-moves-to-reach-target-with-rotations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/)
