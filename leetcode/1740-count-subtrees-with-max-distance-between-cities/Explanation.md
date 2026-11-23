# LeetCode 1617: Count Subtrees With Max Distance Between Cities

**LeetCode Problem #1617 — Count Subtrees With Max Distance Between Cities**
Solve LeetCode Count Subtrees With Max Distance Between Cities using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subtrees With Max Distance Between Cities |
| LeetCode | #1617 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are  n  cities numbered from  1  to  n . You are given an array  edges  of size  n-1 , where  edges[i] = [u i , v i ]  represents a bidirectional edge between cities  u i   and  v i  . There exists a unique path between each pair of cities. In other words, the cities form a  tree .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Subtrees With Max Distance Between Cities**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [783. Minimum Distance Between BST Nodes](../0799-minimum-distance-between-bst-nodes/)
- [1385. Find the Distance Value Between Two Arrays](../1486-find-the-distance-value-between-two-arrays/)
- [2492. Minimum Score of a Path Between Two Cities](../2582-minimum-score-of-a-path-between-two-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/)
