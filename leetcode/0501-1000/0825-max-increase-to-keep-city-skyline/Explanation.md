# LeetCode 807: Max Increase to Keep City Skyline

**LeetCode Problem #807 — Max Increase to Keep City Skyline**
Solve LeetCode Max Increase to Keep City Skyline using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Increase to Keep City Skyline |
| LeetCode | #807 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There is a city composed of  n x n  blocks, where each block contains a single building shaped like a vertical square prism. You are given a  0-indexed   n x n  integer matrix  grid  where  grid[r][c]  represents the  height  of the building located in the block at row  r  and column  c .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Max Increase to Keep City Skyline**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](../../1501-2000/1701-remove-max-number-of-edges-to-keep-graph-fully-traversable/)
- [2154. Keep Multiplying Found Values by Two](../../2001-2500/2274-keep-multiplying-found-values-by-two/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](../../1001-1500/1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)
