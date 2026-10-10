# LeetCode 2161: Partition Array According to Given Pivot

**LeetCode Problem #2161 — Partition Array According to Given Pivot**
Solve LeetCode Partition Array According to Given Pivot using Java and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array According to Given Pivot |
| LeetCode | #2161 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  0-indexed  integer array  nums  and an integer  pivot . Rearrange  nums  such that the following conditions are satisfied:

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Three-pass approach: collect elements < pivot, then == pivot, then > pivot, and concatenate them. This maintains relative order within each partition.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Partition Array According to Given Pivot**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [561. Array Partition](../0561-array-partition/)
- [1389. Create Target Array in the Given Order](../1505-create-target-array-in-the-given-order/)
- [26. Remove Duplicates from Sorted Array](../0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-according-to-given-pivot/)
