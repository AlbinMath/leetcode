# LeetCode 2477: Minimum Fuel Cost to Report to the Capital

**LeetCode Problem #2477 — Minimum Fuel Cost to Report to the Capital**
Solve LeetCode Minimum Fuel Cost to Report to the Capital using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Fuel Cost to Report to the Capital |
| LeetCode | #2477 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of  n  cities numbered from  0  to  n - 1  and exactly  n - 1  roads. The capital city is city  0 . You are given a 2D integer array  roads  where  roads[i] = [a i , b i ]  denotes that there exists a  bidirectional road  connecting cities  a i   and  b i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Fuel Cost to Report to the Capital**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1130. Minimum Cost Tree From Leaf Values](../1228-minimum-cost-tree-from-leaf-values/)
- [1217. Minimum Cost to Move Chips to The Same Position](../1329-minimum-cost-to-move-chips-to-the-same-position/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../1485-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/)
