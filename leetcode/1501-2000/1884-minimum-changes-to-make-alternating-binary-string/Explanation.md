# LeetCode 1758: Minimum Changes To Make Alternating Binary String

**LeetCode Problem #1758 — Minimum Changes To Make Alternating Binary String**
Solve LeetCode Minimum Changes To Make Alternating Binary String using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Changes To Make Alternating Binary String |
| LeetCode | #1758 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  consisting only of the characters  &#39;0&#39;  and  &#39;1&#39; . In one operation, you can change any  &#39;0&#39;  to  &#39;1&#39;  or vice versa.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Changes To Make Alternating Binary String**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [2914. Minimum Number of Changes to Make Binary String Beautiful](../../3001-3500/3174-minimum-number-of-changes-to-make-binary-string-beautiful/)
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1994-minimum-number-of-swaps-to-make-the-binary-string-alternating/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../2001-2500/2017-minimum-number-of-flips-to-make-the-binary-string-alternating/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/)
