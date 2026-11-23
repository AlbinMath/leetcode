# LeetCode 1046: Last Stone Weight

**LeetCode Problem #1046 — Last Stone Weight**
Solve LeetCode Last Stone Weight using JavaScript, Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Last Stone Weight |
| LeetCode | #1046 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an array of integers  stones  where  stones[i]  is the weight of the  i th   stone.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Last Stone Weight**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
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
- [528. Random Pick with Weight](../../0501-1000/0912-random-pick-with-weight/)
- [2846. Minimum Edge Weight Equilibrium Queries in a Tree](../../3001-3500/3079-minimum-edge-weight-equilibrium-queries-in-a-tree/)
- [3419. Minimize the Maximum Edge Weight of Graph](../../3501-4000/3720-minimize-the-maximum-edge-weight-of-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-stone-weight/)
