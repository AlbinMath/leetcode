# LeetCode 2322: Minimum Score After Removals on a Tree

**LeetCode Problem #2322 — Minimum Score After Removals on a Tree**
Solve LeetCode Minimum Score After Removals on a Tree using Java and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Score After Removals on a Tree |
| LeetCode | #2322 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an undirected connected tree with  n  nodes labeled from  0  to  n - 1  and  n - 1  edges.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Score After Removals on a Tree**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [3746. Minimum String Length After Balanced Removals](../4090-minimum-string-length-after-balanced-removals/)
- [861. Score After Flipping Matrix](../0891-score-after-flipping-matrix/)
- [1422. Maximum Score After Splitting a String](../1537-maximum-score-after-splitting-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/)
