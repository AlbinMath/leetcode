# LeetCode 3464: Maximize the Distance Between Points on a Square

**LeetCode Problem #3464 — Maximize the Distance Between Points on a Square**
Solve LeetCode Maximize the Distance Between Points on a Square using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Distance Between Points on a Square |
| LeetCode | #3464 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer   side  , representing the edge length of a square with corners at  (0, 0) ,  (0, side) ,  (side, 0) , and  (side, side)  on a Cartesian plane.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximize the Distance Between Points on a Square**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [783. Minimum Distance Between BST Nodes](../0799-minimum-distance-between-bst-nodes/)
- [1385. Find the Distance Value Between Two Arrays](../1486-find-the-distance-value-between-two-arrays/)
- [1617. Count Subtrees With Max Distance Between Cities](../1740-count-subtrees-with-max-distance-between-cities/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/)
