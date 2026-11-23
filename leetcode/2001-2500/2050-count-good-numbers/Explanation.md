# LeetCode 1922: Count Good Numbers

**LeetCode Problem #1922 — Count Good Numbers**
Solve LeetCode Count Good Numbers using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Numbers |
| LeetCode | #1922 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A digit string is  good  if the digits  (0-indexed)  at  even  indices are  even  and the digits at  odd  indices are  prime  ( 2 ,  3 ,  5 , or  7 ).

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Good Numbers**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)
- [1351. Count Negative Numbers in a Sorted Matrix](../../1001-1500/1476-count-negative-numbers-in-a-sorted-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-numbers/)
