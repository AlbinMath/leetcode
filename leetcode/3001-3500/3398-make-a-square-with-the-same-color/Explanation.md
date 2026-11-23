# LeetCode 3127: Make a Square with the Same Color

**LeetCode Problem #3127 — Make a Square with the Same Color**
Solve LeetCode Make a Square with the Same Color using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make a Square with the Same Color |
| LeetCode | #3127 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a 2D matrix  grid  of size  3 x 3  consisting only of characters  &#39;B&#39;  and  &#39;W&#39; . Character  &#39;W&#39;  represents the white color , and character  &#39;B&#39;  represents the black color .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Make a Square with the Same Color**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2038. Remove Colored Pieces if Both Neighbors are the Same Color](../../2001-2500/2149-remove-colored-pieces-if-both-neighbors-are-the-same-color/)
- [1812. Determine Color of a Chessboard Square](../../1501-2000/1920-determine-color-of-a-chessboard-square/)
- [100. Same Tree](../../0001-0500/0100-same-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-a-square-with-the-same-color/)
