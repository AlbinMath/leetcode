# LeetCode 1894: Find the Student that Will Replace the Chalk

**LeetCode Problem #1894 — Find the Student that Will Replace the Chalk**
Solve LeetCode Find the Student that Will Replace the Chalk using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Student that Will Replace the Chalk |
| LeetCode | #1894 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are  n  students in a class numbered from  0  to  n - 1 . The teacher will give each student a problem starting with the student number  0 , then the student number  1 , and so on until the teacher reaches the student number  n - 1 . After that, the teacher will restart the process, starting with the student number  0  again.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Student that Will Replace the Chalk**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [833. Find And Replace in String](../../0501-1000/0862-find-and-replace-in-string/)
- [890. Find and Replace Pattern](../../0501-1000/0926-find-and-replace-pattern/)
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1112-find-words-that-can-be-formed-by-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/)
