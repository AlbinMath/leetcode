# LeetCode 1905: Count Sub Islands

**LeetCode Problem #1905 — Count Sub Islands**
Solve LeetCode Count Sub Islands using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Sub Islands |
| LeetCode | #1905 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given two  m x n  binary matrices  grid1  and  grid2  containing only  0 &#39;s (representing water) and  1 &#39;s (representing land). An  island  is a group of  1 &#39;s connected  4-directionally  (horizontal or vertical). Any cells outside of the grid are considered water cells.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Count Sub Islands**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [2902. Count of Sub-Multisets With Bounded Sum](../3091-count-of-sub-multisets-with-bounded-sum/)
- [3619. Count Islands With Total Value Divisible by K](../3823-count-islands-with-total-value-divisible-by-k/)
- [38. Count and Say](../0038-count-and-say/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-sub-islands/)
