# LeetCode 3105: Longest Strictly Increasing or Strictly Decreasing Subarray

**LeetCode Problem #3105 — Longest Strictly Increasing or Strictly Decreasing Subarray**
Solve LeetCode Longest Strictly Increasing or Strictly Decreasing Subarray using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Strictly Increasing or Strictly Decreasing Subarray |
| LeetCode | #3105 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are given an array of integers  nums . Return  the length of the  longest   subarray  of   nums   which is either   strictly increasing   or   strictly decreasing   .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Longest Strictly Increasing or Strictly Decreasing Subarray**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../4032-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)
- [1909. Remove One Element to Make the Array Strictly Increasing](../2020-remove-one-element-to-make-the-array-strictly-increasing/)
- [2713. Maximum Strictly Increasing Cells in a Matrix](../2818-maximum-strictly-increasing-cells-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)
