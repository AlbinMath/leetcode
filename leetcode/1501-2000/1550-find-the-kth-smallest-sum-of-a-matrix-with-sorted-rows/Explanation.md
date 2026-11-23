# LeetCode 1439: Find the Kth Smallest Sum of a Matrix With Sorted Rows

**LeetCode Problem #1439 — Find the Kth Smallest Sum of a Matrix With Sorted Rows**
Solve LeetCode Find the Kth Smallest Sum of a Matrix With Sorted Rows using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Kth Smallest Sum of a Matrix With Sorted Rows |
| LeetCode | #1439 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  matrix  mat  that has its rows sorted in non-decreasing order and an integer  k .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Depth-First Search (DFS) / Breadth-First Search (BFS)**. By maintaining state efficiently in a **Tree / Graph / Grid**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Kth Smallest Sum of a Matrix With Sorted Rows**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [378. Kth Smallest Element in a Sorted Matrix](../../0001-0500/0378-kth-smallest-element-in-a-sorted-matrix/)
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii---input-array-is-sorted/)
- [1314. Matrix Block Sum](../../1001-1500/1242-matrix-block-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)
