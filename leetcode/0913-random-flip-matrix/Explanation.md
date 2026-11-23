# LeetCode 519: Random Flip Matrix

**LeetCode Problem #519 — Random Flip Matrix**
Solve LeetCode Random Flip Matrix using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Random Flip Matrix |
| LeetCode | #519 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an  m x n  binary grid  matrix  with all the values set  0  initially. Design an algorithm to randomly pick an index  (i, j)  where  matrix[i][j] == 0  and flips it to  1 . All the indices  (i, j)  where  matrix[i][j] == 0  should be equally likely to be returned.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Random Flip Matrix**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2556. Disconnect Path in a Binary Matrix by at Most One Flip](../2641-disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)
- [54. Spiral Matrix](../0054-spiral-matrix/)
- [59. Spiral Matrix II](../0059-spiral-matrix-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/random-flip-matrix/)
