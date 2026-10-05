# LeetCode 3559: Number of Ways to Assign Edge Weights II

**LeetCode Problem #3559 — Number of Ways to Assign Edge Weights II**
Solve LeetCode Number of Ways to Assign Edge Weights II using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Assign Edge Weights II |
| LeetCode | #3559 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an undirected tree with  n  nodes labeled from 1 to  n , rooted at node 1. The tree is represented by a 2D integer array  edges  of length  n - 1 , where  edges[i] = [u i , v i ]  indicates that there is an edge between nodes  u i   and  v i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **SQL Query / Relational Join & Grouping**. By maintaining state efficiently in a **Relational Table**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Ways to Assign Edge Weights II**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3558. Number of Ways to Assign Edge Weights I](../3844-number-of-ways-to-assign-edge-weights-i/)
- [3016. Minimum Number of Pushes to Type Word II](../3276-minimum-number-of-pushes-to-type-word-ii/)
- [3514. Number of Unique XOR Triplets II](../3820-number-of-unique-xor-triplets-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/)
