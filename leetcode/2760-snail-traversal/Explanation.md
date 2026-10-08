# LeetCode 2624: Snail Traversal

**LeetCode Problem #2624 — Snail Traversal**
Solve LeetCode Snail Traversal using TypeScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Snail Traversal |
| LeetCode | #2624 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write code that enhances all arrays such that you can call the  snail(rowsCount, colsCount)  method that transforms the 1D array into a 2D array organised in the pattern known as  snail traversal order . Invalid input values should output an empty array. If  rowsCount * colsCount !== nums.length , the input is considered invalid.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Fills the matrix column by column. Even-indexed columns fill top-to-bottom; odd-indexed columns fill bottom-to-top, creating the snail pattern.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Snail Traversal**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)

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
- [94. Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/)
- [144. Binary Tree Preorder Traversal](../0144-binary-tree-preorder-traversal/)
- [145. Binary Tree Postorder Traversal](../0145-binary-tree-postorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/snail-traversal/)
