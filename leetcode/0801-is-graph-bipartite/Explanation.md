# LeetCode 785: Is Graph Bipartite?

**LeetCode Problem #785 — Is Graph Bipartite?**
Solve LeetCode Is Graph Bipartite? using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Is Graph Bipartite? |
| LeetCode | #785 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is an  undirected  graph with  n  nodes, where each node is numbered between  0  and  n - 1 . You are given a 2D array  graph , where  graph[u]  is an array of nodes that node  u  is adjacent to. More formally, for each  v  in  graph[u] , there is an undirected edge between node  u  and node  v . The graph has the following properties:

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Is Graph Bipartite?**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [133. Clone Graph](../0133-clone-graph/)
- [882. Reachable Nodes In Subdivided Graph](../0918-reachable-nodes-in-subdivided-graph/)
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](../1701-remove-max-number-of-edges-to-keep-graph-fully-traversable/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/is-graph-bipartite/)
