# LeetCode 802: Find Eventual Safe States

**LeetCode Problem #802 — Find Eventual Safe States**
Solve LeetCode Find Eventual Safe States using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Eventual Safe States |
| LeetCode | #802 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a directed graph of  n  nodes with each node labeled from  0  to  n - 1 . The graph is represented by a  0-indexed  2D integer array  graph  where  graph[i]  is an integer array of nodes adjacent to node  i , meaning there is an edge from node  i  to each node in  graph[i] .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Eventual Safe States**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3286. Find a Safe Walk Through a Grid](../3558-find-a-safe-walk-through-a-grid/)
- [753. Cracking the Safe](../0754-cracking-the-safe/)
- [28. Find the Index of the First Occurrence in a String](../0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-eventual-safe-states/)
