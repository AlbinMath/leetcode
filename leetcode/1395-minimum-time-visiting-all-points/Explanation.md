# LeetCode 1266: Minimum Time Visiting All Points

**LeetCode Problem #1266 — Minimum Time Visiting All Points**
Solve LeetCode Minimum Time Visiting All Points using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time Visiting All Points |
| LeetCode | #1266 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
On a 2D plane, there are  n  points with integer coordinates  points[i] = [x i , y i ] . Return  the  minimum time  in seconds to visit all the points in the order given by   points .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Time Visiting All Points**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1443. Minimum Time to Collect All Apples in a Tree](../1554-minimum-time-to-collect-all-apples-in-a-tree/)
- [1723. Find Minimum Time to Finish All Jobs](../1825-find-minimum-time-to-finish-all-jobs/)
- [2589. Minimum Time to Complete All Tasks](../2657-minimum-time-to-complete-all-tasks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-visiting-all-points/)
