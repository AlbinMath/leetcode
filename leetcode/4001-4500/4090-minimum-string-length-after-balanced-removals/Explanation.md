# LeetCode 3746: Minimum String Length After Balanced Removals

**LeetCode Problem #3746 — Minimum String Length After Balanced Removals**
Solve LeetCode Minimum String Length After Balanced Removals using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum String Length After Balanced Removals |
| LeetCode | #3746 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  consisting only of the characters  &#39;a&#39;  and  &#39;b&#39; .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum String Length After Balanced Removals**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1850-minimum-length-of-string-after-deleting-similar-ends/)
- [2696. Minimum String Length After Removing Substrings](../../2501-3000/2800-minimum-string-length-after-removing-substrings/)
- [1653. Minimum Deletions to Make String Balanced](../../1501-2000/1756-minimum-deletions-to-make-string-balanced/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-string-length-after-balanced-removals/)
