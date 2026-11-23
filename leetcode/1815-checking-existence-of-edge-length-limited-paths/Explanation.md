# LeetCode 1697: Checking Existence of Edge Length Limited Paths

**LeetCode Problem #1697 — Checking Existence of Edge Length Limited Paths**
Solve LeetCode Checking Existence of Edge Length Limited Paths using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Checking Existence of Edge Length Limited Paths |
| LeetCode | #1697 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
An undirected graph of  n  nodes is defined by  edgeList , where  edgeList[i] = [u i , v i , dis i ]  denotes an edge between nodes  u i   and  v i   with distance  dis i  . Note that there may be  multiple  edges between two nodes.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Checking Existence of Edge Length Limited Paths**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [58. Length of Last Word](../0058-length-of-last-word/)
- [718. Maximum Length of Repeated Subarray](../0718-maximum-length-of-repeated-subarray/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../1360-maximum-length-of-a-concatenated-string-with-unique-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/)
