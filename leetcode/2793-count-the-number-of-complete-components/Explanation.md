# LeetCode 2685: Count the Number of Complete Components

**LeetCode Problem #2685 — Count the Number of Complete Components**
Solve LeetCode Count the Number of Complete Components using Java and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Complete Components |
| LeetCode | #2685 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an integer  n . There is an  undirected  graph with  n  vertices, numbered from  0  to  n - 1 . You are given a 2D integer array  edges  where  edges[i] = [a i , b i ]  denotes that there exists an  undirected  edge connecting vertices  a i   and  b i  .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Use **BFS/DFS or Union-Find** to find connected components. For each component with `v` vertices and `e` edges, it's complete if `e == v*(v-1)/2`.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count the Number of Complete Components**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [1684. Count the Number of Consistent Strings](../1786-count-the-number-of-consistent-strings/)
- [3120. Count the Number of Special Characters I](../3408-count-the-number-of-special-characters-i/)
- [9. Palindrome Number](../0009-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-complete-components/)
