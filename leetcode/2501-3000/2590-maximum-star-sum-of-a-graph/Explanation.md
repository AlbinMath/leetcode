# LeetCode 2497: Maximum Star Sum of a Graph

**LeetCode Problem #2497 — Maximum Star Sum of a Graph**
Solve LeetCode Maximum Star Sum of a Graph using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Star Sum of a Graph |
| LeetCode | #2497 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an undirected graph consisting of  n  nodes numbered from  0  to  n - 1 . You are given a  0-indexed  integer array  vals  of length  n  where  vals[i]  denotes the value of the  i th   node.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Star Sum of a Graph**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3547. Maximum Sum of Edge Values in a Graph](../../3501-4000/3845-maximum-sum-of-edge-values-in-a-graph/)
- [1791. Find Center of Star Graph](../../1501-2000/1916-find-center-of-star-graph/)
- [2065. Maximum Path Quality of a Graph](../../2001-2500/2189-maximum-path-quality-of-a-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-star-sum-of-a-graph/)
