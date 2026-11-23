# LeetCode 3863: Minimum Operations to Sort a String

**LeetCode Problem #3863 — Minimum Operations to Sort a String**
Solve LeetCode Minimum Operations to Sort a String using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Sort a String |
| LeetCode | #3863 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  consisting of lowercase English letters.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Operations to Sort a String**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1585. Check If String Is Transformable With Substring Sort Operations](../../1501-2000/1707-check-if-string-is-transformable-with-substring-sort-operations/)
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1941-minimum-number-of-operations-to-make-string-sorted/)
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2501-3000/2558-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-string/)
