# LeetCode 287: Find the Duplicate Number

**LeetCode Problem #287 — Find the Duplicate Number**
Solve LeetCode Find the Duplicate Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Duplicate Number |
| LeetCode | #287 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of integers  nums  containing  n + 1  integers where each integer is in the range  [1, n]  inclusive.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find the Duplicate Number**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1295. Find Numbers with Even Number of Digits](../1421-find-numbers-with-even-number-of-digits/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../2182-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)
