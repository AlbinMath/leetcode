# LeetCode 1442: Count Triplets That Can Form Two Arrays of Equal XOR

**LeetCode Problem #1442 — Count Triplets That Can Form Two Arrays of Equal XOR**
Solve LeetCode Count Triplets That Can Form Two Arrays of Equal XOR using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Triplets That Can Form Two Arrays of Equal XOR |
| LeetCode | #1442 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of integers  arr .

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **Bitwise Masking & Bit Shift**. By maintaining state efficiently in a **Integer Bitmask**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Triplets That Can Form Two Arrays of Equal XOR**. Applying **Depth-First Search (DFS) / Breadth-First Search (BFS)** yields the target result step by step.

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
- [2791. Count Paths That Can Form a Palindrome in a Tree](../../2501-3000/2905-count-paths-that-can-form-a-palindrome-in-a-tree/)
- [2201. Count Artifacts That Can Be Extracted](../../1001-1500/1312-count-artifacts-that-can-be-extracted/)
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../../3501-4000/3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)
