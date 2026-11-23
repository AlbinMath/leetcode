# LeetCode 3257: Maximum Value Sum by Placing Three Rooks II

**LeetCode Problem #3257 — Maximum Value Sum by Placing Three Rooks II**
Solve LeetCode Maximum Value Sum by Placing Three Rooks II using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value Sum by Placing Three Rooks II |
| LeetCode | #3257 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  m x n  2D array  board  representing a chessboard, where  board[i][j]  represents the  value  of the cell  (i, j) .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Value Sum by Placing Three Rooks II**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3256. Maximum Value Sum by Placing Three Rooks I](../3550-maximum-value-sum-by-placing-three-rooks-i/)
- [124. Binary Tree Maximum Path Sum](../0124-binary-tree-maximum-path-sum/)
- [628. Maximum Product of Three Numbers](../0628-maximum-product-of-three-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/)
