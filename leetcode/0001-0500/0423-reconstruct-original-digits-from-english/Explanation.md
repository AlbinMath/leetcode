# LeetCode 423: Reconstruct Original Digits from English

**LeetCode Problem #423 — Reconstruct Original Digits from English**
Solve LeetCode Reconstruct Original Digits from English using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reconstruct Original Digits from English |
| LeetCode | #423 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s  containing an out-of-order English representation of digits  0-9 , return  the digits in  ascending  order .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Mathematical Simulation & Modular Arithmetic**. By maintaining state efficiently in a **Primitive Types**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reconstruct Original Digits from English**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [258. Add Digits](../../0001-0500/0258-add-digits/)
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)
- [402. Remove K Digits](../../0001-0500/0402-remove-k-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reconstruct-original-digits-from-english/)
