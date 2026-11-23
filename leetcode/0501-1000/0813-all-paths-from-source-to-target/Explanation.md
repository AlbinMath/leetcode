# LeetCode 797: All Paths From Source to Target

**LeetCode Problem #797 — All Paths From Source to Target**
Solve LeetCode All Paths From Source to Target using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Paths From Source to Target |
| LeetCode | #797 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a directed acyclic graph ( DAG ) of  n  nodes labeled from  0  to  n - 1 , find all possible paths from node  0  to node  n - 1  and return them in  any order .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **All Paths From Source to Target**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1786. Number of Restricted Paths From First to Last Node](../../1501-2000/1912-number-of-restricted-paths-from-first-to-last-node/)
- [2115. Find All Possible Recipes from Given Supplies](../../2001-2500/2220-find-all-possible-recipes-from-given-supplies/)
- [2920. Maximum Points After Collecting Coins From All Nodes](../../3001-3500/3179-maximum-points-after-collecting-coins-from-all-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/)
