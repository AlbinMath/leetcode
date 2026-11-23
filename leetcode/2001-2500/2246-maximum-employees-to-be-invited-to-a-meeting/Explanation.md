# LeetCode 2127: Maximum Employees to Be Invited to a Meeting

**LeetCode Problem #2127 — Maximum Employees to Be Invited to a Meeting**
Solve LeetCode Maximum Employees to Be Invited to a Meeting using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Employees to Be Invited to a Meeting |
| LeetCode | #2127 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A company is organizing a meeting and has a list of  n  employees, waiting to be invited. They have arranged for a large  circular  table, capable of seating  any number  of employees.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Employees to Be Invited to a Meeting**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1112-find-words-that-can-be-formed-by-characters/)
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../../1501-2000/1679-shortest-subarray-to-be-removed-to-make-array-sorted/)
- [1886. Determine Whether Matrix Can Be Obtained By Rotation](../../2001-2500/2015-determine-whether-matrix-can-be-obtained-by-rotation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/)
