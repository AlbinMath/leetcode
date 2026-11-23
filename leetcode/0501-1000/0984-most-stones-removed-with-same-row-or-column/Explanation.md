# LeetCode 947: Most Stones Removed with Same Row or Column

**LeetCode Problem #947 — Most Stones Removed with Same Row or Column**
Solve LeetCode Most Stones Removed with Same Row or Column using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Stones Removed with Same Row or Column |
| LeetCode | #947 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
On a 2D plane, we place  n  stones at some integer coordinate points. Each coordinate point may have at most one stone.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Most Stones Removed with Same Row or Column**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2352. Equal Row and Column Pairs](../../2001-2500/2428-equal-row-and-column-pairs/)
- [2482. Difference Between Ones and Zeros in Row and Column](../../2501-3000/2606-difference-between-ones-and-zeros-in-row-and-column/)
- [1574. Shortest Subarray to be Removed to Make Array Sorted](../../1501-2000/1679-shortest-subarray-to-be-removed-to-make-array-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)
