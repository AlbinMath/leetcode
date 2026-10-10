# LeetCode 1779: Find Nearest Point That Has the Same X or Y Coordinate

**LeetCode Problem #1779 — Find Nearest Point That Has the Same X or Y Coordinate**
Solve LeetCode Find Nearest Point That Has the Same X or Y Coordinate using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Nearest Point That Has the Same X or Y Coordinate |
| LeetCode | #1779 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two integers,  x  and  y , which represent your current location on a Cartesian grid:  (x, y) . You are also given an array  points  where each  points[i] = [a i , b i ]  represents that a point exists at  (a i , b i ) . A point is  valid  if it shares the same x-coordinate or the same y-coordinate as your location.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find Nearest Point That Has the Same X or Y Coordinate**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1160. Find Words That Can Be Formed by Characters](../1112-find-words-that-can-be-formed-by-characters/)
- [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](../1498-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [3524. Find X Value of Array I](../3831-find-x-value-of-array-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/)
