# LeetCode 2043: Simple Bank System

**LeetCode Problem #2043 — Simple Bank System**
Solve LeetCode Simple Bank System using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Simple Bank System |
| LeetCode | #2043 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  integer matrix  grid ​​​, where  m  and  n  are both  even  integers, and an integer  k .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. **Extract Layers:** For each concentric ring of the grid, extract the elements into a 1D array by traversing the ring clockwise.
2. **Rotate:** Rotate the 1D array by `k % length` positions.
3. **Place Back:** Write the rotated elements back into the corresponding positions in the grid.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Simple Bank System**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1386. Cinema Seat Allocation](../1386-shift-2d-grid/)
- [1972. First and Last Call On the Same Day](../1972-rotating-the-box/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../2914-find-the-safest-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cyclically-rotating-a-grid/)
