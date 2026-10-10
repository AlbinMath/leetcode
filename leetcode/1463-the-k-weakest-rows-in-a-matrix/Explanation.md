# LeetCode 1337: The K Weakest Rows in a Matrix

**LeetCode Problem #1337 — The K Weakest Rows in a Matrix**
Solve LeetCode The K Weakest Rows in a Matrix using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The K Weakest Rows in a Matrix |
| LeetCode | #1337 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  binary matrix  mat  of  1 &#39;s (representing soldiers) and  0 &#39;s (representing civilians). The soldiers are positioned  in front  of the civilians. That is, all the  1 &#39;s will appear to the  left  of all the  0 &#39;s in each row.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **The K Weakest Rows in a Matrix**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [23. Merge k Sorted Lists](../0023-merge-k-sorted-lists/)
- [25. Reverse Nodes in k-Group](../0025-reverse-nodes-in-k-group/)
- [54. Spiral Matrix](../0054-spiral-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)
