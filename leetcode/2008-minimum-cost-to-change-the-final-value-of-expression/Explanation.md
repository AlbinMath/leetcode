# LeetCode 1896: Minimum Cost to Change the Final Value of Expression

**LeetCode Problem #1896 — Minimum Cost to Change the Final Value of Expression**
Solve LeetCode Minimum Cost to Change the Final Value of Expression using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Change the Final Value of Expression |
| LeetCode | #1896 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a  valid  boolean expression as a string  expression  consisting of the characters  &#39;1&#39; , &#39;0&#39; , &#39;&&#39;  (bitwise  AND  operator), &#39;|&#39;  (bitwise  OR  operator), &#39;(&#39; , and  &#39;)&#39; .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Minimum Cost to Change the Final Value of Expression**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2011. Final Value of Variable After Performing Operations](../2137-final-value-of-variable-after-performing-operations/)
- [1413. Minimum Value to Get Positive Step by Step Sum](../1514-minimum-value-to-get-positive-step-by-step-sum/)
- [2540. Minimum Common Value](../2634-minimum-common-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/)
