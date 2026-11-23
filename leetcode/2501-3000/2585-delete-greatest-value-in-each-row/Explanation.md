# LeetCode 2500: Delete Greatest Value in Each Row

**LeetCode Problem #2500 — Delete Greatest Value in Each Row**
Solve LeetCode Delete Greatest Value in Each Row using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Greatest Value in Each Row |
| LeetCode | #2500 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  matrix  grid  consisting of positive integers.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Delete Greatest Value in Each Row**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [2003. Smallest Missing Genetic Value in Each Subtree](../../2001-2500/2131-smallest-missing-genetic-value-in-each-subtree/)
- [1325. Delete Leaves With a Given Value](../../1001-1500/1450-delete-leaves-with-a-given-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-greatest-value-in-each-row/)
