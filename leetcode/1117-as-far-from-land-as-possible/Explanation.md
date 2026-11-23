# LeetCode 1162: As Far from Land as Possible

**LeetCode Problem #1162 — As Far from Land as Possible**
Solve LeetCode As Far from Land as Possible using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | As Far from Land as Possible |
| LeetCode | #1162 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an  n x n   grid  containing only values  0  and  1 , where  0  represents water and  1  represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return  -1 .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **As Far from Land as Possible**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2115. Find All Possible Recipes from Given Supplies](../2220-find-all-possible-recipes-from-given-supplies/)
- [352. Data Stream as Disjoint Intervals](../0352-data-stream-as-disjoint-intervals/)
- [558. Logical OR of Two Binary Grids Represented as Quad-Trees](../0773-logical-or-of-two-binary-grids-represented-as-quad-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/as-far-from-land-as-possible/)
