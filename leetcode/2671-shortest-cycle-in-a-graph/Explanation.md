# LeetCode 2608: Shortest Cycle in a Graph

**LeetCode Problem #2608 — Shortest Cycle in a Graph**
Solve LeetCode Shortest Cycle in a Graph using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest Cycle in a Graph |
| LeetCode | #2608 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a  bi-directional  graph with  n  vertices, where each vertex is labeled from  0  to  n - 1 . The edges in the graph are represented by a given 2D integer array  edges , where  edges[i] = [u i , v i ]  denotes an edge between vertex  u i   and vertex  v i  . Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Floyd Cycle Detection**. By maintaining state efficiently in a **Linked List / Pointer**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Linked List / Pointer**).
2. Process elements sequentially using **Floyd Cycle Detection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Shortest Cycle in a Graph**. Applying **Floyd Cycle Detection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2642. Design Graph With Shortest Path Calculator](../2678-design-graph-with-shortest-path-calculator/)
- [2360. Longest Cycle in a Graph](../2439-longest-cycle-in-a-graph/)
- [214. Shortest Palindrome](../0214-shortest-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-cycle-in-a-graph/)
