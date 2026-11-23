# LeetCode 1754: Largest Merge Of Two Strings

**LeetCode Problem #1754 — Largest Merge Of Two Strings**
Solve LeetCode Largest Merge Of Two Strings using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Merge Of Two Strings |
| LeetCode | #1754 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two strings  word1  and  word2 . You want to construct a string  merge  in the following way: while either  word1  or  word2  are non-empty, choose  one  of the following options:

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Largest Merge Of Two Strings**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1624. Largest Substring Between Two Equal Characters](../../1501-2000/1746-largest-substring-between-two-equal-characters/)
- [3047. Find the Largest Area of Square Inside Two Rectangles](../../3001-3500/3325-find-the-largest-area-of-square-inside-two-rectangles/)
- [583. Delete Operation for Two Strings](../../0501-1000/0583-delete-operation-for-two-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-merge-of-two-strings/)
