# LeetCode 3964: Minimum Lights to Illuminate a Road

**LeetCode Problem #3964 — Minimum Lights to Illuminate a Road**
Solve LeetCode Minimum Lights to Illuminate a Road using PHP and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Lights to Illuminate a Road |
| LeetCode | #3964 |
| Difficulty | Medium |
| Language | PHP |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given three integers  n ,  l , and  r .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Iterative Traversal**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Lights to Illuminate a Road**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
PHP

## Source Code
- [solution.php](./solution.php)

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
- [3962. Maximum Subarray Sum After at Most K Swaps](../3962-number-of-zigzag-arrays-i/)
- [3276. Select Cells in Grid With Maximum Score](../3276-minimum-number-of-pushes-to-type-word-ii/)
- [3820. Pythagorean Distance Nodes in a Tree](../3820-number-of-unique-xor-triplets-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-ii/)
