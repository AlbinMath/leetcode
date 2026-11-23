# LeetCode 4046: Minimum Cost Path With At Most K Turns

**LeetCode Problem #4046 — Minimum Cost Path With At Most K Turns**
Solve LeetCode Minimum Cost Path With At Most K Turns using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Path With At Most K Turns |
| LeetCode | #4046 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a 2D integer array  grid  of size  m x n , where  grid[i][j]  represents the cost of visiting cell  (i, j) , and an integer  k .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost Path With At Most K Turns**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../3714-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)
- [3430. Maximum and Minimum Sums of at Most Size K Subarrays](../3725-maximum-and-minimum-sums-of-at-most-size-k-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/)
