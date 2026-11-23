# LeetCode 2396: Strictly Palindromic Number

**LeetCode Problem #2396 — Strictly Palindromic Number**
Solve LeetCode Strictly Palindromic Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Strictly Palindromic Number |
| LeetCode | #2396 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
An integer  n  is  strictly palindromic  if, for  every  base  b  between  2  and  n - 2  ( inclusive ), the string representation of the integer  n  in base  b  is  palindromic .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Strictly Palindromic Number**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1909. Remove One Element to Make the Array Strictly Increasing](../../2001-2500/2020-remove-one-element-to-make-the-array-strictly-increasing/)
- [2713. Maximum Strictly Increasing Cells in a Matrix](../../2501-3000/2818-maximum-strictly-increasing-cells-in-a-matrix/)
- [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](../../3001-3500/3372-longest-strictly-increasing-or-strictly-decreasing-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/strictly-palindromic-number/)
