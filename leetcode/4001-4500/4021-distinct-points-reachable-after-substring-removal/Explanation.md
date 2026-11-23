# LeetCode 3694: Distinct Points Reachable After Substring Removal

**LeetCode Problem #3694 — Distinct Points Reachable After Substring Removal**
Solve LeetCode Distinct Points Reachable After Substring Removal using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Points Reachable After Substring Removal |
| LeetCode | #3694 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  consisting of characters  &#39;U&#39; ,  &#39;D&#39; ,  &#39;L&#39; , and  &#39;R&#39; , representing moves on an infinite 2D Cartesian grid.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Distinct Points Reachable After Substring Removal**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [1946. Largest Number After Mutating Substring](../../2001-2500/2077-largest-number-after-mutating-substring/)
- [3503. Longest Palindrome After Substring Concatenation I](../../3501-4000/3793-longest-palindrome-after-substring-concatenation-i/)
- [2458. Height of Binary Tree After Subtree Removal Queries](../../2501-3000/2545-height-of-binary-tree-after-subtree-removal-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/)
