# LeetCode 3970: Shortest Path With At Most K Consecutive Identical Characters

**LeetCode Problem #3970 — Shortest Path With At Most K Consecutive Identical Characters**
Solve LeetCode Shortest Path With At Most K Consecutive Identical Characters using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Path With At Most K Consecutive Identical Characters |
| LeetCode | #3970 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer  n  representing the number of nodes in a  directed weighted  graph, numbered from 0 to  n - 1 . This is represented by a 2D integer array  edges , where  edges[i] = [u i , v i , w i ]  represents a directed edge from node  u i   to node  v i   with weight  w i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Path With At Most K Consecutive Identical Characters**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [4046. Minimum Cost Path With At Most K Turns](../4367-minimum-cost-path-with-at-most-k-turns/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../2229-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)
