# LeetCode 2003: Smallest Missing Genetic Value in Each Subtree

**LeetCode Problem #2003 — Smallest Missing Genetic Value in Each Subtree**
Solve LeetCode Smallest Missing Genetic Value in Each Subtree using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Genetic Value in Each Subtree |
| LeetCode | #2003 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There is a  family tree  rooted at  0  consisting of  n  nodes numbered  0  to  n - 1 . You are given a  0-indexed  integer array  parents , where  parents[i]  is the parent for node  i . Since node  0  is the  root ,  parents[0] == -1 .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Missing Genetic Value in Each Subtree**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [865. Smallest Subtree with all the Deepest Nodes](../0896-smallest-subtree-with-all-the-deepest-nodes/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)
- [3718. Smallest Missing Multiple of K](../4080-smallest-missing-multiple-of-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/)
