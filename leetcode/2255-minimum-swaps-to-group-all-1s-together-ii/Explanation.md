# LeetCode 2134: Minimum Swaps to Group All 1's Together II

**LeetCode Problem #2134 — Minimum Swaps to Group All 1's Together II**
Solve LeetCode Minimum Swaps to Group All 1's Together II using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps to Group All 1's Together II |
| LeetCode | #2134 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A  swap  is defined as taking two  distinct  positions in an array and swapping the values in them.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Swaps to Group All 1's Together II**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1437. Check If All 1's Are at Least Length K Places Away](../1548-check-if-all-1s-are-at-least-length-k-places-away/)
- [1247. Minimum Swaps to Make Strings Equal](../1369-minimum-swaps-to-make-strings-equal/)
- [1266. Minimum Time Visiting All Points](../1395-minimum-time-visiting-all-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/)
