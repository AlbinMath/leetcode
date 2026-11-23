# LeetCode 2065: Maximum Path Quality of a Graph

**LeetCode Problem #2065 — Maximum Path Quality of a Graph**
Solve LeetCode Maximum Path Quality of a Graph using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Path Quality of a Graph |
| LeetCode | #2065 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is an  undirected  graph with  n  nodes numbered from  0  to  n - 1  ( inclusive ). You are given a  0-indexed  integer array  values  where  values[i]  is the  value  of the  i th   node. You are also given a  0-indexed  2D integer array  edges , where each  edges[j] = [u j , v j , time j ]  indicates that there is an undirected edge between the nodes  u j   and  v j  ,   and it takes  time j   seconds to travel between the two nodes. Finally, you are given an integer  maxTime .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Path Quality of a Graph**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1971. Find if Path Exists in Graph](../../2001-2500/2121-find-if-path-exists-in-graph/)
- [2497. Maximum Star Sum of a Graph](../../2501-3000/2590-maximum-star-sum-of-a-graph/)
- [2642. Design Graph With Shortest Path Calculator](../../2501-3000/2678-design-graph-with-shortest-path-calculator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-path-quality-of-a-graph/)
