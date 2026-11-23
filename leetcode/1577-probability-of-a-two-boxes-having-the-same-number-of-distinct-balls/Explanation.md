# LeetCode 1467: Probability of a Two Boxes Having The Same Number of Distinct Balls

**LeetCode Problem #1467 — Probability of a Two Boxes Having The Same Number of Distinct Balls**
Solve LeetCode Probability of a Two Boxes Having The Same Number of Distinct Balls using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Probability of a Two Boxes Having The Same Number of Distinct Balls |
| LeetCode | #1467 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given  2n  balls of  k  distinct colors. You will be given an integer array  balls  of size  k  where  balls[i]  is the number of balls of color  i .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Probability of a Two Boxes Having The Same Number of Distinct Balls**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [3160. Find the Number of Distinct Colors Among the Balls](../3434-find-the-number-of-distinct-colors-among-the-balls/)
- [2318. Number of Distinct Roll Sequences](../2404-number-of-distinct-roll-sequences/)
- [1519. Number of Nodes in the Sub-Tree With the Same Label](../1643-number-of-nodes-in-the-sub-tree-with-the-same-label/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
