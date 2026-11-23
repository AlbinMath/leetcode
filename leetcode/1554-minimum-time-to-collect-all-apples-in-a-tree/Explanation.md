# LeetCode 1443: Minimum Time to Collect All Apples in a Tree

**LeetCode Problem #1443 — Minimum Time to Collect All Apples in a Tree**
Solve LeetCode Minimum Time to Collect All Apples in a Tree using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Collect All Apples in a Tree |
| LeetCode | #1443 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an undirected tree consisting of  n  vertices numbered from  0  to  n-1 , which has some apples in their vertices. You spend 1 second to walk over one edge of the tree.  Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at  vertex 0  and coming back to this vertex.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Time to Collect All Apples in a Tree**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1266. Minimum Time Visiting All Points](../1395-minimum-time-visiting-all-points/)
- [1723. Find Minimum Time to Finish All Jobs](../1825-find-minimum-time-to-finish-all-jobs/)
- [2589. Minimum Time to Complete All Tasks](../2657-minimum-time-to-complete-all-tasks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/)
